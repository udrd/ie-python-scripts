import os.path
import string
import re


MAX_CHARS = 10
print()


# string is expected to be in the format nn}xx or -nn}x. can have minus sign
def get_number(text):
    """
    Return the number at the start of text, as a string.

    Keyword arguments:
    text -- string starting with a number
    """
    char = 0
    number = ""
    while char < len(text):
        if text[char] in string.digits + "-":
            number = number + text[char]
            char += 1
        else:
            break
    return number


input_file_name = "input.txt"
# full incrementer syntax is {increment_from_X}
# where X is an n<=MAX_CHARS-character number
incrementer_syntax_start = "{increment_from_"

if not os.path.isfile(input_file_name):
    print("Input file doesn't exist. Create file 'input.txt' "
          "to take text from, output will be 'output.txt'.")
else:
    with open('input.txt', 'r') as input_file:
        input_text = input_file.read()

indexes = re.finditer(incrementer_syntax_start, input_text)

start_values = []

for x in indexes:
    match_end = x.span()[1]
    start_values.append(
        get_number(input_text[match_end:match_end + MAX_CHARS]))

# cut main string into list of strings, using the indexes
# (calculate from that and numbers string list for end of token


# create string from cut up main string + list of numbers to int
