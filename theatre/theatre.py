#!/usr/bin/env python
import sys
import string
import yaml
from decimal import Decimal



def load_config(filename="./config.yml"):
    """
    Load config from a yaml config file
    """
    with open(filename, 'r') as file:
        theatre_config = yaml.safe_load(file)[0]

    return theatre_config

def generate_rows(row_range="a:z", seats_per_row=50):
    """
    This function expands a range of seat rows, with a number of seats per row.
    """
    #print(row_range)
    row_start = ord(row_range.split(':')[0])
    row_finish = ord(row_range.split(':')[1]) +1

    rows = [chr(row) for row in range(row_start,row_finish)]

    seats = {}
    for row in rows:
        for seat in range(seats_per_row):
            seat +=1
            seats[f"{row}{seat}"] = {"available": True}

    return(seats)



if __name__ == '__main__':
    # Some defaults for testing

    config = load_config()
    seats = generate_rows(config['costs']['seat_rows'][0],config['costs']['seats_per_row'])
    print(seats)
    print(config)

