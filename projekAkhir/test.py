import numpy as np
import re

file = open("corpus.txt", encoding="utf8")

corpus = []
question = []

pertanyaan1 = "kapan bom atom dijatuhkan ?"
pertanyaan2 = "kapan bom atom kedua dijatuhkan ?"
pertanyaan3 = "kapan Jepang secara resmi menyerah kepada Sekutu di kapal USS Missouri ?"
pertanyaan4 = "siapa mendatangi penguasa militer Jepang (Gunsei) untuk memperoleh konfirmasi di kantornya ?"

# ganti = {"kapan":"", "siapa":"", "dimana":"", "berapa":"", "?":""}
# tanya = pertanyaan.replace("kapan", "")
tanya = re.sub("[?]|kapan|siapa|dimana|berapa", "", pertanyaan4)
tanya = tanya.strip()
# print(tanya)

pertanyaan = pertanyaan4.split(" ")
question.append(pertanyaan)

print ("kata tanya : " + question[0][0])

# for word in question:
#     for a in word:
#         print(a)

for sentence in file:
    sentence = sentence.split(". ")
    corpus.append(sentence)

# for sentences in corpus:
#     for sentence in sentences:
#         for word in question:
#             for a in word:
#                 if a in sentence:
#                     print(sentence)
        # print(sentence)

# for sentences in corpus:
#     for sentence in sentences:
#         print(sentence)

# print(corpus)

print()

# for sentence in question:
#     for word in sentence:
#         print(word)

# for a in corpus:
#     for sentence in question:
#         for word in sentence:
#             if word in a:
#                 print(a)
#     break

print("passage :")

for a in corpus:
    for b in a:
        if tanya in b:
            print(b)

print()

if question[0][0] == "kapan":
    print("jawaban : waktu")
elif question[0][0] == "dimana":
    print("jawaban : tempat")
elif question[0][0] == "berapa":
    print("jawaban : jumlah")
elif question[0][0] == "siapa":
    print("jawaban : nama orang/organisasi")