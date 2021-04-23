import os.path
import string
import re


MAX_CHARS = 10
MAX_ITERATION_CHARS = 3
DEFAULT_ITERATIONS = 10
ITERATIONS_SYNTAX_START = "{repeat_times_"
INCREMENTER_SYNTAX_START = "{increment_from_"
SYNTAX_END = "}"
INPUT_FILE = "input.txt"
OUTPUT_FILE = "output_sequence.txt"


def get_number(text):
    """
    Return the number at the start of text, as a string.

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


def make_output(text, match_indexes, numbers, iterations):
    """
    Create text to write to file from parameters.

    text          -- text of file, including incrementer instructions
    match_indexes -- indexes of instruction matches in 'text'
    numbers       -- incrementer starting numbers
    iterations    -- number of repetitions of the adjusted text
    """
    # find start and stop indices of text parts to be kept
    piece_start_end = [0]
    for (match, number) in zip(match_indexes, numbers):
        piece_start_end.append(match[0])
        piece_start_end.append(match[1] + len(number) + len(SYNTAX_END))
    piece_start_end.append(len(text) - 1)
    # get text parts to be kept
    text_pieces = []
    for n in range(0, len(numbers)*2 + 1, 2):
        text_pieces.append(text[piece_start_end[n]:piece_start_end[n+1]])
    # get output
    output = ""
    for iteration in range(iterations):
        for (text_piece, number) in zip(text_pieces, numbers):
            output += text_piece + str(int(number) + iteration)
        output += text_pieces[-1] + "\n"
    return output


# get text
input_file_name = "input.txt"
if not os.path.isfile(input_file_name):
    print("Input file doesn't exist. Create file 'input.txt' "
          "to take text from, output will be 'output.txt'.")
else:
    with open(INPUT_FILE, 'r') as input_file:
        input_text = input_file.read()

# read iteration instruction from text if there, then remove it from text
iteration_matches = re.finditer(ITERATIONS_SYNTAX_START, input_text)

iterations = DEFAULT_ITERATIONS
for match in iteration_matches:
    match_end = match.span()[1]
    iterations_string = get_number(
        input_text[match_end:match_end + MAX_ITERATION_CHARS])
    iterations = int(iterations_string)
    input_text = input_text.replace(
        ITERATIONS_SYNTAX_START + iterations_string + SYNTAX_END + "\n", "")

# find any incrementers in the text file
matches = re.finditer(INCREMENTER_SYNTAX_START, input_text)

start_values = []
match_indexes = []

for match in matches:
    match_indexes.append(match.span())

for match in match_indexes:
    match_end = match[1]
    start_values.append(
        get_number(input_text[match_end:match_end + MAX_CHARS]))

# make output text and write
if len(start_values):
    output_text = make_output(input_text, match_indexes,
                              start_values, iterations)
else:
    output_text = input_text * iterations

with open(OUTPUT_FILE, 'w+') as output_file:
    output_file.write(output_text)
