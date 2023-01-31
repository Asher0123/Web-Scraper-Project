import requests
import datetime
import time 
import pandas as pd
from bs4 import BeautifulSoup
import csv

URL='https://www.amazon.in/DUDEME-Sleeve-Cotton-Programmer-Developer/dp/B08FMVZNFB/ref=sr_1_13?crid=2CI3OK3IBCQXW&keywords=data%2Banalytics%2Bt%2Bshirt&qid=1675015464&s=apparel&sprefix=data%2Banalytics%2Bt%2Bshi%2Cfashion%2C350&sr=1-13&th=1&psc=1'
header={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"}
page=requests.get(URL,headers=header)
soup1=BeautifulSoup(page.content,"html.parser")
soup2=BeautifulSoup(soup1.prettify(),"html.parser")
title=soup2.find(id='productTitle').get_text()
price=soup2.find(class_='a-price-whole').get_text()
print(title,price)

price=price.strip()[0:3]
title=title.strip()
today=datetime.date.today()

print(title,price,today)

header=['Title','Price','Date']
data=[title,price,today]
'''
with open('WebScrapingProject.csv','w',newline='',encoding='UTF8') as f:
  writer=csv.writer(f)
  writer.writerow(header)
  writer.writerow(data)
'''

#We are now appending the data
with open('WebScrapingProject.csv','a+',newline='',encoding='UTF8') as f:
  writer=csv.writer(f)
  writer.writerow(data)

df=pd.read_csv('/content/WebScrapingProject.csv')
df

#Using function to Automate the process 
def check_price():
  URL='https://www.amazon.in/DUDEME-Sleeve-Cotton-Programmer-Developer/dp/B08FMVZNFB/ref=sr_1_13?crid=2CI3OK3IBCQXW&keywords=data%2Banalytics%2Bt%2Bshirt&qid=1675015464&s=apparel&sprefix=data%2Banalytics%2Bt%2Bshi%2Cfashion%2C350&sr=1-13&th=1&psc=1'
  header={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36"}
  page=requests.get(URL,headers=header)
  soup1=BeautifulSoup(page.content,"html.parser")
  soup2=BeautifulSoup(soup1.prettify(),"html.parser")
  title=soup2.find(id='productTitle').get_text()
  price=soup2.find(class_='a-price-whole').get_text()
  price=price.strip()[0:3]
  title=title.strip()
  today=datetime.date.today()
  header=['Title','Price','Date']
  data=[title,price,today]
  with open('WebScrapingProject.csv','a+',newline='',encoding='UTF8') as f:
    writer=csv.writer(f)
    writer.writerow(data)

while(True):
  check_price()
  time.sleep(86400)