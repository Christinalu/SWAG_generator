#Referenced the Naive Bayes ML algorithm and pipeline method from the Internet

#Naive Bayes algorithm
from sklearn.naive_bayes import MultinomialNB
clf = MultinomialNB().fit(X_train_tfidf, twenty_train.target)

#pipeline method
from sklearn.pipeline import Pipeline
text_clf = Pipeline([('vect', CountVectorizer()), ('tfidf', TfidfTransformer()), ('clf', MultinomialNB()),])
text_clf = text_clf.fit(twenty_train.data, twenty_train.target)

