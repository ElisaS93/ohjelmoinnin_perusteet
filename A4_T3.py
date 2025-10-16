# Make Python program which prompts user to insert two integers. Use these integers together with the “while-loop” structure to create behaviour like in the example program run below.

# Note! the autograding tool will test that the correct structure has been applied.

print("Program starting.\n")

Starting = int(input("Insert starting value: "))
Stopping = int(input("Insert stopping value: "))

print("\nStarting for-loop:")
while Starting <= Stopping:
    print(Starting, end=' ')
    Starting += 1

print("\n\nProgram ending.")

#valmis