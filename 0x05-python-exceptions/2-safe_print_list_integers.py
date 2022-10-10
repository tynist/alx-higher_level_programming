#!/usr/bin/python3
def safe_print_list_integers(my_list=None, x=0):
    """Prints the first x elements of a list and only integers."""
    if my_list is None:
        my_list = []
    num = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end='')
        except (ValueError, TypeError):
            continue
        num += 1
    print()
    return num
