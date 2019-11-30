from bs4 import BeautifulSoup
import requests
import os
import re
import wget



# get image urls get_images()
# filter images for jpg and png only filter()
# download and save them in negative folder  download_images()
# create text file with paths
# regex for filtering  -> \.[pngjpg]{3}

# global declaration
#
src = []
proc_links = []

def get_images(search_term):
    url = 'https://pixabay.com/images/search/'+search_term+'/'
    if not os.path.exists('Neg'):
        os.makedirs('Neg')
    source_code = requests.get(url,headers={'User-Agent': 'Mozilla/5.0'})
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text,'html.parser')

    for div in soup.find_all('div',{'class':'item'}):
        link = div.find('img')
        src.append(link.get('src'))
    return src

def filter(src):
    pattern = '\.[pngjpg]{3}'
    for s in src:
        if not re.search(pattern,str(s)) is None:
            proc_links.append(str(s))
    return proc_links

def download_images(proc_links):

    pattern = '\.[pngjpg]{3}'
    pic = 1
    for links in proc_links:

        t = re.findall(pattern,links)

        try:
            wget.download(links,"/home/anonymous/PycharmProjects/Scripts/Neg/"+str(pic)+str(t))
        except Exception as e:
            print(str(e))
        pic = pic +1
        print(links)


term = input("Enter your search term for images\n>>")
data = get_images(term)
filered_data = filter(data)
download_images(filered_data)

