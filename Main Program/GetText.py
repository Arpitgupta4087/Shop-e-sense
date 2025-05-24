from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from joblib import load
import warnings
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


warnings.filterwarnings("ignore")

presence_classifier = load('presence_classifier.joblib')
presence_vect = load('presence_vectorizer.joblib')
category_classifier = load('category_classifier.joblib')
category_vect = load('category_vectorizer.joblib')

def get_all_text_from_site(url):

    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    options.add_argument('--blink-settings=imagesEnabled=false')

    # Set up the Chrome WebDriver without additional options
    driver = webdriver.Chrome(options=options)

    # Open the URL
    driver.get(url)

    # Wait for the page to load
    time.sleep(5)  # Adjust this delay as necessary to ensure the page loads completely

    # Extract all text elements from the page and split by newline
    elements = driver.find_elements(By.XPATH, '/html/body')
    all_text = []
    for element in elements:
        texts = element.text.split('\n')
        for text in texts:
            if text.strip():  # This checks if the text is not just whitespace
                all_text.append(text.strip())

    # Close the browser
    driver.quit()

    return all_text
@app.route('/', methods=['POST'])
def main():
    try:
        if request.method =='POST':

            print("Started...\n")
            # Example usage
            url = (list((request.json).values()))[0]
            print(url)
            all_text = get_all_text_from_site(url)
            #print("\n".join(all_text))
            #print(all_text)

            Darkpatterns=[] # Consists dark pattern strings
            #print(all_text)
            for token in all_text:
                result = presence_classifier.predict(presence_vect.transform([token]))
                if result=="Dark":
                    Darkpatterns.append(token)

            #print("Dark patter Strings:\n",Darkpatterns)

            len_darkpatterns= len(Darkpatterns)

            DarkpatternsClassification=[]
            unique_pattern_list=[]


            for tokenDark in Darkpatterns:
                res = category_classifier.predict(category_vect.transform([tokenDark]))
                if res[0] not in unique_pattern_list:
                    unique_pattern_list.append(res[0])
                DarkpatternsClassification.append([tokenDark,res[0]])

            mark = split_strings(Darkpatterns)
            print(mark)
            final={
                  "list": unique_pattern_list,
                  "Darkpatterns": len_darkpatterns,
                  "score": Dark_Score(unique_pattern_list),
                  # Delete the below line if anything goes wrong 16:33 12-02-2024
                  "marking": mark
                  }
            return jsonify(final)
    except:
        print("Error in loading")
        return jsonify(final)
    finally:
        import databaseDP as ab
        ab.upload_data(url, DarkpatternsClassification, len_darkpatterns, unique_pattern_list,Dark_Score(unique_pattern_list))
        '''
        final={
            "list": ["Hi","there"],
            "Darkpatterns":10,
            "score":60,
            "highlightList":["the","in","Amazon.in"]
        }
        print(final)
        '''
        #return jsonify(final)
        print("done")

def Dark_Score(n):
    score=100
    for pattern in n:
        if pattern=='Scarcity' or pattern=='Urgency' or pattern=='Misdirection':
            score-=5
        elif pattern=='Obstruction'or pattern=='Sneaking':
            score-=15
        else:
            score-=20
    return(score)


import re

def split_strings(lst):
    # Define a pattern that matches any character that is NOT a number, alphabet, space, comma, hyphen, single quote, or double quote
    pattern = re.compile(r'[^\w\s,\-\'"\.]', re.UNICODE)

    split_list = []
    for string in lst:
        # Split the string using the pattern
        parts = re.split(pattern, string)
        # Filter out any empty strings that might result from the split operation
        parts_filtered = [part for part in parts if part]
        split_list.extend(parts_filtered)

    return split_list
if __name__ == '__main__':
    app.run(threaded=True, debug=True)

    #ab.upload_data(url, DarkpatternsClassification, len_darkpatterns, unique_pattern_list, Dark_Score(unique_pattern_list))
