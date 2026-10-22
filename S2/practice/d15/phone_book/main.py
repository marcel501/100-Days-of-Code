'''

Phone book reader/writer program

'''


import csv
import sys
import re
import os

sys.path.insert(0, "./src/")
import utilities as utils


modes = {"Read(r)": 'r', "Write(w)": 'w'}
headers = ["Name", "Surname", "Number", "Address"]


def main(argv):
    filename = validate_args(argv)
    setup_database(filename)
    file_operations(mode_select(), filename)
    

def validate_args(arg):
    utils.logger.info("Validating arguments...")
    if len(arg) == 2:
        if (re.search("\\w+\\.+csv", arg[1]) == None):
            sys.exit("Invalid file-name format")
    else:
        sys.exit("Incorrect number of arguments")

    utils.logger.info(arg[1])
    return arg[1]


def setup_database(filename):
    utils.logger.info("Setting up the database...")
    if not os.path.exists(filename):
        open(filename, 'x', newline="")
        close(filename)
    
    with open(filename, 'r+', newline="") as file:
        file.seek(0)
        try:
            file_headers = next(csv.reader(file))
            if not file_headers == headers:
                sys.exit(f"File {filename} not empty!")
        except StopIteration:
            csv.writer(file).writerow(headers)
        finally:
            utils.logger.info(f"File: {filename}")
            utils.logger.info(f"Headers: {headers}") 
            utils.logger.info(f"File_headers: {file_headers}")


def mode_select():
    utils.logger.info("Fetching the mode")

    def print_modes():
        print("Available modes:")
        for mode in modes:
            print(mode)


    print_modes()    
    while True:
        ## Potential try clause
        mode = input("Select a mode: ").tolower()
        if mode in modes.values():
            return mode
        else:
            print("Invalid mode!")
            print_modes()


def file_operations(mode, filename):
    utils.logger.info("Executing file operation")
    
    # TODO: Develop read/ write functions
    
    def read_ops(name):
        with open(filename, 'r', newline="") as file:
            while True:
                #if name is in filename.csv
                    #Print the record
                    #break
                #if name is not in filename.csv
                   #repeat loop 


    def write_ops():
            #Ask for name
            #Ask for surname
            #Ask for number
            #Ask for address

            #Print the staged record
            #Prompt the user if submit or not
                # If not, then return
                # If yes, continue

        with open(filename, 'a', newline="") as file:
            #Commit the staged record into file


    if mode == modes("read(r)").values():
        # TODO: Read: Add prompt and feedback
        read_ops(input("Please enter the name: ").tolower())

    elif mode == modes("write(w)").values():
        # TODO: Write: Add multiple prompts for each element header 
    

if __name__ == "__main__":
    main(sys.argv)
