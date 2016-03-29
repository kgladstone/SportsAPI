#***************************************************************
# Princeton Sports Analytics
# player_weights.R
#
# Authors: Keith Gladstone and Ben Ulene
# April 2016
#
# Analysis of how player weights affect hitting performance
#
#***************************************************************
library(RCurl)

#######################
# Function: player_weight
# Parameter: MLB player Fangraphs ID
# Return: the player weight
#######################
player_weight <- function(id) {
  url = paste("http://www.fangraphs.com/statss.aspx?playerid=", id, sep="")
  options(RCurlOptions = list(verbose = FALSE,
                              followlocation = TRUE,
                              autoreferer = TRUE,
                              nosignal = TRUE))
  page = getURL(url)
  
  st = regexpr("Height/Weight", page)[[1]] + 23
  str = substr(page, st, st + 10)
  
  st = regexpr("/", str)[[1]] + 1
  end = regexpr(" &", str)[[1]] - 1
  wt = as.numeric(substr(str, st, end))
  return(wt)
}

##########################################
# Read in a file of player IDs
##########################################
setwd("~/Desktop/Player_Weights_Project")
data <- read.csv("PID-and-Position.csv", header=TRUE, stringsAsFactors = FALSE)
players <- data 

# Iterate through list of player IDs
wt = rep(0, nrow(players))
for (row in 1:nrow(players)) {
  print(row)
  id = players[row,][1]
  wt[row] = player_weight(id)
}

df = cbind(players, wt)
write.csv(df, "player_weights.csv")
View(df)