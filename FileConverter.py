from pathlib import Path

def readFile(filepath):
    fileR = open(filepath, 'r')
    contents = fileR.readlines()
    fileR.close()
    return contents
def addData(filepath, data):

    newFile = False
    fileReadType = 'a'
    newFile = not Path(filepath).is_file()
    if newFile:
        fileReadType = 'x'


    fileW = open(filepath, fileReadType)
    if not newFile:
        fileW.write("\n")
    if type(data) is int:
        fileW.write("I " + str(data))
    if type(data) is float:
        fileW.write("F " + str(data))
    if type(data) is str:
        fileW.write("S " + str(data))
    if type(data) is bool:
        if data:
            fileW.write("B 1")
        else:
            fileW.write("B 0")

        
    if type(data) is list:
        fileW.write("A " + str(data))

    fileW.close()
def popLastLine(filepath):
    fileR = open(filepath, 'r')
    contents = fileR.readlines()

    fileR.close()
    fileW = open(filepath, 'w')

    newtext = ""
    for line in contents[:-1]:
        newtext += line
    fileW.write(newtext)
    fileW.close()
    if len(contents) <= 0:
        return "N"
    return contents[len(contents) - 1]



addData("SaveStates/Test.txt", True)
