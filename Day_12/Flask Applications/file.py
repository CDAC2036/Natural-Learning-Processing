from flask import Flask, render_template
app = Flask(__name__)

@app.route('/<user>')
def index(user):
    return render_template('BasicWeb.html', name=user)

if __name__ == '__main__':
    app.run(debug=True)