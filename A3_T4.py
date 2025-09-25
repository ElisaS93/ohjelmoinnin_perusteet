# Extend the previous menu program by adding three more options to the menu.

# Options:

# Print the name backwards
# Your name backwards is "{NameBackwards}"
# Print the first character
# The first character in name "{Name}" is "{FirstChar}"
# Show the amount of characters in the name
# There are {NameLength} characters in the name "{Name}"

# Program starting.
# This is a program with simple menu, where you can choose which operation the program performs.
print("Program starting.\nThis is a program with simple menu, where you can choose which operation the program performs.")
# Before the menu, please insert your name: John
Name = input("Before the menu, please insert your name: ")
print("")

# Options:
print("Options:")
# 1 - Print welcome message
print("1 - Print welcome message")
# 2 - Print the name backwards
print("2 - Print the name backwards")
NameBackwards = (Name[::-1])
# 3 - Print the first character
print("3 - Print the first character")
FirstChar = (Name[0])
# 4 - Show the amount of characters in the name
print("4 - Show the amount of characters in the name")
NameLength = (len(Name))
# 0 - Exit
print("0 - Exit")
# Your choice: 1
Choise = int(input("Your choise: "))

# Welcome John!
if (Choise == 1):
    print(f"Welcome {Name}!")
elif (Choise ==2):
    print(f"Your name backwards is \"{NameBackwards}\"")
elif (Choise ==3):
    print(f"The first character in name \"{Name}\" is \"{FirstChar}\"")
elif (Choise ==4):
    print(f"There are {NameLength} characters in the name \"{Name}\"")
elif (Choise ==0):
    print("Exiting...")
else:
    print("Unknown option.")
# Welcome John!

# Program ending.
print("Program ending.")