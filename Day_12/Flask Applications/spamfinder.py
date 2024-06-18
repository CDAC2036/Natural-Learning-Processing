from tkinter import *
from flask import Flask, render_template, request
import joblib
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
app = Flask(__name__)

swords = stopwords.words('english')
ps = PorterStemmer()

def clean_text(sent):
    tokens = [ps.stem(word) for word in word_tokenize(sent) if word.lower() not in swords and word.isalnum()]
    return tokens

classifier = joblib.load('..\classifier.model')
tfidf = joblib.load('..\preprocessor.model')

@app.route('/')
def student():
    return render_template('SPAM_Detector.html')

@app.route('/spamfinder', methods= ['GET', 'POST'])
def result():
    if request.method == 'POST':
        data = dict(request.form)
        message = tfidf.transform([data['message']])
        data['result'] = classifier.predict(message[0])
        return render_template('spamoutput.html', data=data)
    
if __name__ == '__main__':
    app.run(debug=True)

# def check():
#     classifier = joblib.load('classifier.model')
#     tfidf = joblib.load('preprocessor.model')
#     message = str(t.get('1.0', END))
#     result = classifier.predict(tfidf.transform([message]))
#     l.config(text = f"Message is: " + str(result[0]))
#     l.place(x=300, y=550)

# Label(top, text='Enter the message').place(x=50, y=30)
# t = Text(top)
# t.place(x=50, y=70)

# Button(top, text='Check', command=check).place(x=300, y=500)

# l = Label(top, text='Message is...')
