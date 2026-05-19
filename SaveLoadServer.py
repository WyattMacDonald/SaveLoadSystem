import time

import zmq
from pathlib import Path
import FileConverter
import StringConverter
#sets the type of Socket we work with

context = zmq.Context()

socket = context.socket(zmq.REP)
socket.bind("tcp://*:5554")




while True:

    message = socket.recv_string()
    if len(message) > 0:
        recieved = message

        try:
            if recieved[0] == 'S':
                path = ""
                inp = ""
                type = ''
                State = 0
                for char in recieved[1:]:

                    if State == 2:
                        inp += char

                    if State == 1:

                        if char == ',':
                            State += 1
                        else:
                            type += char

                    if State == 0:
                        if char == ',':
                            State += 1
                        else:
                            path += char
                output = None
                if type == 'I':
                    output = StringConverter.ConvertToInt(inp)
                if type == 'F':
                    output = StringConverter.ConvertToFloat(inp)
                if type == 'S':
                    output = inp
                if type == 'A':
                    output = StringConverter.ConvertToArray(inp)
                if type == 'C':
                    output = inp

                if type != 'C':
                    FileConverter.addData(path, output)
                else:
                    FileConverter.directlyAddData(path, "C " + str(output))
                socket.send_string("Saved new type")
        except Exception as e:
            print(e)
            socket.send_string("Error: " + str(e))


        try:
            if recieved[0] == 'L':
                path = ""
                for char in recieved[1:]:
                    path += char

                if Path(path).is_file():
                    socket.send_unicode(FileConverter.popLastLine(path))
                else:
                    socket.send_string("Error, no such file exists")
        except Exception as e:
            print(e)
            socket.send_unicode("Error: " + str(e))












zmq.Context().destroy()

