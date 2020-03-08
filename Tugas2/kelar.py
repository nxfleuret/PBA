dataTrain = open("1_tagged_corpus.txt", "r")

uniqueTaggedWord = {}
tagCount = {}
wordCount = {}
dataTestList = []
dataTaggedList = []
tokenCount = []

for line in dataTrain:
    words = line.split()
    for word in words:
        word = word.lower()
        if word not in uniqueTaggedWord.keys():
            uniqueTaggedWord[word] = 1
        else:
            uniqueTaggedWord[word] = uniqueTaggedWord[word] + 1
        wordSplit = word.split("/")
        
        token = wordSplit[0]
        if token not in wordCount.keys():
            wordCount[token] = 1
        else:
            wordCount[token] = wordCount[token] + 1

        tag = wordSplit[1]
        if tag not in tagCount.keys():
            tagCount[tag] = 1
        else:
            tagCount[tag] = tagCount[tag] + 1

dataTest = open("data_test.txt", "r")
for sentence in dataTest:
    sentence = sentence.rstrip().split("\n")
    for word in sentence:
        word = word.lower()
        word = word.split()
        dataTestList.append(word)

dataTests = []
dataTest2 = open("data_test.txt", "r")

for sentence in dataTest2:
    sentence = sentence.rstrip().split("\n")
    for word in sentence:
        word = word.lower()
        dataTests.append(word)

for words in dataTestList:
    for word in words:
        for i in uniqueTaggedWord:
            temp = i.split("/")
            if temp[0] == word:
                dataTaggedList.append(i)

dataTaggedLists = []
for words in dataTests:
    words = words.split()
    for word in words:
        dataTaggedLists.append(word)

totalTag = sum(tagCount.values())

bayes = {}
tagResult = {}

for words in dataTaggedList:
    word = words.split("/")
    res = uniqueTaggedWord[words]/wordCount[word[0]]*tagCount[word[1]]/totalTag

    if uniqueTaggedWord[words] == wordCount[word[0]]:
        bayes[word[0]] = res
        tagResult[word[0]] = word[1]

    else:
        bayes[word[0]] = res
        tagResult[word[0]] = word[1]
        if bayes[word[0]] < res:
            bayes[word[0]] = res
            tagResult[word[0]] = word[1]
        else:
            bayes[word[0]] = res
            tagResult[word[0]] = word[1]

posTagResult = []

for tagWord in dataTaggedLists:
    posTagResult.append(tagWord + "/" + tagResult[tagWord])

print("Hasil pos tagging dengan unigram tagging")
print(posTagResult)

groundTruth = []

dataGroundTruth = open("ground_truth.txt", "r")

for data in dataGroundTruth:
    data = data.split()
    groundTruth.append(data)

counter = 0
print("\nTag yang tidak sesuai dengan ground truth")
for count, data in enumerate(posTagResult):
    if posTagResult[count] == groundTruth[0][count].lower():
        counter += 1
    else:
        print(data)

accuracy = counter/len(groundTruth[0])
print("\nAkurasi")
print(accuracy)
