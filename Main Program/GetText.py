from flask import Flask, jsonify, request
from flask_cors import CORS
from joblib import load
from playwright.sync_api import sync_playwright
from urllib.parse import urljoin, urlparse
from collections import deque
import re
import time
import warnings
from databaseDP import upload_data

app = Flask(__name__)
CORS(app)
warnings.filterwarnings("ignore")

EXCLUDED_KEYWORDS = [
    'login', 'signin', 'signup', 'register',
    'cart', 'checkout', 'basket',
    'wishlist', 'account', 'profile', 'member'
]

presence_classifier = load('presence_classifier.joblib')
presence_vect = load('presence_vectorizer.joblib')
category_classifier = load('category_classifier.joblib')
category_vect = load('category_vectorizer.joblib')

def get_text_and_links_from_site(page):
    all_text = []
    content = page.locator("main, body").all_inner_texts()
    for section in content:
        for line in section.split("\n"):
            if line.strip():
                all_text.append(line.strip())
    links = set()
    hrefs = page.locator("a").evaluate_all("els => els.map(e => e.href)")
    for href in hrefs:
        if href:
            links.add(href)
    return all_text, list(links)

def bfs_crawler(start_url, max_pages=10):
    all_crawled_text = []
    visited = set()
    queue = deque([start_url])
    pages_crawled = 0
    base_domain = urlparse(start_url).netloc.replace("www.", "").lower()
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(ignore_https_errors=True)
        page = context.new_page()
        while queue and pages_crawled < max_pages:
            current_url = queue.popleft()
            if current_url in visited:
                continue
            print(f"Crawling ({pages_crawled + 1}/{max_pages}): {current_url}")
            try:
                page.goto(current_url, timeout=15000)
                time.sleep(1.5)
                text, links = get_text_and_links_from_site(page)
                if not text:
                    continue
                all_crawled_text.extend(text)
                visited.add(current_url)
                pages_crawled += 1
                for link in links:
                    absolute_link = urljoin(current_url, link)
                    parsed = urlparse(absolute_link)
                    domain = parsed.netloc.replace("www.", "").lower()
                    if (
                        parsed.scheme in ["http", "https"]
                        and domain == base_domain
                        and absolute_link not in visited
                        and not any(k in absolute_link.lower() for k in EXCLUDED_KEYWORDS)
                    ):
                        queue.append(absolute_link)
            except Exception as e:
                print(f"Could not crawl {current_url}: {e}")
                continue
        browser.close()
    print(f"BFS completed. Crawled {pages_crawled} pages.")
    return all_crawled_text

def analyze_text(all_text):
    Darkpatterns = []
    for token in all_text:
        result = presence_classifier.predict(presence_vect.transform([token]))
        if result == "Dark":
            Darkpatterns.append(token)
    DarkpatternsClassification = []
    unique_pattern_list = []
    for tokenDark in Darkpatterns:
        res = category_classifier.predict(category_vect.transform([tokenDark]))
        if res[0] not in unique_pattern_list:
            unique_pattern_list.append(res[0])
        DarkpatternsClassification.append([tokenDark, res[0]])
    mark = split_strings(Darkpatterns)
    score = dark_score(unique_pattern_list)
    return {
        "list": unique_pattern_list,
        "Darkpatterns": len(Darkpatterns),
        "score": score,
        "marking": mark
    }, DarkpatternsClassification, len(Darkpatterns), score

def dark_score(patterns):
    score = 100
    for pattern in patterns:
        if pattern in ['Scarcity', 'Urgency', 'Misdirection']:
            score -= 5
        elif pattern in ['Obstruction', 'Sneaking']:
            score -= 15
        else:
            score -= 20
    return max(0, score)

def split_strings(lst):
    pattern = re.compile(r'[^\w\s,\-\'"\.]', re.UNICODE)
    split_list = []
    for string in lst:
        parts = re.split(pattern, string)
        parts_filtered = [part for part in parts if part]
        split_list.extend(parts_filtered)
    return split_list

@app.route("/", methods=["POST", "OPTIONS"])
def crawl_and_analyze_main():
    if request.method == "OPTIONS":
        return jsonify({"message": "CORS preflight successful"}), 200
    data = request.get_json(silent=True)
    if not data or "url" not in data:
        return jsonify({"error": "No URL provided"}), 400
    url = data["url"]
    print(f"Starting BFS crawl and analysis for: {url}")
    all_crawled_text = bfs_crawler(url, max_pages=10)
    final, classification, count, score = analyze_text(all_crawled_text)
    try:
        upload_data(url, classification, count, final["list"], score)
    except Exception as db_err:
        print(f"Database upload failed: {db_err}")
    print("Completed BFS + analysis.")
    return jsonify(final)

if __name__ == '__main__':
    app.run(port=5000, threaded=True, debug=True, use_reloader=False)
