#!/usr/bin/python3
# 5-text_indentation.py
def text_indentation(content):
    if not isinstance(content, str):
        raise TypeError("content must be a string")

    x = 0
    while x < len(content) and content[x] == ' ':
        x += 1

    while x < len(content):
        print(content[x], end="")
        if content[x] == "\n" or content[x] in ".?:":
            if content[x] in ".?:":
                print("\n")
            x += 1
            while x < len(content) and content[x] == ' ':
                x += 1
            continue
        x += 1
