# -*- coding: utf-8 -*-
"""
Created on Thu Nov 24 15:39:36 2022

@author: richa
"""
from sueca_suits_ranks import rank_points
from sueca_cards import Card, parseCard
from sueca_tricks import *


class CardAlreadyPlayed(Exception):
    pass

class DealerDoesNotHoldTrumpCard(Exception):
    pass

class IllegalCardPlayed(Exception):
    pass


player1 = []
player2 = [] 
player3 = [] 
player4 = []

list_OfTricks = []
temp = []


def clearPlayerList():
    
    players = [player1, player2, player3, player4]
    
    if len(list_OfTricks) > 0:
        
        list_OfTricks.clear()
    
    
    for i in range(len(players)):
        
        players[i].clear()
    
        
        

class Game:
    
    def __init__(self, gameCard):
        
        self.gameCard = gameCard
        return
    
    
    def __getitem__(self):
        
        t_list = self.t
        return t_list

    
    def gameTrump(self):
        
        gameCard = self.gameCard
        return Card(gameCard)
    
    
    def score(self):
        
        game_Cards = ""
        
        pair1Cards = []
        pair1Points = 0
        
        pair2Cards = []
        pair2Points = 0
    
    
        #TEAM 1 = PLAYER 2 AND 4
        #TEAM 2 = PLAYER 1 AND 3
        #DEALER = PLAYER 2
        
        game_Cards = self.game_tricks
        
        pair1Cards.append(game_Cards[3:5])
        pair1Cards.append(game_Cards[9:11])
        
        pair2Cards.append(game_Cards[0:2])
        pair2Cards.append(game_Cards[6:8])
        
        
        for x in range(len(pair1Cards)):
           
            pair1Points += rank_points(pair1Cards[x][0])
            pair2Points += rank_points(pair2Cards[x][0])
            
            if x >= len(pair1Cards) - 1:
                
                return pair1Points, pair2Points


    def gameTricks(self):
        
        return tricksList
    
    
    def playTrick(self, t):
        
        self.game_tricks = str(t.show())
        return self.game_tricks
    
    
    def cardsOf(self, p):
        
        players = [player1, player2, player3, player4]
        slices = [(0, 2), (3, 5), (6, 8), (9, 11)]
        
        clearPlayerList()
       
        
        # print("function called")


        if p in range(1, 5):
            
            # print("if statement entered")
                    
            for i in range(10):

                # print("loop entered")
                list_OfTricks.insert(i, tricksList[i].show())
                
                if i >= 9:
                    
                    for j in range(10):
                        
                        w = parseTrick(list_OfTricks[j]).trick_winner(trumpCardGlob[0][1])
                        storedValOfW = list_OfTricks[j][slices[w - 1][0] : slices[w - 1][1]]
                        
                        
                        for k in range(4):
                            
                            players[k].append(Card(list_OfTricks[j][slices[k][0] : slices[k][1]]))
                                
            
            return players[p - 1]

    
        elif p not in range(1, 5):
            
            print("else entered")
            raise ValueError ("Invalid player number '%i'" % (p))
                

        