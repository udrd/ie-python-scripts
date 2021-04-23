import os.path
import string
import re


MAX_CHARS = 10
MAX_ITERATION_CHARS = 3
DEFAULT_ITERATIONS = 10
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
# where X is an n <= MAX_CHARS - character number

if not os.path.isfile(input_file_name):
    print("Input file doesn't exist. Create file 'input.txt' "
          "to take text from, output will be 'output.txt'.")
else:
    with open('input.txt', 'r') as input_file:
        input_text = input_file.read()

iterations_syntax_start = "{repeat_times_"
incrementer_syntax_start = "{increment_from_"

indexes = re.finditer(iterations_syntax_start, input_text)


iterations = DEFAULT_ITERATIONS
for index in indexes:
    match_end = index.span()[1]
    iterations = get_number(
        input_text[match_end:match_end + MAX_ITERATION_CHARS])

indexes = re.finditer(incrementer_syntax_start, input_text)

start_values = []

for index in indexes:
    match_end = index.span()[1]
    start_values.append(
        get_number(input_text[match_end:match_end + MAX_CHARS]))

# cut main string into list of strings, using the indexes
# (calculate from that and numbers string list for end of token

for iteration in range(iterations):
    for index in indexes:
        span

# create string from cut up main string + list of numbers to int
