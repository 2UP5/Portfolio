# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 15:36:41 2022

@author: richa
"""
from sueca_suits_ranks import ranks_Dict, suits_Dict, rank_points
from sueca_cards import parseCard, Card
import os

# listedSaves = os.listdir("saveFiles")
trumpCardGlob = []
tricksList = []
test = []
listedTricks = []
highestResults = []

class Trick:
    
    def __init__(self, Trick):
        
        self.Trick = Trick
        return
    
    
    def __getitem__(self, Tricks):
        
        returned_Tricks = []
        returned_Tricks.append(Tricks)
        return returned_Tricks
    
    
    def points(self):
            
        ts = self.Trick
        totalPoints = 0
        trickList = [ts[0:2], ts[3:5], ts[6:8], ts[9:11]]
        
        for i in range(len(trickList)):
            
            pointsForTrick = Card(trickList[i][0]).points()
            totalPoints += pointsForTrick
            
            if i >= len(trickList) - 1:
                
                return totalPoints


    def trick_winner(self, t):
        
        highestResults.clear()
        listedTricks.clear()
        
        v = 0
        
        for i in range(4):
            
            listedTricks.insert(i, self.Trick[v:v + 2])
            v += 3
           

        highestResult = str()
        leadSuit = str(listedTricks[0][1])
        
        for j in range(3):
            
            firstCard = Card(listedTricks[j]).show()
            secondCard = Card(listedTricks[j + 1]).show()
            
            higher_ThanResult = parseCard(firstCard).higher_than(parseCard(secondCard), leadSuit, str(t))
            
            # print(j)
            # print(higher_ThanResult)
            # print(highestResult)
            
            if j >= 2:
                
                if higher_ThanResult == True and firstCard not in highestResults:
                
                    highestResults.insert(j, firstCard)
                    
                elif higher_ThanResult == False and secondCard not in highestResults:
                    
                    highestResults.insert(j, secondCard)
                
                
                if len(highestResults) > 1:
                    
                    finalComparison = parseCard(Card(highestResults[0]).show()).higher_than(parseCard(Card(highestResults[1]).show()), leadSuit, t)
                    # print(finalComparison)
                    
                    if finalComparison == True:
                        
                        highestResult = str(highestResults[0])
                    
                    elif finalComparison == False:
                        
                        highestResult = str(highestResults[1])
                    
                    # print("highestResult = " + highestResult)
                    return listedTricks.index(highestResult) + 1
                
                else:
                    
                    highestResult = str(highestResults[0])
                    return listedTricks.index(highestResult) + 1
                
            elif higher_ThanResult == True and firstCard not in highestResults:
                
                highestResults.insert(j, firstCard)
                j += 1
                
            
            elif higher_ThanResult == False and secondCard not in highestResults:
                                
                highestResults.insert(j, secondCard)
                j += 1
    
    
    def show(self):
        
        Trick = self.Trick
        return Trick
    
    
def parseTrick(ts):
    
    trickList = ts.split(" ")


    if len(trickList) == 4:
        
        parseTrick = Trick(ts)

        for i in range(len(trickList)):
            
            parseCard(trickList[i]).show()
            
            if i >= (len(trickList) - 1):
                
                return parseTrick

    else:
        
        raise ValueError ("A trick string must comprise four cards only; the given trick is: '%s'" % (ts))
        
    


def parseGameFile(fname):
    
    split_File = os.path.splitext(fname)
    getFileEXT = str(split_File[1])
    
    
    if getFileEXT == ".sueca":
        
        # f = open(os.getcwd() + "\\" + str(fname), "r")
        f = open(fname, "r")
        
        trumpCard = parseCard(f.readline(1) + f.readline(2).strip())
        tricks = f.readlines()
    
        
        new_tricks = []
        new_tricks.clear()
        
        for x in tricks:
            new_tricks.append(x.replace("\n", ""))
        
        
        if len(trumpCardGlob) > 0:
            
            trumpCardGlob.clear()
            trumpCardGlob.insert(0, trumpCard)
           
        else:
                
            trumpCardGlob.insert(0, trumpCard)
        
        if len(tricksList) < 0:
            for i in range(10):
                
                tricksList.insert(i, parseTrick(Trick(new_tricks[i]).show()))
        else:
            
            tricksList.clear()
            
            for i in range(10):
                
                try:
                    
                    tricksList.insert(i, parseTrick(Trick(new_tricks[i]).show()))
                
                except IndexError:
                    
                    pass
       
    else:
        
        print("Invalid File")
    
    
    tc = Card(trumpCardGlob[0][1])
    #ts = Trick(tricksList)
    ts = tricksList

    return tc, ts
    
   
