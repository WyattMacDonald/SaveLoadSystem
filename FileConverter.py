from pathlib import Path
import StringConverter
def readFile(filepath):
    fileR = open(filepath, 'r')
    contents = fileR.read()
    fileR.close()
    return contents

def directlyAddData(filepath, data):
    newFile = False
    emptyFile = False
    fileReadType = 'a'
    newFile = not Path(filepath).is_file()
    if newFile:
        fileReadType = 'x'
    else:
        emptyFile = (readFile(filepath) == "")

    fileW = open(filepath, fileReadType)
    if not newFile and not emptyFile:
        fileW.write("\n")
    fileW.write(data)
    fileW.close()

def addData(filepath, data):

    newFile = False
    emptyFile = False
    fileReadType = 'a'
    newFile = not Path(filepath).is_file()
    if newFile:
        fileReadType = 'x'
    else:
        emptyFile = (readFile(filepath) == "")




    fileW = open(filepath, fileReadType)

    foundEntry = False
    if not newFile and not emptyFile:
        fileW.write("\n")
    if type(data) is int:
        fileW.write("I " + str(data))
        foundEntry = True
    if type(data) is float:
        fileW.write("F " + str(data))
        foundEntry = True
    if type(data) is str:
        fileW.write("S " + str(data))
        foundEntry = True
    if type(data) is bool:
        if data:
            fileW.write("B 1")
        else:
            fileW.write("B 0")
        foundEntry = True
        
    if type(data) is list:
        fileW.write("A ")
        for i in range(len(data)):
            if i != 0:
                fileW.write(",")
            fileW.write(str(data[i]))
        foundEntry = True
    if not foundEntry:
        fileW.write("C "+ str(data))



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
        return None
    stuff = contents[len(contents) - 1]

    if stuff[0] == 'I':
        return StringConverter.ConvertToInt(stuff[2:])
    if stuff[0] == 'F':
        return StringConverter.ConvertToFloat(stuff[2:])
    if stuff[0] == 'S':
        return stuff[2:]
    if stuff[0] == 'B':
        return StringConverter.ConvertToBool(stuff[2:])
    if stuff[0] == 'A':

        return StringConverter.ConvertToArray(stuff[2:])

    return stuff[2:]




