# Modules
from enum import Enum


# Variables & data structures
a = None
b = None
mode = None

class Modes(Enum):
    FORCE = 1
    STRESS = 2
    STRAIN = 3

units = {
    Modes.FORCE: " N",
    Modes.STRESS: " N/m^2",
    Modes.STRAIN: ""
}

equations = {
    Modes.FORCE: "F = σ * A",
    Modes.STRESS: "σ = F / A",
    Modes.STRAIN: "ε = Δl / l"
}


# Functions
def greet():
    print("## Simple force calculator ##", end="\n\n")

def get_mode_print():
    print("Available modes:")
    for m in Modes:
        print(f"{m.value}: {m.name}\t({equations[m]})")
    print("")

def get_mode_input():
    global mode
    while (mode == None or mode > len(Modes)):
        mode = int(input("Select mode: "))

def get_mode():
    get_mode_print()
    get_mode_input()

def get_num():
    global a, b
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
 
def user_input():
    get_mode()
    get_num()

def calculate():
    result = None
    match mode:
        case 1:
            result = a * b
        case 2:
            result = a / b
        case 3:
            result = a / b
    return result

def output(result):
    print(f"The {Modes(mode).name} is: {result}{units[Modes(mode)]}")


# Main flow
greet()
user_input()
output(calculate())
