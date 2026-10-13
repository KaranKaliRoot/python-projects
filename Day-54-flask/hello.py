from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return '<h1 style="text-align: center">みんな　こんにちわ!</h1>'

@app.route("/bye")
def bye():
    return "<h1>さよなら！</h1>"

@app.route("/<name>")
def greet(name):
    return f"<h1>Hello {name}!</h1>"



if __name__ == "__main__":
    app.run(debug=True)

