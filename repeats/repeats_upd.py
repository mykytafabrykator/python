#!/usr/bin/env python3

"""
Gets the number of the repeated words in the given file.
"""

import sys


HELP_USAGE_TPL = '''
Receive txt file as a first argument

How to use:
    {script_name} file_name.txt N

Where N is an amount of repeats
'''


def getKeys(resDictionary: dict, n: int) -> None:
    """Find and log out words by needed value"""

    result = sorted(resDictionary.items(), key=lambda x: x[1])
    for key, value in result:
        if value > n:
            print(f'{key} found in text {value} times')


def charsDeleter(lst: list) -> list:
    """Delete chars from the list"""

    # may be appended if needed
    chars = [' ', '!', ',', '.', '?', '"', "'", ';', ':', '/', '&', '@', '#']
    y = 0

    while y < len(lst):
        x = 0
        while x < len(chars):
            if chars[x] in lst[y]:
                lst[y] = lst[y].replace(chars[x], '')
            x += 1
        y += 1

    return lst


def file_read(filename: str) -> list:
    """Expect a text file in UTF-8, with text """

    with open(filename) as f:
        text = f.read()
        names = text.lower().split()
        names = charsDeleter(names)

    return names


def counter(lst: list) -> dict:
    """Check if the words are similar"""

    result = {}
    for word in lst:
        try:
            result[word] += 1
        except KeyError:
            result[word] = 1
    return result


def call_error(script_name: str) -> None:
    """Calling an error if asked"""

    text = HELP_USAGE_TPL.format(script_name=script_name)
    print(text, file=sys.stderr)
    exit(-1)


def start(args: list) -> None:
    """Main function."""

    script_name = args[0]
    args = args[1:]

    if not args:
        call_error(script_name)
    else:
        if len(args) == 2:
            fileName = args.pop(0)
            text = file_read(fileName)
            d_words = counter(text)
            getKeys(d_words, int(args.pop(0)))
        else:
            call_error(script_name)


if __name__ == '__main__':
    start(sys.argv)
