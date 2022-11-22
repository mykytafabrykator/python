#!/usr/bin/env python3

"""Select random students from list to ask questions.

A list of students is given in a form of a text file
"""

import random
import sys


# TODO (extra):
# - add multilanguage functionality (e.g. with babel package
#   or with something more diy)
# - ensure the sript corresponds to PEP8 and other coding style
#   standards

USAGE_TPL = '''
Receive file(s) as first argument(s)

USAGE:
    {script_name} file_name.txt

Alternative usage:
    {script_name} file_name.txt file_name_2.txt ... file_name_n.txt

Press enter to get a new name
Write 'x' or 'exit' and press enter to exit the script
Write 'b' or 'back' and press enter to get previous name
Write 'h' or 'history' and press enter to get all named that were chosen
'''

HELP_TPL = '''
Press enter to get a new name
Write 'x' or 'exit' and press enter to exit the script
Write 'b' or 'back' and press enter to get previous name
Write 'h' or 'history' and press enter to get all named that were chosen
'''
HELP_TPL = HELP_TPL.strip()
USAGE_TPL = USAGE_TPL.strip()


def process(filename, sort=True):
    """Expect a text file in UTF-8, with elements separated by \n."""

    # could be done as open().read(), but ctx mgr is better
    with open(filename) as f:
        text = f.read()             # read file as a whole implying it's small
        names = text.splitlines()

    # TODO(COMPLETED):
    # Fix case when there are gaps in input file
    # now it produces empty strings for each extra newline in a file

    # print(f'Got names: {names}')

    # Sort and remove gaps from names if needed
    if sort:
        names.sort()
        while names:
            if '' in names:
                # print('Gaps were here!')
                names.remove('')
            else:
                break
    return names


def ask(lst):
    """Function, which helps to interact with user inputs in console."""

    # TODO(COMPLETED):
    # add different inputs handling:
    #     - on enter, next name is given
    #     - on 'x' | 'exit', program stops execution (via return)
    #     - on 'b' | 'back', the question for name is postponed
    #       (e.g. pushed back to list)

    users_input = input('Press enter for new name\n')

    if (users_input == 'b' or users_input == 'back'):
        if len(lst) >= 2:
            command_back = 'back'
            return command_back
        else:
            print('You haven`t asked anyone before.\n')
            command_back = 'skip'
            return command_back

    elif (users_input == 'x' or users_input == 'exit'):
        text = 'Exited'
        print(text, file=sys.stderr)
        return -1

    elif (users_input == 'h' or users_input == 'history'):
        command_back = 'history'
        return command_back

    elif (users_input == 'help'):
        print(f'{HELP_TPL}')
        command_back = 'skip'
        return command_back

    else:
        return 0


def selector(sequence):
    """Random name chooser function."""
    elements = list(sequence)   # ensure it's a list

    # TODO: fix dirty algo
    history_list = []

    while elements:
        answer_ask = ask(history_list)
        # print(answer_ask)

        if answer_ask == -1:
            exit(-1)

        elif answer_ask == 'back':
            el = history_list[-2]
            history_list.remove(el)
            history_list.append(el)
            print(f'====>\t{el}')

        elif answer_ask == 'skip':
            pass

        elif answer_ask == 'history':
            print(f'{history_list}')

        else:
            idx = random.randint(0, len(elements) - 1)
            el = elements.pop(idx)
            history_list.append(el)
            print(f'====>\t{el}')
    print('The list has ended up.')


def run(args):
    """Main function."""

    # Separate script name from other args
    script_name = args[0]
    args = args[1:]
    # print(f'Args now: {script_name} | {args}')

    # no arguments provided -- print USAGE and exit with error
    if not args:
        text = USAGE_TPL.format(script_name=script_name)
        print(text, file=sys.stderr)
        exit(-1)

    while args:
        studlist_filename = args.pop(0)
        print(f'Working with the file named {studlist_filename}\n')
        names = process(studlist_filename)
        selector(names)

    # TODO(COMPLETED):
    # code logic to process numerous input files


if __name__ == '__main__':
    run(sys.argv)
