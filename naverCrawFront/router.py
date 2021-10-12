from flask import Flask
from flask.templating import render_template
import requests


app = Flask(__name__)

@app.route("/news")
def index():
    

    return render_template("index.html")


if __name__ == "__main__" :
    app.run(debug=True, port=5000)