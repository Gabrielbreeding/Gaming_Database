#!/usr/bin/python3
#Gabriel breeding

import sys
import pickle

datafile = open("gamelib.pickle", "rb")
games = pickle.load(datafile)
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
    
    elif fro == 'search':
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
    option = input("would you like to add or edit a game? ")
    
    if option[0] == 'A' or option[0] == 'a':
        games[len(games.keys())+1] = [input("What is the Genre? "), input("What is the Title? "), input("Who was the Developer? "), input("Who was the Publisher? "),
                                     input("On what system was it released? "), input("What year was it released? "), input("What is your rating on it? "),
                                     input("is it single or multiplayer? "), input("What was The Price? "), input("Have you Beaten it? "),
                                     input("When did you buy it? "), input("Any Notes? ")]
    elif option[0] == 'e' or option[0] == 'E':
        print('''
              Edit Menu
        ''')
        available = []
        for key in games.keys():
            if games[key][1] not in available:
                available.append(games[key][1])
                
        c = 0        
        for i in available:
            c+=1
            print()
            print("            "+ str(c) + ")   " + i)              
        print('''+================================+''')
        title = input("Please select a title from above to edit ")
        
        
        
    
def All():
    print("running Print All Games")
    keys = games.keys()
    for key in keys:
        details(key)
        
def Search(filt = 'menu'):
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
        destination = input("Please select a Search term from above ")
        direct(destination, 'search')
        
    elif filt == 'genre':
        available = []
        print('''
                  Genre Selection Menu: ''')
        for key in games.keys():
            term = games[key][0]
            if term not in available:
                available.append(games[key][0])
        
        c = 0        
        for i in available:
            c+=1
            print()
            print("            "+ str(c) + ")   ", i) 

               
        print('''+================================+''')
        destination = input("Please select a Search term from above ")
        if destination == "1":
            keys = list(games.keys())
            genre = games[keys[0]][0]
            
            for key in games.keys():
                if games[key][0] == genre:
                    details(key)
               
    elif filt == 'title':
        available = []
        print('''
                  Title Selection Menu: ''')
        for key in games.keys():
            if games[key][1] not in available:
                available.append(games[key][1])
                
        c = 0        
        for i in available:
            c+=1
            print()
            print("            "+ str(c) + ")   " + i) 

               
        print('''+================================+''')
        destination = input("Please select a title from above ")        
        
    elif filt == 'developer':
        available = []
        print('''
                  Developer Selection Menu: ''')
        for key in games.keys():
            if games[key][2] not in available:
                available.append(games[key][2])
                
        c = 0        
        for i in available:
            c+=1
            print()
            print("       "+ str(c) + ")   " + i) 

               
        print('''+================================+''')
        destination = input("Please select a developer from above ")   
    
    elif filt == 'publisher':
        available = []
        print('''
                  Publisher Selection Menu: ''')
        for key in games.keys():
            if games[key][3] not in available:
                available.append(games[key][3])
                
        c = 0        
        for i in available:
            c+=1
            print()
            print("       "+ str(c) + ")   " + i) 

               
        print('''+================================+''')
        destination = input("Please select a Publisher from above ")                
        
    elif filt == 'system':
        available = []
        print('''
                  System Selection Menu: ''')
        for key in games.keys():
            for j in range(len(games[key][4])):
                if games[key][4][j] not in available:
                    available.append(games[key][4][j])
                
        c = 0
        for i in available:
            c+=1
            print()
            print("       "+ str(c) + ")   " + i) 
        
        print()
        print("       B)    Back")

               
        print('''+================================+''')
        destination = input("Please select a System from above ")       
        
    elif filt == 'release':
        available = []
        print('''
                  Year Selection Menu: ''')
        for key in games.keys():
            if games[key][5] not in available:
                available.append(games[key][5])
                
        c = 0        
        for i in available:
            c+=1
            print()
            print("       "+ str(c) + ")   " + i) 

               
        print('''+================================+''')
        destination = input("Please select a Release Year from above ")            
        
    elif filt == 'rating':
        available = []
        print('''
                  Rating Selection Menu: ''')
        for key in games.keys():
            if games[key][6] not in available:
                available.append(games[key][6])
                
        c = 0        
        for i in available:
            c+=1
            print()
            print("       "+ str(c) + ")   " + i) 

               
        print('''+================================+''')
        destination = input("Please select a rating from above ")                
        
    elif filt == 's or m':
        available = []
        print('''
                  Multiplayer Selection Menu: ''')
        for key in games.keys():
            if games[key][7] not in available:
                available.append(games[key][7])
                
        c = 0        
        for i in available:
            c+=1
            print()
            print("       "+ str(c) + ")   " + i) 

               
        print('''+================================+''')
        destination = input("Please select an option from above ")               
        
    elif filt == 'price':
        available = []
        print('''
                  Price Selection Menu: ''')
        for key in games.keys():
            if games[key][8] not in available:
                available.append(games[key][8])
                
        c = 0        
        for i in available:
            c+=1
            print()
            print("       "+ str(c) + ")   " + i) 

               
        print('''+================================+''')
        destination = input("Please select a price from above ")           
        
    elif filt == 'beaten':
        available = []
        print('''
                  Beaten Selection Menu: ''')
        for key in games.keys():
            if games[key][9] not in available:
                available.append(games[key][9])
                
        c = 0        
        for i in available:
            c+=1
            print()
            print("       "+ str(c) + ")   " + i) 

               
        print('''+================================+''')
        destination = input("Please select an option from above ")          
        
    elif filt == 'purchase':
        available = []
        print('''
                  Purchase amount Selection Menu: ''')
        for key in games.keys():
            if games[key][10] not in available:
                available.append(games[key][10])
                
        c = 0        
        for i in available:
            c+=1
            print()
            print("       "+ str(c) + ")   " + i) 

               
        print('''+================================+''')
        destination = input("Please select a Purchase amount from above ")          
           
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
    
    