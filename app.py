from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "<h1>Bozkurt97 - Intigriti, subdomain takeover!<script>confirm(9)></script>.."
