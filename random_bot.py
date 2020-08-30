import os, random
import csv
import pandas as pd

dir1 = r"C:\Users\MrKap\Projects\AI_Final_Project\stock-market-bots\stock-data"

class randomBot:
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

        #select 3 random stocks
        for i in range(0, 3):
            file = random.choice(filelist)
            filelist.remove(file)
            self.selections.append(file)
    
        #get beginning values n + 10 days to give room for the Bayes for the project
        start_date = "2008-06-23"
        end_date = "2017-12-29"
        for i in self.selections:
            myCsv = pd.read_csv(("{0}\{1}".format(dir1, i)), sep = ",")
            bStart = myCsv[myCsv['Date'].str.match(start_date)]
            bStart = float(bStart.iloc[0, 4])
            bEnd =  myCsv[myCsv['Date'].str.match(end_date)]
            bEnd = float(bEnd.iloc[0, 4])
            self.beginning.append(bStart)
            self.end.append(bEnd)
            self.difference.append(bEnd-bStart)

        #get just stock tags
        self.selections = [x.split("_")[0] for x in self.selections]
            