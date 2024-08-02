# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 20:21:43 2022

@author: richard
"""

from sueca_games import *
from sueca_cards import *
from sueca_tricks import *
from sueca_suits_ranks import *
import os


class GameFileCouldNotBeFound(Exception):
    pass

class SuecaGameIncomplete(Exception):
    pass


# listedSaves = os.listdir("saveFiles")



def runGame(fname, showCards = False, showGame = False):
    
    countLines = 0

    # f = open(os.getcwd() + "\\saveFiles\\" + str(fname), "r")
    
    split_File = os.path.splitext(fname)
    getFileEXT = str(split_File[1])
    
    
    
    
    if getFileEXT == ".sueca" and os.path.exists(fname):
        
        f = open(fname, "r")
        isolate_Trump = f.readline(1) + f.readline(2).strip()
        linesAmount = f.readlines()
        
        if len(linesAmount) > 9:
            
            tc, ts = parseGameFile(fname)
            
            if showGame == True:
                
                print("Trump: " + str(tc[0]) + " - " + str(suit_full_name(tc[0][1])))
                
                for line in linesAmount:
                    
                    countLines += 1
                    print(str(countLines) + ": " + line.strip())
                    
            
            
                    
            if showCards == True:
                
                g = Game(tc)
                
                shownP1 = []
                shownP2 = []
                shownP3 = []
                shownP4 = []
                shownCards = [shownP1, shownP2, shownP3, shownP4] 
                
                for j in range(1, 5):
                    
                    for k in range(10):
                        
                        shownCards[j - 1].insert(k, g.cardsOf(j)[k].show()) #i know the order must be based on gameplay but better than nothing at this stage
                    
                if j >= 4:
                    
                    for l in range(1, 5):
                        
                        print("Player %i: %s \n" % (l, str(shownCards[l-1])))
        else:
            
            raise SuecaGameIncomplete ("Opened an incomplete sueca game")
                
    else:
                
        raise GameFileCouldNotBeFound ("Could not find the game file '%s'" % (fname))

    # print(countLines)
    
        # return sueca_CommandLine()





#Testing function    
# def sueca_CommandLine():
    
#     try:
        
#         fname = input("Enter game name: ")
#         split_File = os.path.splitext(fname)
        
#         getFileEXT = str(split_File[1])
            

#         if getFileEXT == ".sueca" and fname in listedSaves:
            
#             runGame(fname)
            
#         else:
            
#             raise GameFileCouldNotBeFound
           
        
#     except GameFileCouldNotBeFound:
        
#         print("Game not found, please try again")
#         return sueca_CommandLine()
        
# sueca_CommandLine()

    