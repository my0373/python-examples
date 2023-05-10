#!/usr/bin/env python
import sys 
def quit():
    """Exit the application
    """
    print("Quitting")
    sys.exit(0)

def login_banner():
    """
    Print a simple login banner
    """
    msg = "Welcome to the theatre app"
    padding = int((80 - len(msg)) / 2)
    print("*"*80 + "\n")
    print(" " * padding + msg + " "*padding) 
    
    
    print("\n" + "*"*80)
    
    
def mainloop():
    """
    The main loop of the application.
    """
    
    # Print the login banner when we start the loop.
    login_banner()
    
    #  
    moption = input("Press q to quit\n> ")
    if moption.lower() == 'q':
        quit() 

if __name__ == '__main__':
    
    mainloop()
    