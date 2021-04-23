# Text block repeater with number incrementers
Easily multiply a text block with optional number increments in each copy of the block.

## Installation
Python is needed to run the script

## How to use
* Create file 'input.txt' and paste in it the text you want repeated.
* Optional: Add as first or last line {repeat_times_X} where X is number of times to repeat the text, e.g. `{repeat_times_12}`. If `{repeat_times_X}` is omitted, it will decault to 10 repetitions.
* Optional: Mark any numbers you want incremented in each copy by replacing the number with `{increment_from_X}` where X is the starting number you want to use.
* Run the script, which will create file 'output.txt' with the generated text.
* **NOTE**: The script overwrites output.txt every time it is run.
* Copy the generated text from 'output.txt' to your dialogue file.

### Notes
* To have empty lines between copies of the text, leave an empty line before or after the input text. Any empty lines are also copied over.
* Maximum number of repetitions is 999, maximum incrementer numbers are 10 characters long.

### Example use (single line)
You want to add 7 more options to the 10 you already have, and your latest line is
```
~RandomNum(10,10)~ + ~Lorem ipsum dolor sit amet.~ + SubbranchXyz10
```

Create input.txt with contents:
```
{repeat_times_7}
+ ~RandomNum(17,{increment_from_11})~ + ~REPLACE~ + SubbranchAbc{increment_from_1}
```
This will create/overwrite output.txt with contents:
```
+ ~RandomNum(17,11)~ + ~REPLACE~ + SubbranchAbc1
+ ~RandomNum(17,12)~ + ~REPLACE~ + SubbranchAbc2
+ ~RandomNum(17,13)~ + ~REPLACE~ + SubbranchAbc3
+ ~RandomNum(17,14)~ + ~REPLACE~ + SubbranchAbc4
+ ~RandomNum(17,15)~ + ~REPLACE~ + SubbranchAbc5
+ ~RandomNum(17,16)~ + ~REPLACE~ + SubbranchAbc6
+ ~RandomNum(17,17)~ + ~REPLACE~ + SubbranchAbc7
```

### Example use (multiple lines)
You want to create an exchange that goes 30 times back and forth, so you need 30 similar blocks, each linking to the next.

Create input.txt with contents (plus an empty line at the bottom for spacing of text blocks):
```
{repeat_times_30}
IF ~~ THEN BEGIN ConversationBranchA{increment_from_1}
SAY ~REPLACE~
++ ~REPLACE~ + ConversationBranchA{increment_from_2}
END

```

Create input.txt with contents:
```
IF ~~ THEN BEGIN ConversationBranchA1
SAY ~REPLACE~
++ ~REPLACE~ + ConversationBranchA2
END

IF ~~ THEN BEGIN ConversationBranchA2
SAY ~REPLACE~
++ ~REPLACE~ + ConversationBranchA3
END

```

...

```
IF ~~ THEN BEGIN ConversationBranchA30
SAY ~REPLACE~
++ ~REPLACE~ + ConversationBranchA31
END

```

## License
MIT
