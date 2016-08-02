# Alexander Singleton
#Beautiful_ESPN_Scraper
#
#Dependencies: requests.py, BeautifulSoup.py, pandas.py

#########################################################################

import requests
from bs4 import BeautifulSoup

# 10 total columns in ESPN roster data 
column_start = 1 # Instance for first column
column_end = 11 # Instance for last column 

# Create url for each team on ESPN
prefix = "http://espn.go.com/mlb/team/roster/_/name/"
#team_Abbrev = mlb_Teams_Abbrev[i] #need to construct this list 
sort = "sort/weight/" #See Readme: Sorting by weight simplifies web-scraping
#team_Name = mlb_Teams[i] #need to construct this list

# url = prefix + team_Abbrev + sort + team_Name

url = "http://espn.go.com/mlb/team/roster/_/name/ari/sort/weight/arizona-diamondbacks"
page = requests.get(url) #Downloads the HTML sourcecode from url 

# Sourcecode parsed by Beautiful Soup
soup = BeautifulSoup(page.content) 

# Find the roster in HTML sourcecode ('tablehead')
right_table=soup.find("table", class_="tablehead")

#Creates lists for player data 
mlb_data = []
temp_list =[]

# Extract table (roster) data by row and fills list of lists 
for row in right_table.findAll("tr"):
    cells = row.findAll("td")
    if len(cells)==(column_end-column_start):  
           for entry in range(column_start,column_end):   
                temp_list.append(cells[entry-1].find(text=True))

    mlb_data.append(temp_list)
    temp_list = []


#import pandas to convert list of lists to data frame 
import pandas as pd
df=pd.DataFrame(mlb_data)

# Writes data frame to Microsoft Excel Sheet 
df.to_excel('test_Spy_2.xlsx', sheet_name='sheet1', index=False)
