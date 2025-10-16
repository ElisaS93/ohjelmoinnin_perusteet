# Create program which prompts the user to insert an integer and then display the steps to calculate the multiplicative persistency based on the user input.

# In short, the steps in the multiplicative persistency is calculated by multiplying digits together in a given integer. This process is then repeated for the result which makes the result value smaller on each iteration till the result contains only one digit.

# The program must stop the iteration when the result contains only one digit. Finally before the program closes, it shows the steps taken.

# Program starting.

# Check multiplicative persistence.
# Insert an integer: 796
# 7 * 9 * 6 = 378
# 3 * 7 * 8 = 168
# 1 * 6 * 8 = 48
# 4 * 8 = 32
# 3 * 2 = 6
# No more steps.

# This program took 5 step(s)

# Program ending.

print("Program starting.\n")
print("Check multiplicative persistence.")

n = int(input("Insert an integer: "))

steps = 0  


while n >= 10:
    digits = [int(d) for d in str(n)]
    print(" * ".join(map(str, digits)), end=" = ")
    product = 1
    for d in digits:
        product *= d
    print(product)
    n = product
    steps += 1

print("No more steps.\n")
print(f"This program took {steps} step(s)\n")
print("Program ending.")

#valmis