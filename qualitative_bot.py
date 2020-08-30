import os, random
import csv
import bs4
import requests
import urllib
from bs4 import BeautifulSoup
import pandas as pd



dir1 = r"C:\Users\MrKap\Projects\AI_Final_Project\stock-market-bots\stock-data"
dir2 = r"C:\Users\MrKap\Projects\AI_Final_Project\stock-market-bots\\anew"

class qualitativeBot:
    def __init__(self):
        self.selections = [] #stock tags

        self.beginning = [] #beginning value on June 23, 2008
        self.end = [] #ending value on January 1, 2018
        self.difference = [] #end-begin value over the ~10 year period

    def getSelections(self):
        return self.selections
    
    def getBeginning(self):
        return self.beginning

    def getEnd(self):
        return self.end

    def getDifference(self):
        return self.difference    

    def select(self):
        filelist = os.listdir(dir1)
        
        #select first 3 stocks + get their score
        for i in range(0, 3):
            stock_tag = filelist[i].split("_")[0]

            #make api call to google
            query = stock_tag
            query = query.replace(' ', '+')
            url = f"https://google.com/search?q={query}"

            ua = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
            headers = {"user-agent" : ua}
            resp = requests.get(url, headers=headers)

            soup = BeautifulSoup(resp.content, "html.parser")

            results = []
            for g in soup.find_all('div', class_='r'):
                anchors = g.find_all('a')
                if anchors:
                    title = g.find('h3').text
                    results.append(title)
            #print(results)
            
            #bStart = myCsv[myCsv['Date'].str.match(start_date)]
            #bStart = float(bStart.iloc[0, 4])

            myCsv = pd.read_csv(("{0}\{1}".format(dir2, "ANEWDataSortable.csv")), sep = ",")
            score = 0
            for j in results:
                title = j.split()
                for k in title:
                    #print(k)
                    if not k.isalpha():
                        continue
                    bStart = myCsv[myCsv['Description'].str.match(k)]
                    #print(bStart)
                    if bStart.empty:
                        continue
                    else:
                        score += bStart.iloc[0, 2]
            
            
            self.selections.append((filelist[i], score))

        for i in range(3, len(filelist)):
            stock_tag = filelist[i].split("_")[0]

            #make api call to google
            query = stock_tag
            query = query.replace(' ', '+')
            url = f"https://google.com/search?q={query}"

            ua = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
            headers = {"user-agent" : ua}
            resp = requests.get(url, headers=headers)

            soup = BeautifulSoup(resp.content, "html.parser")

            results = []
            for g in soup.find_all('div', class_='r'):
                anchors = g.find_all('a')
                if anchors:
                    title = g.find('h3').text
                    results.append(title)

            myCsv = pd.read_csv(("{0}\{1}".format(dir2, "ANEWDataSortable.csv")), sep = ",")
            score = 0
            for j in results:
                title = j.split()
                for k in title:
                    if not k.isalpha():
                        continue
                    bStart = myCsv[myCsv['Description'].str.match(k)]
                    if bStart.empty:
                        continue
                    else:
                        score += bStart.iloc[0, 2]
            
            minVal = min(self.selections)[1]
            if(score > minVal):
                self.selections.remove(min(self.selections))
                self.selections.append((filelist[i], score))
        
    
        #get beginning values n + 10 days to give room for the Bayes for the project
        start_date = "2008-06-23"
        end_date = "2017-12-29"
        for i in self.selections:
            myCsv = pd.read_csv(("{0}\{1}".format(dir1, i[0])), sep = ",")
            bStart = myCsv[myCsv['Date'].str.match(start_date)]
            bStart = float(bStart.iloc[0, 4])
            bEnd =  myCsv[myCsv['Date'].str.match(end_date)]
            bEnd = float(bEnd.iloc[0, 4])
            self.beginning.append(bStart)
            self.end.append(bEnd)
            self.difference.append(bEnd-bStart)

        #get just stock tags
        self.selections = [x[0].split("_")[0] for x in self.selections]
            