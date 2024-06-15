from flask import Flask
app = Flask(__name__)

@app.route('/') # Decorator
def hello_world():
    return ("Welcome to Flask Application")

@app.route('/hello') 
def hello():
    return ("Hello World!")

@app.route('/welcome') 
def welcome():
    return ("This is Welcome Page.")

if __name__ == '__main__':
    app.run(debug = True)