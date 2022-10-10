#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """Divides element by elements 2 list"""
    results = []
    for i in range(0, list_length):
        try:
            results.append(my_list_1[i] / my_list_2[i])
        except IndexError:
            print("out of range")
            results.append(0)
        except TypeError:
            print("wrong type")
            results.append(0)
        except ZeroDivisionError:
            print("division by 0")
            results.append(0)
        finally:
            pass
    return results
