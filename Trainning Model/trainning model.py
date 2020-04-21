import numpy as np
import re
import pickle 
import nltk
from nltk.corpus import stopwords
from sklearn.datasets import load_files
nltk.download('stopwords')

#importing the data 20 newsgroups
from sklearn.datasets import fetch_20newsgroups
dataset_train  = fetch_20newsgroups(subset='train') #only for trainning data and shuffle them

# dataset = load_files('txt/') 
# dataset_data = dataset.data
# dataset_target = dataset.target


#Use bag of words model 
from sklearn.feature_extraction.text import CountVectorizer
Vectorizer = CountVectorizer(max_features = 2000, min_df = 3, max_df = 0.4, stop_words = stopwords.words('english'))
Train_BOW = Vectorizer.fit_transform(dataset_train.data)
Train_BOW.shape


#TFIDF Model
from sklearn.feature_extraction.text import TfidfTransformer
transformer = TfidfTransformer()
Train_TFIDF = transformer.fit_transform(Train_BOW)
Train_TFIDF.shape


#Using Naive Bayes ML algorithm
#1.9.2 from https://scikit-learn.org/stable/modules/naive_bayes.html 
from sklearn.naive_bayes import MultinomialNB
classifier = MultinomialNB().fit(Train_TFIDF, dataset_train.target)

#for efficiency
from sklearn.pipeline import Pipeline
text_classifier = Pipeline([('vect', CountVectorizer()), ('tfidf', TfidfTransformer()), ('clf', MultinomialNB()), ])

text_classifier = text_classifier.fit(dataset_train.data, dataset_train.target)


dataset_test = fetch_20newsgroups(subset='test', shuffle=True)
predicted = text_classifier.predict(dataset_test.data)
np.mean(predicted == dataset_test.target)
