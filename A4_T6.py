# Program starting.
# Insert a positive integer: 10
# 10 -> 5 -> 16 -> 8 -> 4 -> 2 -> 1
# Sequence had 6 total steps.

# Program ending.

print("Program starting.")

n = int(input("Insert a positive integer: "))

if n <= 0:
    print("Please insert a positive integer next time.")
else:
    sequence = [n]
    steps = 0

    while n != 1:
        if n % 2 == 0:
            n = n // 2
        else: 
            n = 3 * n + 1
        sequence.append(n)
        steps += 1

    print(" -> ".join(map(str, sequence)))
    print(f"Sequence had {steps} total steps.")

print("\nProgram ending.")

#valmis
