import re

def time(subs):
    time_cleaning = r'(\d{2}.\d{2}.\d{2}.\d{3})\s.*\s(\d{2}.\d{2}.\d{2}.\d{3})$'
    if re.search(time_cleaning, subs):
        return True
    return False

def tag(subs):
    tag_cleaning = r'<[^>]*>'
    if re.search(tag_cleaning, subs):
        return True
    return False

def pagenumber(subs):
    number_cleaning = r'^\d{1,4}$'
    if re.search(number_cleaning, subs):
        return True
    return False

def not_subs(subs):
    if time(subs):
        return True
    if tag(subs):
        return True
    if pagenumber(subs):
        return True
    return False

def cleaning_data(subs):
    after_cleaning = []
    subs = subs.split('\n')
    for line in subs:
        if not_subs(line) == False:
            after_cleaning.append(line)
    return after_cleaning

def main():
    subtitles = open('doc_3.srt','r').read()
    after_cleaning = cleaning_data(subtitles)

    # remove blank space and blank lines
    remove_blank = [i for i in after_cleaning if i[:-1]]

    file = open('c_subtitle.txt','w+')
    for data in remove_blank:
        file.write(data)
        file.write('\n')
    file.close()

main()
