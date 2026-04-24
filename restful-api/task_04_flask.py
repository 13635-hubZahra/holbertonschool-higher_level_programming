from flask import Flask, jsonify, request

app = Flask(__name__)
users = {}
@app.route("/")
def home():
    ...
@app.route("/status")
def status():
    ...
@app.route("/data")
def data():
    ...
@app.route("/users/<username>")
def get_user(username):
    ...
@app.route("/add_user", methods=["POST"])
def add_user():
    ...
if __name__ == "__main__":
    app.run()
