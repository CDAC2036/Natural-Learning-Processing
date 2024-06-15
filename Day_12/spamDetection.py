import joblib
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
from flask import Flask,render_template,request
app=Flask(__name__)
swords = stopwords.words('english')
ps = PorterStemmer()

# It is rquired as tfidf needs clean text function bcz tfidf = TfidfVectorizer(analyzer=clean_text) and tfidf is used for preprocessor.model
def clean_text(sent):
    tokens = [ps.stem(word) for word in word_tokenize(sent) if word.lower() not in swords and word.isalnum()]
    return tokens


classifier = joblib.load('classifier.model')
tfidf = joblib.load('preprocessor.model')
 
@app.route('/')
def student():
    return render_template('spamdetector.html')

@app.route('/spamfinder',methods=['POST','GET'])
def result():
    if request.method=='POST':
        data=dict(request.form)
        messege=tfidf.transform([data['messege']])
        data['result']=classifier.predict(messege)[0]
        return render_template('spamoutput.html',data=data)
    
if __name__=='__main__':
    app.run(debug=True)
    

