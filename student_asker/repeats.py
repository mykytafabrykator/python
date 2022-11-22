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


def getKeys(resDictionary, n):
    """Find and log out words by needed value"""
    a = sorted(resDictionary.items(), key=lambda x:x[1])
    for key, value in a:
        if value > n:
            print(f'{key} found in text {value} times')


def charsDeleter(lst):
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


def file_read(filename, sort=True):
    """Expect a text file in UTF-8, with text """

    with open(filename) as f:
        text = f.read()
        if sort:
            names = text.lower().split()
        else:
            names = text.split()

    # print(f'Got names: {names}')

    # Sort and remove gaps from names if needed
    if sort:
        names.sort()
        charsDeleter(names)
    return names


def equalityChecker(lst):
    """Check if the words are similar"""
    i = 0
    d_words = {}
    counter = 1

    while i < (len(lst)-1):
        d_words[lst[i]] = counter
        if lst[i] == lst[(i+1)]:
            counter += 1
            d_words[lst[i]] = counter
        else:
            counter = 1
        i += 1
    return d_words


def start(args):
    """Main function."""

    # Separate script name from other args
    script_name = args[0]
    args = args[1:]
    # print(f'{args} given args')

    # if no arguments given
    # print HELP_USAGE_TPL and exit with error
    if not args:
        text = HELP_USAGE_TPL.format(script_name=script_name)
        print(text, file=sys.stderr)
        exit(-1)
    else:
        if len(args) == 2:
            while args:
                fileName = args.pop(0)
                print(f'\nWorking with the file named {fileName}\n')
                text = file_read(fileName)
                # print(text)
                d_words = equalityChecker(text)
                amount = args.pop(0)
                getKeys(d_words, int(amount))
        else:
            text = HELP_USAGE_TPL.format(script_name=script_name)
            print(text, file=sys.stderr)
            exit(-1)


if __name__ == '__main__':
    start(sys.argv)
