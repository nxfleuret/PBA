import re

fileOpen = open("tugas1.txt", "r")
text = fileOpen.read()

citations = re.split('\n\n', text)

citationList = []
for citation in citations:

    #get year
    year = re.findall('[(](?:19|20)[0-9][0-9][)]', citation)
    authorCitation = re.split('[(](?:19|20)[0-9][0-9][)]', citation)
    year = year[0][1:-1]

    #get author
    author = re.findall("[A-Z][a-z'`-]*, [A-Za-z]*|^[A-Z][a-z'`-]* [A-Z][a-z'`-]*", authorCitation)
    if len(author) > 1:
        authors = 0
        for i in range (len(author)):
            if ',' not in author[i-authors] and '.' not in author[i-authors]:
                author.pop(i-authors)
                authors += 1
    
    #gget title
    title = re.findall('\".*\"', citation)
    if len(title) == 0:
        if len(author) == 0:
            title = re.findall('[A-Za-z,]{1,}[ ][A-Za-z, ]{0,}',authorCitation[0])[0]
        else:
            title = re.split(author[-1], citation)[1]
            if ').' not in title:
                title = re.findall('[A-Za-z,]{1,}[ ][A-Za-z, ]{0,}[\.]',title)[0]
            
            else:
                title = title.split(').')[1]
                title = re.findall('[A-Za-z,]{1,}[ ][A-Za-z,: ]{0,}[\.(]',title)
                title = title[0]
    else:
        title = title[0][1:-1]

    citationList.append(title)
    citationList.append(author)
    citationList.append(year)

for citation in citationList:
    print(f'title : {title}, author : {author}, year : {year}')