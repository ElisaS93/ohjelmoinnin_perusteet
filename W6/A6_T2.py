def writeFile(PFilename, PContent) -> None:
    Filehandle = open(PFilename, 'w')
    Filehandle.write(PContent)
    Filehandle.close()
    return None

def main() -> None:
    print("Program starting.")
    FirstName = input("Insert first name: ")
    LastName = input("Insert last name: ")
    FileName = input("Insert file name: ")
    Content = "{}\n{}".format(FirstName, LastName)
    writeFile(FileName, Content)
    print("Program ending.")
    return None

if __name__ == "__main__":
    main()

#valmis