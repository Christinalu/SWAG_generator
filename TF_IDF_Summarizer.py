import math
import nltk
import nltk.corpus
nltk.download('punkt')
import re
import matplotlib.pyplot as plt
import heapq
import operator
import itertools 
# pip install matplotlib, heapq

def word_frequency_list(text):

    stopword_list = nltk.corpus.stopwords.words('english')
    word_token = nltk.word_tokenize(text)
    ps = nltk.PorterStemmer()

    freq_list = {}
    
    for w in word_token:
        w = ps.stem(w)
        if w not in stopword_list:
            if w not in freq_list.keys():
                freq_list[w] = 1
            elif w in freq_list.keys():
                freq_list[w] = freq_list[w] + 1
            
    return freq_list

def word_freq_without_stem(text):

    stopword_list = nltk.corpus.stopwords.words('english')
    word_token = nltk.word_tokenize(text)

    freq_list_no_stem = {}
    
    for w in word_token:
        if w not in stopword_list:
            if w not in freq_list_no_stem.keys():
                freq_list_no_stem[w] = 1
            elif w in freq_list_no_stem.keys():
                freq_list_no_stem[w] = freq_list_no_stem[w] + 1
            
    return freq_list_no_stem

    


def word_frequency_matrix(sentToken):

    freq_matrix = {}
    stopword_list = nltk.corpus.stopwords.words('english')
    ps = nltk.PorterStemmer()

    for s in sentToken:
        
        freq_list = {}
        wordToken = nltk.word_tokenize(s)
        
        for w in wordToken:
            w = w.lower()
            w = ps.stem(w)
            if w not in stopword_list:
                if w in freq_list:
                    freq_list[w] = freq_list[w] + 1
                elif w not in freq_list:
                    freq_list[w] = 1

        freq_matrix[s[:20]] = freq_list

    return freq_matrix



def document_freq(freq_matrix):

    document_freq = {}

    for key, value in freq_matrix.items():
        for w, f in value.items():
            if w in document_freq:
                document_freq[w] = document_freq[w] + 1
            elif w not in document_freq:
                document_freq[w] = 1
    return document_freq


def tf_matrix(freqMatrix):

# tf = frequency / total word count in sentences

    tfMatrix = {}
    for key, value in freqMatrix.items():

        tf_list = {}

        total_count = len(value.keys())
        for w, count in value.items():
            tf_list[w] = count / total_count

        tfMatrix[key] = tf_list

    return tfMatrix

    
def idf_matrix(freqMatrix, documentFreq, docCount):

# log (total number of documents / word frequency in all documents)

    idfMatrix = {}

    for key, value in freqMatrix.items():
        idf_list = {}
        for w, f in value.items():
            idf_list[w] = math.log10(docCount / float(documentFreq[w]))
        idfMatrix[key] = idf_list

    return idfMatrix



def tf_idf(tf, idf):

# tf-idf = tf * idf

    tf_idf_matrix = {}

    for (k1, v1),(k2, v2) in zip(tf.items(), idf.items()):

        tf_idf_list = {}

        for (w1, tf_val), (w2, idf_val) in zip(v1.items(), v2.items()):
            tf_idf_list[w1] = float(tf_val) * float(idf_val)

        tf_idf_matrix[k1] = tf_idf_list

    return tf_idf_matrix


def sentence_score(tf_idf_matrix):
    sentence_score = {}

    for key, value in tf_idf_matrix.items():
        
        sent_score = 0

        for w, score in value.items():
            sent_score = sent_score + score

        sent_words_count = len(value.keys())

        sentence_score[key] = sent_score / sent_words_count

    return sentence_score


def get_threshold (sentence_score):

    sum = 0

    for s in sentence_score:
        sum = sum + sentence_score[s]

    sentence_count = len(sentence_score.keys())

    threshold = sum / sentence_count

    return threshold

def summarize(sent_token, score_matrix, threshold):

    sentence_count = 0
    summary = ""

    for s in sent_token:
        if s[:20] in s:
            if score_matrix[s[:20]] >= threshold:
                summary = summary + s + " "
                sentence_count = sentence_count + 1
    return summary


def super_summarizer_all_functions(text):

    sentences = nltk.sent_tokenize(text)
    doc_count = len(sentences)

    freq_matrix = word_frequency_matrix(sentences)

    doc_freq = document_freq(freq_matrix)

    tf_m = tf_matrix(freq_matrix)
    #print(tf_m)
    idf_m = idf_matrix(freq_matrix, doc_freq, doc_count)
    #print(idf_m)
    
    tf_idf_m = tf_idf(tf_m, idf_m)

    sent_score = sentence_score(tf_idf_m)

    threshold = get_threshold(sent_score)

    adjusted_threshold = 1.1 * threshold
    
    summarization = summarize(sentences, sent_score, adjusted_threshold)
    
    return summarization

def preprocess_data(text):
    text = re.sub(r'\[0-9]*\]',' ',text)
    text = re.sub(r'\s+', ' ', text)
    return text

def freq_histogram (text):

    freq_list = word_freq_without_stem(text)
    
    symbol = [',', '.','?',':',';','(',')']
    most_freq_words = {}
    sorted_d = dict(sorted(freq_list.items(), key=operator.itemgetter(1),reverse = True))

    for k, v in sorted_d.items():
        if k.lower() not in symbol:
            if k.lower() not in nltk.corpus.stopwords.words('english'):
                most_freq_words[k] = v
    
    most_five = dict(itertools.islice(most_freq_words.items(),10))
    plt.bar(most_five.keys(),most_five.values(), width = 0.8, color = 'skyblue',linewidth = 1.0)
    plt.title("Words Frequency Histogram", loc = 'center')
    plt.xlabel("Word")
    plt.ylabel("Frequency")
    plt.show()
    plt.close()
    
def main_function(test_text):
    textdata = preprocess_data(test_text)
    summarization = super_summarizer_all_functions(textdata)
    # print(summarization)
    freq_histogram (textdata)
    return summarization
    
