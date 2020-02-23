import re
import json

fileOpen = open("doc_1.txt", "r")
text = fileOpen.read()

class Citation:
    def __init__(self, title ,author, year):
        self.title = title
        self.author = author
        self.year = year

citations = re.split('\n\n',text)

citationList = []
for citation in citations:
    # get year
    year  = re.findall('\((?:19|20)[0-9][0-9]\)',citation)
    authorCitation = re.split('\((?:19|20)[0-9][0-9]\)',citation)
    if len(year) == 0:
        authorCitation = re.split('[12]\d{3}',citation)  
    else:
        year = year[0][1:-1]

    # get author
    author = re.findall('[A-Z][A-Z|a-z]+\,?\s[A-Z][a-z]*\s[A-Z][a-z]*\.?|[A-Z][a-z]+\,?\s[A-Z][a-z]*\.?|^[A-Z][a-z]+',authorCitation[0]) 
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
            title = re.findall('[A-Za-z,]{1,}\s[A-Za-z, ]{0,}',authorCitation[0])[0]     
        else:
            title = re.split(author[0], citation)[1]
            if ').' not in title :
                title = re.findall('[A-Za-z,]{1,}\s[A-Za-z, ]{0,}[\.]',title)
                title = title[0]
            else : 
                title = title.split(').')[1]
                title = re.findall('[A-Za-z,]{1,}\s[A-Za-z,: ]{0,}[\.(]',title)          
                title = title[0]
    else:
        title = title[0][1:-1]     
  
    # Creat Citation
    citationList.append(Citation(title, author, year))

#dictionary
dict = []
for citation in citationList:
    if len(citation.year)>1:
        dict.append(
            {
                "authors": '; '.join(citation.author),
                "title": citation.title,
                "year": citation.year
            }
        )
    elif len(citation.year)==0 and len(citation.author)==0:
        dict.append(
            {
                "title": citation.title
            }
        )
    elif len(citation.year)==0:
        dict.append(
            {
                "authors": '; '.join(citation.author),
                "title": citation.title
            }
        )

with open('a_judul.json', 'w') as f:
    json.dump(dict, f)