from flask import Flask

'''
This is a simple Flask application that serves a static HTML page.
'''

### WSGI Application
### This is the entry point for the Flask application.
app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to flask course,This is a simple Flask application."

@app.route("/hello")
def hello():
    return "Hello, World!"

@app.route("/about")
def about():
    return "This is a simple Flask application that serves a static HTML page."

if __name__ == '__main__':
    app.run(debug=True)

