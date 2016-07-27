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
right_table=soup.find('table', class_='tablehead')

# (Would like to automate the assignment of the empty list arrays via a loop...)
# for i in range(column_start,column_end):
# 	"V"+ str(i) = []
# However, python doesn't like me assigning a "String" as a variable 

# Creates empty lists for each column of roster data 
V1, V2, V3, V4, V5, V6, V7, V8, V9, V10 = [],[],[],[],[],[],[],[],[],[]

# Extract table (roster) data by row
for row in right_table.findAll("tr"):
    cells = row.findAll('td')
    if len(cells)==(column_start-column_end):  
       
       #Fill lists with Roster data  
        V1.append(cells[0].find(text=True))
        V2.append(cells[1].find(text=True)) #Name column
        V3.append(cells[2].find(text=True))
        V4.append(cells[3].find(text=True))
        V5.append(cells[4].find(text=True))
        V6.append(cells[5].find(text=True))
        V7.append(cells[6].find(text=True))
        V8.append(cells[7].find(text=True))
        V9.append(cells[8].find(text=True)) #Weight Column 
        V10.append(cells[9].find(text=True))

        # Prototype Code for handling the above rather messy assignments:  
        # for i in range(column_start,column_end):
    	#  a = "V"+ str(i)
    	#  a.append(cells[i-1].find(text=True))

#import pandas to convert list to data frame, then c-bind all columns 
import pandas as pd
df=pd.DataFrame(V1,columns=['V1'])
df['V2']=V2
df['V3']=V3
df['V4']=V4
df['V5']=V5
df['V6']=V6
df['V7']=V7
df['V8']=V8
df['V9']=V9
df['V10']=V10

# Prototype Code: 
# for i in range(column_start+1,11): 
# 	name_of_list = 'V'+ str(i)
#     df[name_of_list] = name_of_list

#df  

# Writes data frame to Microsoft Excel Sheet 
df.to_excel('test_Spy.xlsx', sheet_name='sheet1', index=False)