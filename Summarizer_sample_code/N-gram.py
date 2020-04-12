# N-grams Modelling

import random

text = """Global warming or climate change has become a worldwide concern."""

n = 3

ngrams = {}

#Create the n-grams
for i in range(len(text)-n):
    gram = text[i:i+n] # text[0:3] = Glo
    if gram not in ngrams.keys():
        ngrams[gram] = []
    ngrams[gram].append(text[i+n]) #text[0+3] = text[3] = b

#Testing our N-Gram model

currentGram = text[0:n]
result = currentGram
for i in range(100):
    if currentGram not in ngrams.keys():
        break
    possibilities = ngrams[currentGram]
    nextItem = possibilities[random.randrange(len(possibilities))]
    result += nextItem
    currentGram = result[len(result) - n:len(result)]

print(result)
