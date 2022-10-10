#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """Prints x elements of a list."""
    num = 0
    for i in range(x):
        try:
            print(f"{my_list[i]}", end='')
        except IndexError:
            continue
        num += 1
    print()
    return num
