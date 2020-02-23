from collections import Counter
import csv
import re

documentdata = open("doc_2.txt","r")
words = documentdata.read()

def casefolding(source):
    file = source.lower()
    return file

def punctuation(text):
    for ch in '!"#$%&()*+,-./:;<=>?@[\\]^_\'{|}~':
        text = text.replace(ch,"")
    return text

def removenumber(word):
    remove = re.sub(r'\d+','',word)
    return remove.split()

hasil_casefolding = casefolding(words)

hasil_punctuation = punctuation(hasil_casefolding)

tokenization = removenumber(hasil_punctuation)

def filtering(x):
    clean = []
    stopwords = open("id.stopwords.02.01.2016.txt", "r")
    stopwords_data = stopwords.read()

    for word in x:
        if word not in stopwords_data:
            clean.append(word)
    return clean

filtering_data = filtering(tokenization)

top_30_words = Counter(filtering_data).most_common(30)
with open('b_kataunik.txt', 'w') as f:
    csv.writer(f,delimiter=' ').writerows(top_30_words)
