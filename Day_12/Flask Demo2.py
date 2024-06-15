from flask import Flask
app = Flask(__name__)

@app.route('/<name>') 
def hello(name):
    return ("Hello %s" %name)

@app.route('/') 
def welcome():
    return ("This is Home Page.")

if __name__ == '__main__':
    app.run(debug = True)