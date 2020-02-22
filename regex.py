import re
import json

fileOpen = open("tugas1.txt", "r")
text = fileOpen.read()

citations = re.split('\n\n', text)

class Citation:
    def __init__(self, title ,author, year):
        self.title = title
        self.author = author
        self.year = year

citations = re.split('\n\n',text)

citation_list = []
for citation in citations:
    # get year
    year  = re.findall('\(((?:19|20)[0-9][0-9])\)',citation)
    author_citation = re.split('[(](?:19|20)[0-9][0-9][)]',citation)

    # get author
    author = re.findall('[A-Z][a-z]{1,}[,]{0,1}\s[A-Z][a-z]{0,}[\.]{0,1}',author_citation[0])
    if len(author) == 0:
        author = re.findall('[A-Z][a-z]{1,}',author_citation[0])  
    if len(author) > 1 :
        poped_item = 0
        for index in range(len(author)) :
            if ',' not in author[index-poped_item] and '.' not in author[index-poped_item]:
                author.pop(index-poped_item)   
                poped_item +=1

    # get title
    title = re.findall('\".*\"', citation)
    if len(title) == 0 :
        if len(author) ==0 :
            title = re.findall('^[A-Za-z,]{1,}[ ][A-Za-z, ]{0,}',author_citation[0])
        else:
            title = re.split(author[-1], citation)[1]
            if ').' not in title :
                title = re.findall('[A-Za-z,]{1,}[ ][A-Za-z, ]{0,}[\.]',title)
            else : 
                title = title.split(').')[1]
                title = re.findall('[A-Za-z,]{1,}[ ][A-Za-z,: ]{0,}',title)          
                title = title[0]
    else:
        title = title[0][1:-1]     

    # Creat Citation
    citation_list.append(Citation(title, author, year))
citationFormat = []
cit = []
for citation in citation_list:
    nama = '; '.join(citation.author)
    judul = ''.join(citation.title)
    tahun = ''.join(citation.year)
    if len(nama)==0:
        if len(tahun)==0:
            print(f'title : {judul}')
            citationFormat.append("title : "+judul)
            cit.append(citationFormat)
        elif len(judul)==0:
            print(f'year : {tahun}')
            citationFormat.append("year : "+tahun)
            cit.append(citationFormat)
        else:
            print(f'year : {tahun}\ntitle : {judul}')
            citationFormat.append("year : "+tahun)
            citationFormat.append("title : "+judul)
            cit.append(citationFormat)
    elif len(tahun)==0:
        if len(judul)==0:
            print(f'authors : {nama}')
            citationFormat.append("author : "+nama)
            cit.append(citationFormat)
        else:
            print(f'authors : {nama}\ntitle : {judul}')
            citationFormat.append("title : "+judul)
            citationFormat.append("author : "+nama)
            cit.append(citationFormat)
    elif len(judul)==0:
        print(f'authors : {nama}\nyear : {tahun}')
        citationFormat.append("year : "+tahun)
        citationFormat.append("author : "+nama)
        cit.append(citationFormat)
    else:
        print(f'authors : {nama}\nyear : {tahun}\ntitle : {judul}')
        citationFormat.append("year : "+tahun)
        citationFormat.append("title : "+judul)
        citationFormat.append("author : "+nama)
        cit.append(citationFormat)
    print()
    # cit.append(citationFormat)
    # citationFormat.append("year : "+tahun)
    # citationFormat.append("title : "+judul)
    # citationFormat.append("author : "+nama)
    # cit.append(citationFormat)

# for a in citationFormat:
#     print(a)

# print(cit)