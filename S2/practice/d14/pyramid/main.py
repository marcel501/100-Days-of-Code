#
# Python pyramid printer
#


import pyramids
import sys
import utilities as util


ARG_NUM = 2


''' Main program execution flow'''
def main():
    launch(convert(validate(sys.argv)))    


''' Validate provided arguments '''
def validate(i):
    if not (len(i) == ARG_NUM):
        sys.exit("Incorrect number of arguments")
    elif i[1].isalpha() == False:
        sys.exit("Alphabetic characters only")
    else:
        return i[1]


''' Convert argument to a standard format '''
def convert(i):
    return i.lower()


''' Launch printer '''
def launch(value):
    if pyramids.printer(value) == False:
        sys.exit("Pyramid type not found")


if __name__ == "__main__":
    main()

