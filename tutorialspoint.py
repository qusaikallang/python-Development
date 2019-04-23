from bs4 import BeautifulSoup
import requests
from string_format import make
import time
title = []
def tutcrawl():
    k  = 0
    p = 5
    txt = []
    dta = []
    nxtlnk = ''
    nxtxt = ''
    r = requests.get("https://www.tutorialspoint.com/tutorialslibrary.htm")
    source_code = r.text
    soup = BeautifulSoup(source_code,'html.parser')
    for i in soup.find_all('a'):
        j = str(i)
        #print(i)
        if ('target="_blank"' not in j) and ('data-placement'not in j) and ('class' not in j):
            text = i.get_text('a')
            txt.append(text)
            half = i.get('href')
            dta.append('https://www.tutorialspoint.com'+str(half))

    while p >= 0:#removes not required indices from front
        dta.pop(p)
        txt.pop(p)
        p-=1

    #print(dta)
    #to get last index add [:-1]
    p = 0
    while p <= 16:#loop to remove unwanted index from back
        dta.pop(len(dta)-1)
        txt.pop(len(dta)-1)
        p+=1
    txt.pop(len(dta)-1)
    txt.append('Learn yaml')
    #print(len(txt))
    for i in range(0,len(txt)):# didnt use -1 becoz the stop int value of range will not include the last integer for example if stop int is 994 thn count will stop at 993
        print(i,txt[i])
    choice = int(input("Input your selected course please:\n>>"))
    r = requests.get(dta[choice])
    source = r.text
    soup = BeautifulSoup(source,'html.parser')
    file = open(txt[choice]+'.txt','w')
    for p in soup.find_all('p'):
        text = p.get_text('p')
        if '© Copyright 2018. All Rights Reserved.' not in text:
            s = text.split('.')
            m = '\n'.join(s)

            try:# protocol 1 writing m after encoding to utf-8 and decoding in cp1252 codec
                g = m.encode('utf-8').decode('cp1252')
                #print(g)
                file.writelines(g)
            except UnicodeDecodeError:# protocol 2 writing in simple string format
                print(make.BOLD+'error raised, switching to protocol 2'+make.END)
                file.writelines(m)
    for i in soup.find_all('pre', {'class': 'result notranslate'}):
        text = i.get_text('pre')
        file.writelines(text)
        #completed this loop with mehnat masshakkat
        # inomplete loop for getting specific conventions

    for i in soup.find_all("a"):
        if 'Next Page ' in i:
            nxtlnk = i.get('href')

    full = 'https://www.tutorialspoint.com' + nxtlnk
    while True:
        print(make.BOLD+make.BLUE+'>>Fetching your tutorial please wait'+make.END)
        file.writelines('\n')
        r = requests.get(full)
        plain = r.text
        soup = BeautifulSoup(plain,'html.parser')
        for p in soup.find_all('p'):
            text = p.get_text('p')
            if '© Copyright 2018. All Rights Reserved.' not in text:
                s = text.split('.')
                m = '\n'.join(s)
                if "You don't have permission to access" in m:
                    print(">>Blocked")



                try:  # protocol 1 writing m after encoding to utf-8 and decoding in cp1252 codec
                    g = m.encode('utf-8').decode('cp1252')
                    # print(g)
                    file.writelines(g)

                except UnicodeDecodeError:  # protocol 2 writing in simple string format
                    print(make.BOLD + 'error raised, switching to protocol 2' + make.END)
                    g = m.encode('utf-8')
                    file.writelines(str(g))
        for i in soup.find_all('pre', {'class': 'result notranslate'}):
            text = i.get_text('pre')
            file.writelines(text)
        for i in soup.find_all("a"):
            if 'Next Page ' in i:
                nxtlnk = i.get('href')
                nxtxt = str(nxtlnk)
        full = 'https://www.tutorialspoint.com' + nxtlnk
        if 'quick_guide.htm' in nxtxt:
            break





# class errors()
tutcrawl()
print(make.PURPLE+'Tutorial fetched succesfully'+make.END)
