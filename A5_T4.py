# The following code should calculate the area of a rectangle based on the user inputs.

# Fix the example code below without altering defined function names or function parameters. Fixed code must produce similar results as is in the expected program runs. The code must also be fixed to match the requirements in the provided style guide.

def askDimension(PPrompt) -> float:
   Feed = float(input(f"Insert  {PPrompt}: "))
   return Feed

def calcRectangleArea(PWidth, PHeight) -> float:
   Area = PWidth * PHeight
   return float(Area)

def main():
    print("Program starting.")
    Width = askDimension("width")
    Height = askDimension("height")
    Area = calcRectangleArea(Width, Height)
    print("")
    print(f"Area is {Area}²")
    print("Program ending.")

main()

#valmis
