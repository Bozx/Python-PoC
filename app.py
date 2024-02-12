from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Bozkurt97 - Intigriti, subdomain takeover!"
