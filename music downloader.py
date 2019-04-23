from bs4 import BeautifulSoup
import requests
import wget
import os

try:
        os.mkdir('C:\\Users\qusai\OneDrive\Desktop\songs')
        print('Directory created')
except FileExistsError :
        print('Directory exists,Continuing')

p = input('Which page you wanna view for movies to download songs'+'\n'+'>>')
url = "https://www.songsmp3.org/1/bollywood-music.html?page=" + p
def song(url):
        #module0
        r = requests.get(url)
        source_code = r.text
        soup = BeautifulSoup(source_code,"html.parser")
        urlname = open('urlname.txt','w')
        i = 0
        for link in soup.find_all('li'and'a'):
            s = str(link)
            if "img" and 'class="movie"' in s:
                href = link.get('href')
                urlname.write("https://www.songsmp3.org"+str(href)+'\n')
        urlname.close()
        for link in soup.find_all('li'and 'img'):
                s = str(link)
                alt = link.get('alt')
                if 'img' and 'class="movie"' in s:
                        print(i, alt)
                        i+=1
        uchoice = input('choose the movie whose songs you wanna download'+'\n'+'>>')
        m = open('urlname.txt','r')
        line = m.readlines()
        url1 = line[int(uchoice)].strip()
        m.close()
        #mmodule 2
        f = open('urlname.txt','w')
        r = requests.get(url1)
        source_code = r.text
        soup = BeautifulSoup(source_code,'html.parser')
        for link in soup.find_all('a'):
                s = str(link)
                if 'class="link"' in s:
                        href = link.get('href')
                        f.write('https://www.songsmp3.org'+href+'\n')
        f.close()
        i = 0
        j = open('names.txt','w')
        for link in soup.find_all('div',{'class':'link'}):
                text = link.get_text('div')
                j.write(text+'\n')
                print(i,text)
                i+=1
        j.close()
        j = open('names.txt','r')
        g = j.readlines()
        f = open('urlname.txt','r')
        uchoice = input("choose the song you want to download"+'\n'+'>>')
        filename = g[int(uchoice)].strip()
        j.close()
        line = f.readlines()
        url1 = line[int(uchoice)].strip()
        f.close()
        #module 3
        f = open('urlname.txt','w')
        r = requests.get(url1)
        source_code = r.text
        soup = BeautifulSoup(source_code,'html.parser')
        for link in soup.find_all('a',{'class':'dowbutzip'}):
                href = link.get('href')
                f.write(href+'\n')
        f.close()
        print('0 -> Download in 128kbps')
        print('1 -> Download in 320kbps')
        f = open('urlname.txt','r')
        line = f.readlines()
        uchoice = input('your choice'+'>>')
        url1 = line[int(uchoice)].strip()
        f.close()
        output = 'C:\\Users\qusai\OneDrive\Desktop\songs\\'+filename+'.mp3'
        print('Downloading....')
        song = wget.download(url1,out=output)
        print('Download complete....')

song(url)
