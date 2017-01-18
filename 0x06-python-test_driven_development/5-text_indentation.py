#!/usr/bin/python3
def text_indentation(text):
    if isinstance(text, str) is False:
        raise TypeError("text must be a string")
    else:
        text = text.replace(". ", ".\n\n")
        text = text.replace("? ", "?\n\n")
        text = text.replace(": ", ":\n\n")
        text = text.strip()
        print("{:s}".format(text))
    print("")
