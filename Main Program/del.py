from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    print("here")
    if request.method == 'POST':
        url = (list((request.json).values()))
        print("New port",url)


if __name__ == '__main__':
    app.run(port=8000,threaded=True, debug=True)