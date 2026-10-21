'''

Phone book reader/writer program

'''


import csv
import sys
import re
import os
import utilities as utils


modes = ["Read(r)", "Write(w)"]
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
    # TODO: Print prompt and get mode input from user
        # Develop a list of modes
    utils.logger.info("mode select")


def file_operations(mode, filename):
    utils.logger.info("Executing file operation")
    # TODO: Develop read/ write functions
        # TODO: Read: Add prompt and feedback
        # TODO: Write: Add multiple prompts for each element header 
    # TODO: Include conditional logic for mode
    utils.logger.info("File operations")


if __name__ == "__main__":
    main(sys.argv)
