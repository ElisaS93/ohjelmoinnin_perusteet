WEEKDAYS = ("Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday",)

def readFile(PFilename: str, PRows: list[str]) -> None:
    print('Reading file "{}".'.format(PFilename))
    # 0. Clear PRows list just in case
    # 1. Open filehandle
    # 2. Read filehandle line-by-line
    # 2.1. Skip first line (header row)
    # 2.2. Check if line is empty '\n'
    # 2.3. Add non empty datarow without newline at the end.
    # 3. Close filehandle 
    return None

def analyseTimestamps(PRows: list[str], PResults: list[str]) -> None:
    print("Analysing timestamps.")
    # Append results to the PResults list
    # Initialise helper list 
    # WeekdayTimestampAmount: list[int] = [0, 0, 0, 0, 0, 0, 0]
    # Iterate rows with i
    #   Iterate WEEKDAYS with j
    #      Check if the row starts with the weekday name
    #          Count the day in proper place
    # Iterate WEEKDAYS with i and append the daily results
    # Clear the helper list
    return None

def displayResults(PResults: list[str]) -> None:
    print("Displaying results.")
    # Iterate results and print for the user
    return None

def main() -> None:
    # 1. Initialise
    # 1.1. Initialise rows list
    Rows: list[str] = [] #list for storing file rows
    # 1.2. Initialise results list
    Results: list[str] = [] #list for strogin analysis results
    # 2. Operate
    print("Program starting.")
    # 2.1. Ask user to define filename
    Filename = input("Insert filename: ")
    # 2.2. Read file
    readFile(Filename, Rows) #jump to readFile function, send ref to Rows list as a function parameter
    # 2.3. Analyse rows
    analyseTimestamps(Rows, Results) #jump to analyseTimestamps function, send ref to Rows and Results lists as a fun.par.s
    
    # 2.3. Display results
    displayResults(Results) #jump to the displayResults function, sen reference to Results as a fun.par.
    # 3. Cleanup
    # 3.1. Clear lists
    print("Program ending.")
    return None

main()