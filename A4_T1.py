# Create a Python program which prompts user to insert two integers. Use these integers together with the “for-loop” structure to create behaviour like in the example program example run below.

# Note! the autograding tool will test that the correct structure has been applied.

# Program starting.

# Insert starting value: 1
# Insert stopping value: 10

# Starting for-loop:
# 1
# 2
# 3
# 4
# 5
# 6
# 7
# 8
# 9
# 10

# Program ending.

Starting = int(input("Insert starting value: "))
Stopping = int(input("Insert starting value: "))

print("\nStarting for loop:")
while Starting < Stopping+1:
    print(Starting)
    Starting += 1 

print("\nProgram ending.")

#valmis