# Website printing Hello World
from flask import Flask,jsonify
app = Flask(__name__)

# flask module sytax to print hello world in the website
@app.route('/')
def hello_world():
    return "Hello World!"

# only applicable under this function
if __name__ == '__main__':
    app.run(debug=True)