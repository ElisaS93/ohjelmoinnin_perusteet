# Create a menu-driven Python program with following options:

# Insert a word
# Which stores user inserted word into memory.
# Show current word
# Prints the word from the memory
# Show current word in reverse
# Prints the word from the memory in reverse.
# Exit
# Stops the program gracefully
# Unknown option
# Initialize the Word with an empty string.

# Program starting.
# Options:
# 1 - Insert word
# 2 - Show current word
# 3 - Show current word in reverse
# 0 - Exit
# Your choice: 1
# Insert word: Banana

# Options:
# 1 - Insert word
# 2 - Show current word
# 3 - Show current word in reverse
# 0 - Exit
# Your choice: 2
# Current word - "Banana"

# Options:
# 1 - Insert word
# 2 - Show current word
# 3 - Show current word in reverse
# 0 - Exit
# Your choice: 3
# Word reversed - "ananaB"

# Options:
# 1 - Insert word
# 2 - Show current word
# 3 - Show current word in reverse
# 0 - Exit
# Your choice: 0


def displayMenu() -> None:  
    print("\nOptions:")
    print("1 - Insert word")
    print("2 - Show current word")
    print("3 - Show current word in reverse")
    print("0 - Exit")
    return int(input("Your choice: "))

def main() -> None:
    print("Program starting.")
    Word = ""
    choice = -1
    while choice != 0:
        choice = displayMenu()
        if choice == 1:
            Word = input("Insert word: ")
        elif choice == 2:
            print(f"Current word - \"{Word}\"")
        elif choice == 3:
            print(f"Word reversed - \"{Word[::-1]}\"")
        elif choice == 0:
            print("Exiting program.\n\nProgram ending.")
        else:
            print("Unknown option! Try again.")

main()

#valmis