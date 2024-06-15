from flask import Flask,request,redirect,url_for,render_template

app=Flask(__name__)
@app.route('/')
def index():
    return render_template('a1.html')

@app.route('/success/<name>')
def success(name):
    return 'Welcome %s!' %name

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='POST':
        user=request.form['nm']
        return redirect(url_for('success',name=user))
    return 'hi'
    
if __name__=='__main__':
    app.run(debug=True)
