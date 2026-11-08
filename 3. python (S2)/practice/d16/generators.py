#
# Generator functions
#
# Overview of python generator functions
#

'''
The yield keyword is comparable to the return; however it behaves differently.
Its capability is to produce a sequence of values overtime as it essentially
functions as a save point pausing the function when it returns a single value.
The state of the function can be resumed anytime until the function is 
returned or finished.
'''

def multiple(max):
    num = 1
    while num < max:
        yield num**2
        num += 1


a = multiple(10)
for num in a:
    print(num)

