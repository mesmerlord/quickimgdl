import PIL
from PIL import Image as img
import cloudscraper
import csv
import shutil
from django.utils.text import slugify
from concurrent.futures import ThreadPoolExecutor
import concurrent.futures

newscrape = cloudscraper.create_scraper()
imagelist = []
fileName = []

with open('newfile3.csv', 'r', encoding='utf-8') as imagefile:
    reader = csv.reader(imagefile)
    next(reader,None)
    for line in reader:
        imagelist.append(line[4])
        fileName.append(line[2])

def downloadImg(url, filename):
    connect = newscrape.get(url)
    if(connect.status_code==200):
        imageFile = connect.content
        with open(file = (f'Images/{slugify(filename)}.jpg'), mode='wb') as newfile:
            newfile.write(imageFile)
    else:
        print(url)

with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
    executor.map(downloadImg, imagelist,fileName)


