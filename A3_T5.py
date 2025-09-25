print("Program starting.\n")

while True:
    print("Options:")
    print("1 - Celsius to Fahrenheit")
    print("2 - Fahrenheit to Celsius")
    print("0 - Exit")

    Choice = input("Your choice: ")

    if Choice == "1":
        Cel = float(input("Insert the amount of Celsius: "))
        Fah = Cel * 1.8 + 32
        print(f"{round(Cel, 1)} °C equals to {round(Fah, 1)} °F\n")

    elif Choice == "2":
        Fah = float(input("Insert the amount of Fahrenheit: "))
        Cel = (Fah - 32) / 1.8
        print(f"{round(Fah, 1)} °F equals to {round(Cel, 1)} °C\n")

    elif Choice == "0":
        print("Exiting...\n")
        print("Program ending.")
        break

    else:
        print("Unknown option.\n")