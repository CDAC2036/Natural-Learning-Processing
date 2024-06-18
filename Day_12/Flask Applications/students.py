from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def student():
    return render_template('read_marks.html')

@app.route('/result', methods = ['POST','GET'])
def result():
    if request.method =='POST':
        phy = int(request.form['phy'])
        chem = int(request.form['chem'])
        math = int(request.form['math'])

        avg = (phy+chem+math)/3
        return render_template('result.html', result=avg)
    
if __name__ == '__main__':
    app.run(debug=True)