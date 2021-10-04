from selenium import webdriver as wd
from bs4 import BeautifulSoup as bou
import time
import requests
import pandas as pd

start_url = 'https://en.wikipedia.org/wiki/List_of_brightest_stars_and_other_record_stars'
page = requests.get(start_url)

soup = bou(page.text, 'html.parser')
start_table = soup.find('table')

templist = []

tablerows = start_table.find_all('tr')

for tr in tablerows:
    td = tr.find_all('td')
    row = [i.text.rstrip() for i in td]

    templist.append(row)
    
starnames =[]
distance =[]
mass =[] 
radius =[] 
lum = []

for i in range(1,len(templist)):

    starnames.append(templist[i][1])
    distance.append(templist[i][3])
    mass.append(templist[i][5])
    radius.append(templist[i][6])
    lum.append(templist[i][7])

df = pd.DataFrame((list(zip(starnames,distance,mass,radius,lum))),columns=['starnames','distance','mass','radius','lum'])
df.to_csv('stars.csv')
