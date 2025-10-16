# Make a program, which prompts user to insert words. Program must stop prompting words if user inserts empty word. After stopping the repetitive prompt, print the amount of words and characters that the user inserted.

# Program starting.

# Insert word (empty stops): Close
# Insert word (empty stops): the
# Insert word (empty stops): loop
# Insert word (empty stops): 

# You inserted:
# - 3 words
# - 12 characters

# Program ending.

print("Program starting.\n")
WordCount = 0
CharCount = 0

Word = input("Insert word (empty stops): ")
while Word != '':
    WordCount += 1
    CharCount += len(Word)
    Word = input("Insert word (empty stops): ")

print("\nYou inserted:")
print(f"- {WordCount} words")
print(f"- {CharCount} characters")
print("\nProgram ending.")

#valmis