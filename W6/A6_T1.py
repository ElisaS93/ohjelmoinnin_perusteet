# Create a program that can read a text file and then print the file content. User must be able to specify the file name. Decorate the beginning and the end of the file with a decorative line.

# Decorative lines

# #### START "{filename}" ####
# #### END "{filename}" ####

# Program starting.
# This program can read a file.
# Insert filename: A6_T1_D1.txt
# #### START "A6_T1_D1.txt" ####
# Hello
# World

# #### END "A6_T1_D1.txt" ####
# Program ending.



def readFile(Filename):
    Filehandler = open(Filename, 'r')
    Content = ''
    Row = Filehandler.readline()
    while Row != '':
        Content += Row
        Row = Filehandler.readline()
    Filehandler.close()
    return Content #palaa takaisin kutsukohtaan

def main() -> None:
    print("Program starting.")
    print("This program can read a file.")
    Filename = input("Insert filename: ")
    FileContent = readFile(Filename) #hyppää readFile funktioon
    print("### START \"{}\" ###".format(Filename))   #tekee saman asian kuin f-string print(f"### START {Filename} ###")
    print(FileContent)
    print("### END \"{}\" ###".format(Filename))
    print("Program ending.") 

if __name__ == "__main__":
    main()

    #valmis