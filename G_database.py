#!/usr/bin/python3
#Gabriel breeding

import sys


def menu():
    print('''
              Gaming Database Menu:
              
        1)   Add/Edit Game
        
        2)   Print All Games
        
        3)   Search by Title
        
        4)   Remove a Game
        
        5)   Save
        
        Q)   Quit
        
        
      +================================+
        
    ''')
def direct(where):
    if where == '1':
        AEGame()
    elif where == '2':
        All()
    elif where == '3':
        Search('title')
    elif where == '4':
        Remove()
    elif where == '5':
        Save()
    elif where == 'Q' or where == 'q':
        sys.exit()
        
        
        
def AEGame():
    print("running Add/Edit Game")
    
def All():
    print("running Print All Games")
    
def Search(filt):
    print(" Search by Title")
    
def Remove():
    print(" running Remove a Game")
    
def Save():
    print(" running Save")
    
while True:
    menu()
    destination = input("Please select an option from above. ")
    direct(destination)
    
    