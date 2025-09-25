# Create menu program with submenus. Mainly for unit conversions. Use the values from the following table for unit conversions https://www.isa.org/getmedia/192f7bda-c77c-480a-8925-1a39787ed098/CCST-Conversions-document.pdf

# Menu options:

# Length
# Meters to kilometers
# Kilometers to meters
# Weight
# Grams to pounds
# Pounds to grams
# Exit
# “Exiting...”
# Handle all the data in floating point datatype. Remember to round every value in 1 digit precision right before displaying.

# Other possible prints:

# “Unknown option.”

# Program starting.
print("Program starting.\n")
# Welcome to the unit converter program!
print("Welcome to the unit converter program!\nFollow the menu instructions below.")
# Follow the menu instructions below.

# Options:
print("Options:")
# 1 - Length
print("1 - Length")
# 2 - Weight
print("2 - Weight")
# 0 - Exit
print("0 - Exit")
# Your choice: 1
Choice = input("Your choice: ")

# Length options:
# 1 - Meters to kilometers

if Choice == "1":
    print("Length options:")
    print("1 - Meters to kilometers")
    print("2 - Kilometers to meters")
    print("0 - Exit")
    Choice = input("Your choice: ")

    if Choice =="1":
        Meters = float(input("Insert meters: "))
        Kilometers = Meters / 1000
        print(f"{round(Meters, 1)} m is {round(Kilometers, 1)} km\n")
        print("Program ending.")
    elif Choice =="2":
        Kilometers = float(input("Insert kilometers: "))
        Meters = Kilometers * 1000
        print(f"{round(Kilometers, 1)} km is {round(Meters, 1)} m\n")
        print("Program ending.")
    elif Choice == "0":
        print("Exiting...\n")
        print("Program ending.")
    else:
        print("Unknown option.\n")

elif Choice == "2":
    print("Weight options:")
    print("1 - Grams to pounds")
    print("2 - Pounds to grams")
    print("0 - Exit")
    Choice = input("Your choice: ")

    if Choice =="1":
        Grams = float(input("Insert grams: "))
        Pounds = Grams * 0.002205
        print(f"{round(Grams, 1)} g is {round(Pounds, 1)} lb\n")
        print("Program ending.")
    elif Choice =="2":
        Pounds = float(input("Insert pounds: "))
        Grams = Pounds * 453.6
        print(f"{round(Pounds, 1)} lb is {round(Grams, 1)} g\n")
        print("Program ending.")
    elif Choice == "0":
        print("Exiting...\n")
        print("Program ending.")
    else:
        print("Unknown option.\n")


elif Choice == "0":
    print("Exiting...\n")
    print("Program ending.")
    

else:
    print("Unknown option.\n")


# Program ending.