# 
# Python fibonacci sequence
#

import utilities as util


MAX = 40


def main():
    greet()
    print_output(calculate(get_input()))


def greet():
    print("# Fibonacci sequence #", end="\n\n")


def get_input():
    while True:
        try:
            number = int(input(f"Enter number of terms: "))
            if number > 2 and number < MAX:
                break
        except ValueError:
            print()
            util.logger.error("Non-numeric input detected")
    util.logger.info(f"Value of number is {number}")
    return number


def calculate(number):
    fib = [0, 1]
    for n in range(2, number):
        fib.append(fib[n - 1] + fib[n - 2])
    return fib


def print_output(fib):
    util.logger.debug("print_output function check")
    print(fib)


if __name__ == "__main__":
    main()
