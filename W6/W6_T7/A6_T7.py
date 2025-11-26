LOWER_ALPHABETS = "abcdefghijklmnopqrstuvwxyz"
UPPER_ALPHABETS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
DELIMITER = ';'

def readFile(PFilename) -> str:
    Content = ''
    FileHandle = open(PFilename, 'r')
    Row = FileHandle.readline()
    while Row != '':
        Content += Row
        Row = FileHandle.readline()
    FileHandle.close()
    return Content

def writeFile() -> None:
    return None

def appendToFile() -> None:
    return None

def rot() -> str:
     newContent = ''
     return newContent

def getLocation(locationId):
    Location = "unknown"
    if locationId == 1:
        Location = "Galpa's palace"
    elif locationId== 2:
        Location = "Ohto's palace"
    elif locationId == 3:
        Location = "Vetellius' palace"
    elif locationId == 4:
        Location = "Vespasian's palace"
    elif locationId == 0:
        Location = "home"
    return Location

def main() -> None:
    print("Travel starting.")
    PlayerProgressFilename = "player_progress.txt"
    Progress = readFile(PlayerProgressFilename)
    LastProgress = Progress.strip().split('\n')[-1].split(DELIMITER)
    CurrentLocationId = int(LastProgress[0])
    CurrentLocation = getLocation(CurrentLocationId)
    NextLocationId = int(LastProgress[1])
    NextLocation = getLocation(NextLocationId)
    PassPhrase = LastProgress[2]
    print(f"Currently at {CurrentLocation}.")
    print(f"Travelling to {NextLocation}...")
    print(f"...Arriving to the {NextLocation}.")
    print("Passing the guard at the entrance.")
    return None

main()