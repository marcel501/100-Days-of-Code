# Modules

from enum import Enum


# Variables & data structures

TARGET = 57

class distances(Enum):
    HERE = 0
    VERY_CLOSE = 1
    CLOSE = 2
    FAR = 3
    VERY_FAR = 4


# Functions

def greet():
    print("# Python number game #", end="\n\n")


def get_input():
    while True:
        try:
            number = int(input("Enter number: "))
            break
        except ValueError:
            print()
    return number


def calculate(number):
    distance = abs(TARGET - number)
    
    if distance == 0:
        value = 0
    elif distance > 0 and distance <= 10:
        value = 1
    elif distance > 10 and distance <= 20:
        value = 2
    elif distance > 20 and distance <= 30:
        value = 3
    elif distance > 40:
        value = 4

    return value


def print_output(value):
    print("The target is " + distances(value).name)


# Main

greet()
print_output(calculate(get_input()))

