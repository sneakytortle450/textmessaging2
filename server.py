from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/goodbye")
def goodbye_world():
    return "<p>Goodbye, World!</p>"

app.run(host='0.0.0.0', port=81,debug=True)