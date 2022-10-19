#!/usr/bin/python3
"""Text indentation"""


def text_indentation(text):
    """
    Args: Prints a text with 2 new lines after each of these character . ? and :
     There should be no space at the beginning or at the end of each printed line.
        :param text: the text to print (a string).

    Raises: TypeError - If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    count = 0
    while count < len(text) and text[count] == " ":
        count = count + 1

    while count < len(text):
        print(text[count], end="")
        if text[count] == "\n" or text[count] in ".?:":
            if text[count] in ".?:":
                print("\n")
            count = count + 1
            while count < len(text) and text[count] == " ":
                count = count + 1
            continue
        count = count + 1
