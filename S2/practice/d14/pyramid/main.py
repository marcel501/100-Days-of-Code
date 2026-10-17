'''
Print a specified triangle of constant height to terminal. 

'''


import pyramids
import sys
import utilities as util


HEIGHT = 6


def main():
    print_output(get_input())    


''' User input, validation and conversion '''
def get_input():
    util.logger.info("Stage 1.. Input operations")    

    while True:
        string_in = input("Enter triangle name: ")
        if string_in.isalpha() == True:
            break
        else:
            print("Alphabetic characters only")

    return string_in.lower()


''' Checking and output '''
def print_output(shape):
    util.logger.info("Stage 2.. Output operations")

    ''' Check if shape is present in database '''
    def check(shape):
        for i in pyramids.shape_list:
            if i["name"] == shape:
                return True, pyramids.shape_list.index(i)
        else:
            return False, 0
    
    # Record status and ID of shape.
    present, shape_id = check(shape)
    
    if present == False:
        sys.exit("Pyramid type not found")
    else:
        pyramids.shape_list[shape_id]["function"](HEIGHT)

if __name__ == "__main__":
    main()

