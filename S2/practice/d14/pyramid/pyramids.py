'''
Triangle printing algorithms


'''


import utilities as util
import math

# Printer functions

def equilateral(height):
    '''
             #
            ###
           #####
          #######
         #########
        ###########
    '''
    util.logger.info("equilateral")

    if height < 1:
        util.logger.warning("Height cannot be 0")
    else:
        for row in range(0, height):
            print(" " * (height - row), end="")                 
            print("#" * (2*row + 1), end="") 
            print()                                


def isosceles(height):
    '''
           #  
           #
          ###
          ###
         #####
         #####
    '''
    util.logger.info("equilateral")

    TAPER = 2

    if height < 1:
        util.logger.warning("Height cannot be 0")
    else:
        for row in range(0, height):
            print(" " * (height - math.floor(row / TAPER)), end="")                 
            print("#" * (2 * math.floor(row / TAPER) + 1), end="") 
            print() 


def scalene(height):
    '''
           #  
           ###
          ######
          ########
         ###########
         #############
    '''
    print("In progress")
    # TODO: define triangle algorithm


def right(height):
    '''
             #
            ##
           ###
          ####   
         #####
        ######
    '''
    util.logger.info("equilateral")

    if height < 1:
        util.logger.warning("Height cannot be 0")
    else:
        for row in range(0, height):
            print(" " * (height - row), end="")                 
            print("#" * (row + 1), end="") 
            print()      


def acute(height):
    print("In progress")
    # TODO: define triangle algorithm


def obtuse(height):
    print("In progress")
    # TODO: define triangle algorithm


# Database

shape_list = [
    {"name": "equilateral", "function": equilateral}, 
    {"name": "isosceles", "function": isosceles}, 
    {"name": "scalene", "function": scalene},
    {"name": "right", "function": right},
    {"name": "acute", "function": acute},
    {"name": "obtuse", "function": obtuse}
]

