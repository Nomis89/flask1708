from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    print("fasdf")
    return "<p>Hello, World!</p>"

@app.route("/tweede")
def bye_world():
    print("fasdf")
    return "<p>Bye, World!</p>"
