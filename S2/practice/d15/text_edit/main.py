'''
Simple text document editor program

'''

import sys




''' Check command line arguments '''
def check_arg(arg):
    if not len(arg) == 2:
        sys.exit("Incorrect number of arguments")
    

''' Select mode '''
def mode_select():
    avail_modes = [
            {'r': "Read"},
            {'w': "Write"}, 
            {'a': "Append"}
    ]
    
    def print_modes(avail_modes):
        print("Modes of operation:")
        for key, value in avail_modes.items():
            print(f"{key}: {value}")

    
    while True:
        print_modes(avail_modes)
        mode = input("Enter mode: ")

        if mode.isalpha() == False:
            print("Alphabetic characters only!")
        elif len(mode) > 2:
            print("Enter only 1 character")
        elif mode in avail_modes:
            return tolower(mode)


def read_file():
    print(file.read())
    

def write_file():
    file.write(input())


def append_file():
    write_file()


check_arg(sys.argv)
file_name = sys.argv[1]

mode = mode_select()

with open(file_name, mode+"t"):
    match mode:
        case 'r':
            read_file()
            exit
        case 'w':
            write_file()
            exit
        case 'a':
            append_file()
            exit

