#
# Lightweight Engineering Calculator 1000
#


# Modules

import ioutil
import mathlib as ml


# Variables

num = []
mode = None


# Functions

# Basic input
def aquire_input(num, mode):
    mode = ioutil.get_mode(ml)
    num = ioutil.get_num()
    return num, mode

# Calculate result
def calculate(num, mode):
    result = None
    match mode:
        case 1:
            result = num[0] * num[1]
        case 2:
            result = num[1] / num[1]
        case 3:
            result = num[1] / num[1]
    return result

# Output result
def output(result, mode):
    print(f"The {ml.Modes(mode).name} is: {result}{ml.units[ml.Modes(mode)]}")


# Main flow

ioutil.greet()
num, mode = aquire_input(num, mode)
output(calculate(num, mode), mode)

