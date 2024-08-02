# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 20:02:54 2022

@author: richard
"""

from sueca_suits_ranks import *


class CardInvalid(Exception):
    pass


class Card:
    
    def __init__(self, Card):
        
        self.Card = Card
        return
    
    
    def __getitem__(self, Cards):
        
        Cards = self.Card
        return Cards
    
    def points(self):
        
        cardRank = self.Card[0]
        pointsForCard = rank_points(cardRank)
        
        return pointsForCard
        
        
    def higher_than(self, other, s, t):
        
        ranksKeys = list(ranks_Dict.keys())  
        # suitsKeys = list(suits_Dict.keys())
        
        Card = self.Card
        cardRank = Card[0]
        cardSuit = Card[1]
        
        otherCard = other.show()
        otherCardRank = otherCard[0]
        otherCardSuit = otherCard[1]
        
        
        # print("Card = " + str(Card))
        # print("Other card = " + str(otherCard))
        
       
        higher_rank = rank_higher_than(cardRank, otherCardRank)
        
        if cardSuit == otherCardSuit: 
            
            if higher_rank == True:
                
                return True
            
            elif higher_rank == False:
                
                return False
        
        elif higher_rank == True or higher_rank == False:
            
                if cardSuit == t:
                    
                    return True
                
                elif otherCardSuit == t:
                    
                    return False
            
                elif otherCardSuit == s:
                    
                    return False
                
                elif cardSuit == s:
                    
                    return True
                
    
    
    def show(self):
        
        Card = self.Card
        return Card   
        
    

def parseCard(cs):
    
    if len(cs) == 2:
        
        parseCard = Card(cs)
        
        c = cs[0]
        s = cs[1]
        
        if c in ranks_Dict and s in suits_Dict:
           
            return parseCard
            
        else:
            
            if c not in ranks_Dict and s not in suits_Dict:
                    
                raise CardInvalid ("Card '%s' is invalid!" %(cs))
            
            elif c not in ranks_Dict:
                
                raise CardInvalid ("Card '%s' is invalid! Invalid rank symbol: '%c'" % (cs, c))
            
            elif s not in suits_Dict:
                
                raise CardInvalid ("Card '%s' is invalid! Invalid suit symbol: '%c'" % (cs, s))
        
    else:
        
        raise CardInvalid ("Card '%s' is invalid!" %(cs))
    
    
    
        

        
       
        
         
