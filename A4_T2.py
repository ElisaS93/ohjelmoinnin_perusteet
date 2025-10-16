# Copy the previous program and modify the behaviour to match the example program run below. This program must use “for-loop” structure.

# It is recommended to replace the print-command end character with space, so that all the iterations can be printed on the same row. Last iteration might require additional logic to get rid of the extra space at the end.

# Note! the autograding tool will test that the correct structure has been applied.

# Program starting.

# Insert starting value: 11
# Insert stopping value: 15

# Starting for-loop:
# 11 12 13 14 15

# Program ending.

print("Program starting.\n")

Starting = int(input("Insert starting value: "))
Stopping = int(input("Insert stopping value: "))

print("\nStarting for-loop:")
for i in range(Starting, Stopping + 1):
    print(i, end=' ')

print("\n\nProgram ending.")

#valmis