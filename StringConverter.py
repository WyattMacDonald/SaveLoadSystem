'''
main converter for the save load system
current things to convert:

I = Integer
F = Floating point number
B = bool
S = String
C = custom
A = array type. when converting it will also have a letter in front for the data it holds
N = None, usaually used for when a file is empty or for requested file reading is non existant

'''

def ConvertToInt(input):
    return int(input)
def ConvertToFloat(input):
    return float(input)
def ConvertToBool(input):
    if input == '0':
        return False
    else:
        return True

def ConvertStringToVariable(input):

    type = 'I'

    for char in input:
        if char == '.':
            type = 'F'
        if not char.isdigit():
            type = 'S'

    if type == 'I':
        return ConvertToInt(input)
    elif type == 'F':
        return ConvertToFloat(input)
    elif type == 'S':
        return input





def ConvertToArray(input):
    output = []
    currentString = ""
    for char in input:
        if char == ',':
            #converter
            output.append(ConvertStringToVariable(currentString))
            currentString = ""

        else:
            currentString += char
    return output
