# -*- coding: utf-8 -*-
"""
Created on Wed Aug  3 16:51:03 2016

@author: Duwan_000
"""
import re
import requests
from bs4 import BeautifulSoup

# 10 total columns in ESPN roster data 
column_start = 1 # Instance for first column
column_end = 20 # Instance for last column 

url = "http://espn.go.com/mlb/stats/batting/_/qualified/true"
page = requests.get(url) #Downloads the HTML sourcecode from url 

# Sourcecode parsed by Beautiful Soup
soup = BeautifulSoup(page.content, "lxml") 

# Find the roster in HTML sourcecode ('tablehead')
right_table=soup.find("table", class_="tablehead")

#Creates lists for player data 
mlb_batting_data = []
temp_list =[]

# Uses a sexy Regular Expression to avoid scrapping repeat headers in ESPN data
for row in soup.find_all("tr", class_= re.compile("^o|^e")): 
    cells = row.findAll("td")
    for entry in range(column_start,column_end):   
                temp_list.append(cells[entry-1].find(text=True))

    mlb_batting_data.append(temp_list)
    temp_list = []
    
    
#import pandas to convert list of lists to data frame 
import pandas as pd
df=pd.DataFrame(mlb_batting_data)

df  

# Writes data frame to Microsoft Excel Sheet 
df.to_excel('espn_Batting_Data_Test.xlsx', sheet_name='sheet1', index=False)
    