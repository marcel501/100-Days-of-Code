"""
Function testing program

"""

def basic_functions():
    ''' Positional arguments (args)'''
    def positional(fruit, vechicle, name):
        pass


    ''' Keyword arguments (kwargs)'''
    def keyword(animal, name, age):
        pass


    ''' Mixed argument'''
    def mixed(vechicle, make, model):
        pass


    ''' Strictly positional arguments'''
    def strict_positional(item_1, item_2, item_3, /):
        pass


    ''' Strictly keyword arguments'''
    def strict_keyword(*, name, number, address):
        pass


    ''' Strictly combined arguments'''
    def strict_combined(item1, item2, /, *, address1, name):
        pass


    ''' Default parameter values'''
    def default_param(value = "unknown"):
        pass
    

    ''' Arbitrary positional arguments'''
    def arbitrary_args(*fruits):    # Accepts any number of values
        pass
    

    ''' Arbitrary mixed positional arguments (*arg)'''
    def arbitrary_mixed_args(name, *address):
        pass


    ''' Arbitrary keyword arguments (**kwarg)'''
    def arbitrary_key_args(**pets):
        pass


def built_in_functions():
    ''' Map '''
    def map_test():
        # Map applies a defined function or operation on every item within a
        # sequence
        map()
    

    ''' Filter '''
    def filter_test():
        # Returns values from a sequence only when it satisfies an imposed
        # condition
        filter()


    ''' Sorted '''
    def sorted_test():
        # Sorts a given sequence
        # It is useful in lambda functions when its used as a key
        sorted()
        

def special_functions():
    ''' Lambda'''
    def lambda_test(n):
        # The power of lambda is most useful inside functions.
        # Since it is anonymous, additional arguments to fully define lambda
        # can be anonymously passed in without any declarations.
        # It essentially turns variables into functions.
        return lambda a : a * n
        # In this case n is defined while a is anonymously passed in.

    
    ''' Decorators'''
    def encrypt(func):
        text = func.encode('ascii')
        for char in text:
            char += 1
    

    @encrypt
    def decoration_test():
        return "Hello there"


def recursion_test():
    




