import random
import nltk

#
# N-grams

text = """A false negative error, or in short a false negative, is a
test result that indicates that a condition does not hold,
while in fact it does. In other words, erroneously, no effect has been inferred.
An example for a false negative is a test indicating that a woman is not pregnant whereas she is actually pregnant."""

n=5
ngrams = {}

words = nltk.word_tokenize(text)
for i in range(len(words)-n):
    gram = ' '.join (words[i:i+n])
    if gram not in ngrams.keys():
        ngrams[gram] = []
    ngrams[gram].append(words[i+n])

#give the prediction of the next word

currentGram = ' '.join(words[0:n])
result = currentGram
for i in range(40):
    if currentGram not in ngrams.keys():
        break
    possibilities = ngrams[currentGram]
    nextItem = possibilities[random.randrange(len(possibilities))]
    result += ' '+ nextItem
    rwords = nltk.word_tokenize(result)
    currentGram = ' '.join(rwords[len(rwords)-n:len(rwords)])

print(result) 
