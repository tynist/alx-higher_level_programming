#!/usr/bin/python3
def safe_function(fct, *args):
    """Executes a function safely"""
    import sys
    try:
        results = fct(*args)
        return results
    except Exception as error:
        print("Exception: {}".format(error), file=sys.stderr)
        return None
