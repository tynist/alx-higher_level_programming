#!/usr/bin/python3
def safe_print_list(my_list=None, x=0):
    """Prints x elements of a list."""

    if my_list is None:
        my_list = []
    num = 0
    for i in range(x):
        try:
            print(f'{my_list[i]}', end='')
        except IndexError:
            continue
        num += 1
    print()
    return num
