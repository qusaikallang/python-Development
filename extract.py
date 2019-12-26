import re
import pytesseract
from PIL import Image
import os


def extract():
    count = 0
    f = open('alidata.txt','a')
    li = []
    dir = os.path.dirname(__file__)
    imgs = 'DubaiDirectory/'
    dir2 = os.path.join(dir,imgs)
    emailpattern = '\s*[0-9a-z\.]+@[-a-z0-9.]*\.[a-z]+'
    c = 0
    for root,dirs,files in os.walk(imgs):
        for file in files:
            c = c + 1
            img_text =  pytesseract.image_to_string(dir2+file)
            r = re.findall(emailpattern,img_text)
            print("working with page->",c)
            for i in r:
                count +=1
                f.write(str(i)+"\n")

    print(count)
    f.close()


extract()
