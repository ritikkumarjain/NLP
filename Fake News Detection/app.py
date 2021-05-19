import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import spacy
nlp = spacy.load('en_core_web_sm')
import streamlit as st

import string 
import re
import nltk


st.set_page_config(page_title = "Fake News Detector")
page_bg_img = '''
<style>
body {
background-image: url("https://cdn.aarp.net/content/dam/aarp/politics/government-and-elections/2020/07/1140-fact-fake-blocks.jpg");
background-size: cover;
}
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

desc = "This web app detects fake news written in English.You can either enter the URL of a news article, or paste the text here(works better)."
subject = ['1) News',
          '2) Politics',
          '3) Left-News',
          '4) Government-News',
          '5) US_News',
          '6) Middle-East']
st.title("Fake News Detector")
st.markdown(desc)
st.subheader("Enter the text of a news article written in English from the following subject")
for i in subject:
    st.markdown(i)



df=pd.read_csv('df.csv')

df['cleaned_original']=df['text'].apply(lambda x:x.lower())


stopwords = spacy.lang.en.stop_words.STOP_WORDS
def remove_stopwords(text):
    return " ".join([word for word in str(text).split() if word not in stopwords])


PUNCT_TO_REMOVE = string.punctuation
def remove_punctuation(text):
    return text.translate(str.maketrans('', '', PUNCT_TO_REMOVE))

df['cleaned_original'] = df['cleaned_original'].apply(lambda x:remove_stopwords(x))
df['cleaned_original']= df['cleaned_original'].apply(lambda x: remove_punctuation(x))
df['cleaned_original'] = df['cleaned_original'].str.replace(r"[\"\,’]", '')


# maxlen = -1
# for doc in df['cleaned_original']:
#     tokens = nltk.word_tokenize(doc)
#     if(maxlen<len(tokens)):
#         maxlen = len(tokens)
# print("The maximum number of words in a title is =", maxlen) 

from sklearn.linear_model import LogisticRegression,PassiveAggressiveClassifier
from sklearn.metrics import roc_auc_score,confusion_matrix
from sklearn.feature_extraction.text import CountVectorizer,TfidfVectorizer
from sklearn.metrics import plot_confusion_matrix
from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(df['cleaned_original'], df.label, test_size = 0.2,random_state=10,stratify=df.label)
vec_train = CountVectorizer().fit(X_train)
X_vec_train = vec_train.transform(X_train)
X_vec_test = vec_train.transform(X_test)


model3 = LogisticRegression(C=3)
model3.fit(X_vec_train, y_train)
predicted_value3 = model3.predict(X_vec_test)
accuracy_value3 = roc_auc_score(y_test, predicted_value3)
#print(accuracy_value3)


#text = st.text_area('Input text/news headlines for detection') 
st.write('---')
# st.write('write text here')
text = st.text_area('Input text/news headlines for detection') 

text_new=text.lower()
    
text_new = remove_stopwords(text_new)
text_new = remove_punctuation(text_new)
#file['Cleaned_Text'] = file['Cleaned_Text'].str.replace(r"[\"\,’]:", '')
text_clean=[text_new]
    
text_clean = [text_new]
text_vec = vec_train.transform(text_clean)

preds = model3.predict(text_vec)

if st.button('Show Prediction'):
    if preds==1:
        st.markdown("<h1><span style='color:red'>❌ This is a fake news article!😡</span></h1>",
                     unsafe_allow_html=True)
    elif preds<0: 
        st.warning("Detection coming in negative.Invalid Input Given")
    elif preds==0:  
         st.markdown("<h1><span style='color:green'>✅ This is a real news article!👍</span></h1>",
                     unsafe_allow_html=True)
    else:
         st.warning("Something went wrong\nTry again")
    

# if st.button('Show Prediction'):
#     st.write('Showing')
#     st.write(answer)
st.write('---')
# if st.button('Is news Fake',key='predict'):
#     try: 
#         Model=model3
#         prediction=Model.predict(text_vec)
#         #sub['Preds']=prediction
            
#         #output = round(prediction[0],4)
#         if output<0:
#             st.warning("Detection coming in negative.Invalid Input Given")
#         else:
#             #st.success("The News detected is---> {}".format(predictions))
#             st.write(prediction)
#     except:
#         st.warning("Something went wrong\nTry again")
            
            
#print(prediction)            

























