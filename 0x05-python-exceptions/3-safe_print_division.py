#!/usr/bin/python3
def safe_print_division(a, b):
    """Divides two integers and prints the result"""
    try:
        results = a / b
    except (ZeroDivisionError, TypeError):
        results = None
    finally:
        print('Inside result: {}'.format(results))
        return results
