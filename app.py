from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Bozkurt97 - HG_Real @ Intigriti, subdomain takeover!<img src=x onerror=confirm(9)>..."
