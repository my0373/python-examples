#!/usr/bin/env python
import sys 
import string
import yaml 
from decimal import Decimal


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
    print("*"*80 + "\n")
    print(msg.center(80,)) 
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

def expand_range(config_range):
    
    first = config_range[0][0]
    last = config_range[0][2]
    
    return [range(ord(first),ord(last))]
         
    
    
def load_config(filename="./config.yml"):
    with open(filename,'r') as file:
        theatre_config = yaml.safe_load(file)[0]
    
    theatre_config['costs']['seat_rows'] = expand_range((theatre_config['costs']['seat_rows']))
    
    print(expand_range((theatre_config['costs']['seat_rows'])))


if __name__ == '__main__':
    
    # Some defaults for testing

    load_config()
    
    mainloop()
    
    