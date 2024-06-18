from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
      return ('Welcome to AI!')

@app.route('/hello')
def hello():
      return ('HELLO!')

@app.route('/welcome')
def welcome():
      return ('WELCOME!')

if __name__ == '__main__':
    app.run(debug = True)