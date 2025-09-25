# In this task the idea is to create a program where user can define an integer and choose the decision structure being applied to the inserted integer. Certain rules must be applied to specified value tresholds and the decision structure has partial role in the end results. Structure, order and operators matter, so do exactly as the task describes.

# Prompt user to insert value as an integer.
# Display menu
# option 1 - In one multi-branched decision
# option 2 - Independent if-statement decisions
# option 0 - Exit
# Prompt user to choose option
# Apply following math operations in the options 1 & 2
# One multi-branched decision structure:
# Value is 400 or more => add 44 to the existing value
# Value is 200 or more => add 22 to the existing value
# Value is 100 or more => add 11 to the existing value
# Independent if-statement decisions one after another:
# Value is 400 or more => add 44 to the existing value
# Value is 200 or more => add 22 to the existing value
# Value is 100 or more => add 11 to the existing value
# Exit: “Exiting…”
# At the end of the options 1 & 2, show the results like in the example program runs.
# Other possible output variats:

# “Unknown option.”


# Program starting.
# Testing decision structures.
print("Program starting.\nTesting decision structures.")
# Insert an integer: 250
Number = int(input("Insert an integer: "))
# Options:
print("Options:")
# 1 - In one multi-branched decision
print("1 - In one multi-branched decision")
# 2 - In multiple independent if-statements
print("2 - In multiple independent if-statements")
# 0 - Exit
print("0 - Exit")
# Your choice: 1
Choice = input("Your choice: ")
# Using one multi-branched decision structure.
if Choice == "1":
    print("Using one multi-branched decision structure.")
    if Number >= 400:
        Result = Number + 44
    elif Number >= 200:
        Result = Number + 22
    elif Number >= 100:
        Result = Number + 11
    elif Number <100:
        Result = Number

    print(f"Result is {Result}\n")
    print("Program ending.")


elif Choice == "2":
    print("Using multiple independent if-statements structure.")
    if Number >= 400:
        Number = Number + 44
    if Number >= 200:
        Number = Number + 22
    if Number >= 100:
        Number = Number + 11
    if Number <100:
        Number = Number

    print(f"Result is {Number}\n")
    print("Program ending.")

elif Choice == "0":
    print("Exiting...\n")
    print("Program ending.")
    

else:
    print("Unknown option.\n")