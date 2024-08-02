# -*- coding: utf-8 -*-
"""
@author: richard
"""



ranks_Dict = {
    
    "2": {"Full_Name": "2", "Points": 0},
    
    "3": {"Full_Name": "3", "Points": 0},
    
    "4": {"Full_Name": "4", "Points": 0},
    
    "5": {"Full_Name": "5", "Points": 0},
    
    "6": {"Full_Name": "6", "Points": 0},
    
    "Q": {"Full_Name": "Queen", "Points": 2},
    
    "J": {"Full_Name": "Jack",  "Points": 3},
    
    "K": {"Full_Name": "King",  "Points": 4},
    
    "7": {"Full_Name": "7",     "Points": 10},
    
    "A": {"Full_Name": "Ace",   "Points": 11},
    
    }


suits_Dict = {
    
    "H": {"Full_Name": "Hearts"},
    "D": {"Full_Name": "Diamonds"},
    "S": {"Full_Name": "Spades"},
    "C": {"Full_Name": "Clubs"},
    
    }




def valid_suit(s):

    s = str(s)
        
    if s in suits_Dict:
        
        return True
    
    elif s not in suits_Dict:
        
        return False
                
        
            
def valid_rank(r):
    
    r = str(r)
   
    if r in ranks_Dict:
        
        return True
    
    elif r not in ranks_Dict:
        
        return False



def suit_full_name(s):
    
    s = str(s)
    
    if valid_suit(s) == True:
            
        full_Name = suits_Dict[s].get("Full_Name")
        return full_Name
        
    else:        
         raise ValueError ("Invalid suit symbol: '%s'" % (s))
    
   
     


def rank_points(r):
   
    r = str(r)
        
    if valid_rank(r) == True:
        
        rankPoints = ranks_Dict[r].get("Points")
        return rankPoints
    
    else:
        
        raise ValueError ("Invalid rank symbol: '%s'" % (r))
        

    
    
def rank_higher_than(r1, r2):
    
    keys = list(ranks_Dict.keys())  
    
  
    if r1 not in keys and r2 not in keys:
            
        raise ValueError ("Invalid rank symbols: '%s' and '%s'" %(r1, r2))  
        
    elif r1 not in keys:
       
       raise ValueError ("Invalid rank symbol: '%s'" % (r1))
                        
   
    elif r2 not in keys:
       
        raise ValueError ("Invalid rank symbol: '%s'" % (r2))

    
    elif keys.index(r1) > keys.index(r2):
        
        return True
        
    else:
        
        return False

        
    









