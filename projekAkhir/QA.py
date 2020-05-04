import operator
from nltk.tag import CRFTagger
ct = CRFTagger()
ct.set_model_file('all_indo_man_tag_corpus_model.crf.tagger')

corpusFile = open("corpus.txt", encoding="utf8")

corpus = []
q = []
passage = {}

for sentences in corpusFile:
    corpus = sentences.split(". ")

# print(corpus)

# print()

# for sentence in corpus:
#     print(sentence)

print()

question = "Dimana kantor penguasa militer Jepang ?"
q = question.split(" ")

# print(q)

# print()

# for word in q:
#     print(word)

print()

for sentence in corpus:
    for word in q:
        if word in sentence:
            if sentence not in passage.keys():
                passage[sentence] = 1
            else:
                passage[sentence] += 1
            # print(word)
            # print(sentence)

print(q[0])

print()

for a in passage:
    print(a, " : ", passage[a])

# print(passage)

print()

ans = max(passage.items(), key = operator.itemgetter(1))[0]
print(ans)

taggedAns = []

a = ans.split(" ")
taggedAns.append(a)

print(taggedAns)

print()

tagged = ct.tag_sents(taggedAns)
print(tagged)