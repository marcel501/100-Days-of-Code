#
# Python shape selector program
#

import shapes as sh


def main():
    greet()
    print_output(get_input())
    

def greet():
    print("# Welcome to the python shape selector #", end="\n\n")


def get_input():
    while True:
        shape = input("Enter shape name: ")
        if shape.isalpha() == True:
            break
    return shape


def print_output(shape):
    for s in sh.shapes:
        if shape == s["name"]:
            print(s)
            break
    else:
        print("Shape not found!")


if __name__ == "__main__":
    main()
