'''
Simple text document editor program

'''

import sys


''' Check command line arguments '''
def check_arg(arg):
    if not len(arg) == 2:
        sys.exit("Incorrect number of arguments")
    else:
        return sys.argv[1]


''' Select mode '''
def mode_select():
    avail_modes = {'r': "Read",
                   'w': "Write", 
                   'a': "Append"
    }
    
    def print_modes(avail_modes):
        print("Modes of operation:")
        for key, value in avail_modes.items():
            print(f"{key}: {value}")
        print()
    
    while True:
        print_modes(avail_modes)
        mode = input("Enter mode: ")

        if mode.isalpha() == False:
            print("Alphabetic characters only!")
        elif len(mode) > 2:
            print("Enter only 1 character")
        elif mode in avail_modes:
            return mode.lower()


''' Read, write, append file operations '''
def file_operations(mode, file_name):

    def read_file():
        print(file.read())
    
    def write_file():
        while True:
            file_in = input("")
            if file_in == "":
                break
            else:
                file.write(file_in + "\n")


    def append_file():
        write_file()
    
    while True:
        try:
            with open(file_name, mode) as file:
                match mode:
                    case 'r':
                        read_file()
                        break
                    case 'w':
                        write_file()
                        break
                    case 'a':
                        append_file()
                        break
        except FileNotFoundError:
            open(file_name, 'x')
            close(file_name, 'x')


file_operations(mode_select(), check_arg(sys.argv))


