#!/usr/bin/python3
def fizzbuzz():
    """Prints numbers 1 to 100 separated by a space. 
    For multiples of three, print Fizz instead of the number.
    For multiples of five, print Buzz instead of the number.
    For multiples of three and five, print FizzBuzz instead of the number.
    """
    for nums in range(1, 101):
        if nums % 3 == 0 and nums % 5 == 0:
            print("FizzBuzz ", end="")
        elif nums % 3 == 0:
            print("Fizz ", end="")
        elif nums % 5 == 0:
            print("Buzz ", end="")
        else:
            print(f"{nums}", end="")
