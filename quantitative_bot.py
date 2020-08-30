import os, random
import csv
from sklearn import preprocessing
from sklearn.naive_bayes import GaussianNB
import pandas as pd
import numpy as np

dir1 = r"C:\Users\MrKap\Projects\AI_Final_Project\stock-market-bots\stock-data"

class quantitativeBot:
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
    
        found = 0
        while(found < 3):
            filename = random.choice(filelist)
            filelist.remove(filename)

            #print(filename)

            bayes_start_date = "2008-06-06"
            bayes_end_date = "2008-06-23"
            myCsv = pd.read_csv(("{0}\{1}".format(dir1, filename)), sep = ",")
            bStart = myCsv.index[myCsv["Date"].str.match(bayes_start_date)].tolist()
            bEnd =  myCsv.index[myCsv["Date"].str.match(bayes_end_date)].tolist()
            closes = []

            #print(bStart)
            #print(bEnd)

            for i in range(int(bStart[0]), int(bEnd[0])):
                closes.append(myCsv.iloc[i, 4])
            
            diff = []
            for i in range(1, len(closes)):
                prev = closes[i-1]
                cur = closes[i]
                if(cur-prev > 0):
                    diff.append("positive")
                else:
                    diff.append("negative")
            
            labels = []
            for j in diff:
                if(j == "positive"):
                    labels.append(0) #buy
                else:
                    labels.append(1) #sell

            lblEnc = preprocessing.LabelEncoder()
            features = lblEnc.fit_transform(diff)
            features = features.reshape(-1,1)

            model = GaussianNB()

            model.fit(features, labels)

            predicted = model.predict([[0, 1]])

            if(predicted == 1):
                self.selections.append(filename)
                found += 1

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
            