'''
Print a specified triangle of varying height to terminal. 

'''


import sys
import utilities as util


HEIGHT = 6


def main():
    launch(convert(get_input()))    


''' Get & validate the user input '''
def get_input():
    string_in = input("Enter triangle name: ")
    while True:
        if string_in.isalpha() == True:
            break
        else:
            sys.exit("Alphabetic characters only")
    return string_in


''' 
Convert argument to a standard format 
Standard form: lower-case    
'''
def convert(i):
    return i.lower()


''' Launch printer '''
def launch(value):
    if __import__('pyramids').printer(value, HEIGHT) == False:
        sys.exit("Pyramid type not found")


if __name__ == "__main__":
    main()

