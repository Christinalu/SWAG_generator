import bs4 as bs
import urllib.request
import re
import nltk
nltk.download('stopwords')
import heapq

def main_func(text):
    # Fetch the article
    # for paragraph in soup.find_all('p'):
    #     text += paragraph.text

    # Preprocessing the data
    text = re.sub(r'\[[0-9]*\]',' ',text)
    text = re.sub(r'\s+',' ',text)
    article = text.lower()
    article = re.sub(r'\W',' ',article)
    article = re.sub(r'\d',' ',article)
    article = re.sub(r'\s+',' ',article)

    # Tokenize sentences
    token_sen = nltk.sent_tokenize(text)

    # Stopword list
    stop_words = nltk.corpus.stopwords.words('english')

    # Word counts 
    count = {}
    for word in nltk.word_tokenize(article):
        if word not in stop_words:
            if word not in count.keys():
                count[word] = 1
            else:
                count[word] += 1

    # Converting counts to weights
    max_count = max(count.values())
    for key in count.keys():
        count[key] = count[key]/max_count
        
    # Product sentence scores    
    score = {}
    for sentence in token_sen:
        for word in nltk.word_tokenize(sentence.lower()):
            if word in count.keys():
                if len(sentence.split(' ')) < 25: #length of each sentence of summary
                    if sentence not in score.keys():
                        score[sentence] = count[word]
                    else:
                        score[sentence] += count[word]
                        
    # Gettings best 5 lines             
    best_sentences = heapq.nlargest(5, score, key=score.get)

    print('-------------------------------------------------------')

    best = ""
    for sentence in best_sentences:
        best += sentence + ' '
    # print(best)
    return best