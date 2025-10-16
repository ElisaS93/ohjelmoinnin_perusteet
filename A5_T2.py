# Create Python program which is able to print user input with a decorative frame.

# Program must consist of two functions:

# main-function
# Print starting and ending statements.
# Print any empty row (see example program run)
# Prompt user to insert a word.
# Pass the inserted word into the frameWord-function.
# Returns None
# frameWord
# Takes PWord as a parameter.
# Prints the framing and the PWord
# Hint: Multiply the asterisk '*'-character.
# Returns None
# Note! Tests for this task relies on properly defined functions and may fail if the program is not written according to the instructions.


def frameWord(Pword):
    print("*" * (len(Pword)+4))
    print(f"* {Pword} *")
    print("*" * (len(Pword)+4))
    return None

def main():
    print("Program starting.")
    word = input("Insert word: ")
    print("")
    frameWord(word)
    print("Program ending.")
    return None

main()

#valmis