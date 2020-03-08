import numpy as np

uniqueWord = {}
uniqueWordTag = {}
tagCount = {}

dataTraining = open("1_tagged_corpus.txt", "r")

for line in dataTraining:
    words = line.rstrip().split()
    for word in words:
        word = word.lower()
        if word not in uniqueWordTag.keys():
            uniqueWordTag[word] = 1
        else:
            uniqueWordTag[word] = uniqueWordTag[word] + 1
        wordSplit = word.split("/")
        token = wordSplit[0].lower()
        tag = wordSplit[1]
        if tag not in tagCount.keys():
            tagCount[tag] = 1
        else :
            tagCount[tag] = tagCount[tag] + 1

# print(tagCount)
print(uniqueWordTag)

dataTestList = []
dataTestWord = []

dataTest = open("data_test.txt", "r")
for sentence in dataTest:
    sentence = sentence.rstrip().split("\n")
    for word in sentence:
        word = word.lower()
        word = word.split()
        dataTestList.append(word)

print(dataTestList)
print(len(dataTestList))

for sentence in dataTestList:
    for word in sentence:
        for i in uniqueWordTag:
            if word in i:
                dataTestWord.append(uniqueWordTag[i])

print(dataTestWord)
print(len(dataTestWord))

# for x in uniqueWordTag:
#     if "ted" in x:
#         print(uniqueWordTag[x])
# print("")
# print(tagCount)

