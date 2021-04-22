import os.path
import string
import re

MAX_DIGITS = 5


input_file_name = "input.txt"
# full incrementer syntax is {increment_from_X} where X is an n-digit number
incrementer_syntax_start = "{increment_from_"

if not os.path.isfile(input_file_name):
    print("Input file doesn't exist. Create file 'input.txt' "
          "to take text from, output will be 'output.txt'.")
else:
    with open('input.txt', 'r') as input_file:
        input_text = input_file.read()

# find where the replacement tokens are {increment_from_x}
# make it easy to repeatedly replace theen with consecutive numbers

# search for text in a loop and get indexes (store in list),
# read numbers and store them into a string list

# cut main string into list of strings, using the indexes
# (calculate from that and numbers string list for end of token

# create string from cut up main string + list of numbers to int

indexes = re.finditer(incrementer_syntax_start, text)
