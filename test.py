#!/usr/bin/env python3



import os,sys


# cmd = input('what do you want? ')


def printWelcome():
    print('inserisci un comando')

def OpenApp():
    app = sys.argv[2]
    os.system(f'open /System/Applications/{app}.app') 
    
def HandelCommand():
    cmd = sys.argv[1]
    if cmd == 'open':
        OpenApp()
    elif cmd == 'cat':
        handleCat()
        

def handleCat():
    CatFile = sys.argv[2]
    file = open(CatFile, 'r')
    lines = file.readlines()
    print(' ')
    for line in lines:   
        print(line, end="")
          
          
def HasCommand():
    return len(sys.argv) >= 2





if __name__ == '__main__':
    print(sys.argv)
    if HasCommand():
        HandelCommand()
        
    else:
        printWelcome()
        
            
            