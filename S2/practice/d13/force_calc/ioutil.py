#
# Input/Output Utilities "ioutil" Library
#


# Variables

MAX_NUM = 2


# Functions

# Greet script
def greet():
    print("## Simple force calculator ##", end="\n\n")

# Mode input
def get_mode(mathlib):
    # 1. Print choices
    print("Available modes:")
    for m in mathlib.Modes:
        print(f"{m.value}: {m.name}\t({mathlib.equations[m]})")
    print("")
    # 2. Get user input
    mode = None
    while (mode == None or mode > len(mathlib.Modes)):
        mode = int(input("Select mode: "))
    # 3. Return
    return mode

# Number input
def get_num():
    for i in range(MAX_NUM - 1):
        num = list(map(int, input("Enter numbers: ").split()))
    return num



