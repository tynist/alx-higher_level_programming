#!/usr/bin/python3
if __name__ == "__main__":
    """Print the number of and list of arguments"""
    import sys
    lists = sys.argv
    lengths = len(lists) - 1
    arg = "argument"
    print("{} argument{}{}".format(
            lth,
            "" if lengths == 1 else "s",
            "." if lengths == 0 else ":"))
    for i in range(1, len(lists)):
        print("{}: {}".format(i, lists[i]))
