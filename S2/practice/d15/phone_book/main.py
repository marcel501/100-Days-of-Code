'''

Phone book reader/writer program

'''


import csv
import sys
import re


def main():
    filename = validate_args(argv)
    setup_database(filename)
    file_operations(mode_select(), filename)
    

def validate_args(arg):
    if arg == 2:
        if not (re.search("\w+\.+csv", arg) == None):
            return arg
        else:
            sys.exit("Invalid file-name format")
    else:
        sys.exit("Incorrect number of arguments")


def setup_database():
    # TODO: Setup database 
        # Check if file exists
        # Create csv file (if not done so already)
        # TODO: Add database initialisation logic
            # TODO: Define a list of headers


def mode_select():
    # TODO: Print prompt and get mode input from user
        # Develop a list of modes


def file_operations(mode, filename):
    # TODO: Develop read/ write functions
        # TODO: Read: Add prompt and feedback
        # TODO: Write: Add multiple prompts for each element header 
    # TODO: Include conditional logic for mode


if __name__ == "__main__":
    main()
