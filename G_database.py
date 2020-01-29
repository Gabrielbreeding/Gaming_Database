#!/usr/bin/python3
#Gabriel breeding

import sys
import pickle

games = {1: ['FPS', 'Halo3', 'Bungie', 'microsoft', 'xbox 360', '2007', '10', 'either', '$30.00', 'yes', '1/15/2008', 'the best halo!'],
         2: ['FPS', 'Destiny 2', 'Bungie', ' ', 'Xbox One, Ps4, Stadia, PC', '2017', '10', 'either', 'Free', 'yes', 'xx/xx/2017', 'Campaign is done, but much more to do!' ]}

datafile = open("gamelib.pickle", "wb")
pickle.dump(games, datafile)
datafile.close

def menu():
    print('''
              Gaming Database Menu:
              
        1)   Add/Edit Game
        
        2)   Print All Games
        
        3)   Search for Game
        
        4)   Remove a Game
        
        5)   Save
        
        Q)   Quit
        
        
      +================================+
        
    ''')
def direct(to, fro):
    if fro == 'main':
        if to == '1':
            AEGame()
        if to == '2':
            All()
        if to == '3':
            Search()
        if to == '4':
            Remove()
        if to == '5':
            Save()
        if to == 'Q' or to == 'q':
            sys.exit()
    
    if fro == 'search':
        if to == '1':
            Search('genre')
        if to == '2':
            Search('title')
        if to == '3':
            Search('developer')
        if to == '4':
            Search('system')
        if to == '5':
            Search('release')
        if to == '6':    
            Search('rating')
        if to == '7':
            Search('s or m')
        if to == '8':
            Search('price')
        if to == '9':   
            Search('beaten')
        if to == '10':
            Search('purchase')
        if to == 'B' or to == 'b':
            pass
            
       

        
def details(which):
    detail = games[which]
    print()
    print("Genre:", detail[0])
    print("Title:", detail[1])
    print("Developer:", detail[2])
    print("Publisher:", detail[3])
    print("Console:", detail[4])
    print("Release Year:", detail[5])
    print("Rating:", detail[6])
    print("Single or Multi:", detail[7])
    print("Price:", detail[8])
    print("Beaten:", detail[9])
    print("Purchase Date:", detail[10])
    print("Notes:", detail[11])
    print()
    print("+================================+")
        
        
def AEGame():
    print("running Add/Edit Game")
    
def All():
    print("running Print All Games")
    keys = games.keys()
    for key in keys:
        details(key)
        
def Search(filt):
    if filt == 'menu':       
        print('''
                  Search Menu:
                  
            1)   Search by Title
            
            2)   Search by Rating
            
            3)   Search by Genre
            
            4)   Search by System
            
            5)   Search by Developer
            
            6)   Search by Publisher
            
            7)   Search by Release Year
            
            8)   Search by Multiplayer
            
            9)   Search by Price
            
            10)  Search by Beaten
            
            11)  Search by Purchase Date
            
            B)   Back to Main Menu
            
            
          +================================+
        ''')
        destination = input("Please select a Search term from above")
        direct(destination, 'search')
        
    elif filt == 'genre':
        available = []
        print('''
                  Genre Selection Menu: ''')
        for key in games.keys():
            if games(key)[0] not in available:
                available.append(games(key)[0])
                
        for i in available:
            print()
            print("       ", i + ")   " + available[i]) 

               
        print('''+================================+''')
        destination = input("Please select a Search term from above")
        
           
        
    elif filt == 'title':
        destination = input("Please enter desired title for search: ")
        
    elif filt == 'developer':
        
    elif filt == 'system':
        
    elif filt == 'release':
        
    elif filt == 'rating':
        
    elif filt == 's or m':
        
    elif filt == 'price':
        
    elif filt == 'beaten':
        
    elif filt == 'purchase':
        
    
        
    
def Remove():
    print(" running Remove a Game")
    
def Save():
    print(" running Save")
    datafile = open("gamelib.pickle", "wb")
    pickle.dump(games, datafile)
    datafile.close
    print("saved!")
    
while True:
    menu()
    destination = input("Please select an option from above. ")
    direct(destination, 'main')
    
    