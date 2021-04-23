import os.path
import string
import re


MAX_CHARS = 10
MAX_ITERATION_CHARS = 3
DEFAULT_ITERATIONS = 10
ITERATIONS_SYNTAX_START = "{repeat_times_"
INCREMENTER_SYNTAX_START = "{increment_from_"
SYNTAX_END = "}"

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


def make_output(text, indexes, numbers, iterations):
    """
    Create text to write to file from parameters.


    """

    return "placeholder"


input_file_name = "input.txt"
# full incrementer syntax is {increment_from_X}
# where X is an n <= MAX_CHARS - character number

if not os.path.isfile(input_file_name):
    print("Input file doesn't exist. Create file 'input.txt' "
          "to take text from, output will be 'output.txt'.")
else:
    with open('input.txt', 'r') as input_file:
        input_text = input_file.read()

iteration_indexes = re.finditer(ITERATIONS_SYNTAX_START, input_text)

iterations = DEFAULT_ITERATIONS
for index in iteration_indexes:
    match_end = index.span()[1]
    iterations_string = get_number(
        input_text[match_end:match_end + MAX_ITERATION_CHARS])
    iterations = int(iterations_string)
    input_text = input_text.replace(
        ITERATIONS_SYNTAX_START + iterations_string + SYNTAX_END + "\n", "")

indexes = re.finditer(INCREMENTER_SYNTAX_START, input_text)

start_values = []

for index in indexes:
    match_end = index.span()[1]
    start_values.append(
        get_number(input_text[match_end:match_end + MAX_CHARS]))

# cut main string into list of strings, using the indexes
# (calculate from that and numbers string list for end of token


if len(start_values):
    output_text = make_output(input_text, indexes, start_values, iterations)
else:
    output_text = input_text * iterations

print(output_text)
# create string from cut up main string + list of numbers to int
