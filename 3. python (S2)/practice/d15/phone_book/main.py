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
    
    # Create file
    if not os.path.exists(filename):
        open(filename, 'x', newline="")
        close(filename)
    
    # Add headers
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
        mode = input("Select a mode: ").lower()
        if mode in modes.values():
            return mode
        else:
            print("Invalid mode!")
            print_modes()


def file_operations(mode, filename):
    utils.logger.info("Executing file operation")
    
    def read_ops(name, filename):
        with open(filename, 'r', newline="") as file:
            while True:
                if name in csv.DictReader(file, name):
                    print(name)
                    break


    def write_ops(filename):

        def decision():
            while True:
                prompt = input("Are you sure you want to submit? (y/n): ").lower()
                if prompt == 'y':
                    return 'y'
                elif prompt == 'n':
                    return 'n'


        def write_to_file(stage, filename):
            with open(filename, 'a', newline="") as file:
                writer = csv.DictWriter(file, fieldnames=headers)
                writer.writerow(stage)


        stage = {"Name": None, "Surname": None, "Number": None, "Address": None}

        while True:
            # Data entry
            stage["Name"] = input("Enter name: ")
            stage["Surname"] = input("Enter surname: ")
            stage["Number"] = input("Enter number: ")
            stage["Address"] = input("Enter address: ")

            # Print the staged record
            print(stage)

            # Prompt the user if submit or not
            match decision():
                case 'y':
                    write_to_file(stage, filename)
                    break
                case 'n':
                    print("Record discarded")


    if mode == modes["Read(r)"]:
        read_ops(input("Please enter the name: ").lower(), filename)
    elif mode == modes["Write(w)"]:
        write_ops(filename)


if __name__ == "__main__":
    main(sys.argv)
