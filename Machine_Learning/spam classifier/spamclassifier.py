import nltk
from nltk.corpus import stopwords
import string
import streamlit as st
import pickle
from nltk.stem.porter import PorterStemmer

ps = PorterStemmer()
def transform_text(text):
  text = text.lower()
  text = nltk.word_tokenize(text)
  ans = []
  for i in text:
    if  i.isalnum():
      ans.append(i)
  # text = ''.join(ans)
  text = ans[:]
  ans.clear()
  for i in text:
    if i not in stopwords.words('english') and i not in string.punctuation:
      ans.append(i)
  # text = ''.join(ans)
  text = ans[:]
  ans.clear()
  for i in text:
    ans.append(ps.stem(i))
  return ' '.join(ans)

countvectorizer = pickle.load(open('CountVectorizer.pkl','rb'))
model = pickle.load(open('BernoulliNaiveBayes .pkl','rb'))

st.title('Spam Classifier')
sentence = st.text_input('Enter Text')

if st.button('Predict'):
    sentence = countvectorizer.transform([transform_text(sentence)])
    result = model.predict(sentence)[0]
    if result == 1:
        st.header('Spam')

    else:
        st.header('Not Spam')

