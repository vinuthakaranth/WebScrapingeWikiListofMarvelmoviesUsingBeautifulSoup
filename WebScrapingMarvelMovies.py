# -*- coding: utf-8 -*-
"""
Created on Fri Apr  6 23:43:10 2018

@author: vinutha karanth
"""

#import relevant libraries
import wordcloud
import matplotlib
import bs4
import csv
import pandas
import numpy as np
from collections import Counter
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
from matplotlib import pyplot as plt
from wordcloud import WordCloud
from PIL import Image

#open connection, grab page
my_url = 'https://en.wikipedia.org/wiki/List_of_Marvel_Cinematic_Universe_films'
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

#open csv file for writing
file_name = "MarvelBoxOffice2.csv"
f = open(file_name,"w")

#write headers to csv
headers = "Film, US Release date, Worldwide Gross, Worldwide Ranking\n"
f.write(headers)

# html parser
page_soup = soup(page_html,"html.parser")

table = page_soup.findAll("table", {"class":"wikitable"}) 
BoxOfficetable = table[4]

table_row = BoxOfficetable.findAll("tr") 
for row in table_row[2:len(table_row)-1]:    
    row_info = row.findAll("td")
    Film = row_info[0].text
    USReleasedate = row_info[1].text
    WorldwideGross = row_info[4].text
    WorldwideRanking = row_info[6].text
    f.write(Film.replace(",", "|").replace("\n","") + "," + USReleasedate.replace(",", "|") + "," + WorldwideGross.replace(",", "|") + "," + WorldwideRanking.replace(",", "|").replace("\n","") + "\n")
    
f.close() 

        
        
moviedata=pandas.read_csv("MarvelBoxOffice2.csv")
moviedata_group = moviedata.groupby('Film')
moviedata_totals = moviedata_group.sum()
my_plot = moviedata_totals.plot(kind='bar')
