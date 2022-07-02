from flask import Flask, render_template

app = Flask(__name__)
app.config.from_object('config')

@app.route("/")
def home():
    return "<h1>Hello World</h1>"