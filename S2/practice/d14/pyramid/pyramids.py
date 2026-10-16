'''
Triangle printing algorithms


'''


import utilities as util


# Printer control

''' Call appropriate printer function '''
def printer(value, height):
    if (value == "equilateral"):
       equilateral(height)
    elif (value == "isosceles"):
        isosceles(height)
    elif (value == "scalene"):
        scalene(height)
    elif (value == "right"):
        right(height)
    elif (value == "acute"):
        acute(height)
    elif (value == "obtuse"):
        obtuse(height)
    else:
        return False


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
    for row in range(0, height):
        print(" " * (height - row), end="")                 
        print("#" * (2*row + 1), end="") 
        print()                                


def isosceles(height):
    '''
    '''
    print("triangle2")
    # TODO: define triangle algorithm


def scalene(height):
    print("triangle3")
    # TODO: define triangle algorithm


def right(height):
    '''
            #
           ##
          ###
         ####   
        #####
    '''
    print("triangle4")
    # TODO: define triangle algorithm


def acute(height):
    print("triangle5")
    # TODO: define triangle algorithm


def obtuse(height):
    print("triangle6")
    # TODO: define triangle algorithm


