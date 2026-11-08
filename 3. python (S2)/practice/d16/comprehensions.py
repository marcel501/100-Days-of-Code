#
# Comprehensions
#
# Comprehensions are compact declarations of new sequences stemmed from
# existing sequences utilising iterative execution logic.
# 
# Comprehensions exist in different forms:
# 1. List
# 2. Dictionary
# 3. Set
# 4. Generator
#


def list_comp():
    # [expression for item in iterable if condition]
    a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]

    even = [num for num in a if num % 2 == 0]
    odd = [num for num in a if num % 2 == 1]
    prime = [num for num in odd if not num == 1 and num % 3 == 1]
    # Prime list only works on low numbers

    print(f"Even list: {even}")
    print(f"Odd list: {odd}")
    print(f"Prime list: {prime}")


def dict_comp():
    # {key_expression: value_expression for item in iterable if condition}
    a = {num: num**2 for num in range(1, 6)}
    print(a)


def set_comp():
    # {expression for item in iterable if condition}
    a = {num**2 for num in range(1, 10)}
    print(a)


def generator_comp():
    # (expression for item in iterable if condition)
    a = (num for num in range(10) if num % 2 == 0)
    print(list(a))
        

print(
    '''
    Available modes:
    1:\tlist comprehension
    2:\tdictionary comprehension
    3:\tset comprehension
    4:\tgenerator comprehension
    '''
    )

match int(input("Select mode: ")):
    case 1:
        list_comp()
    case 2:
        dict_comp()
    case 3:
        set_comp()
    case 4:
        generator_comp()


