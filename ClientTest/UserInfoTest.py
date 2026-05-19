import os
from pathlib import Path

import zmq





#sets the type of Socket we work with to send requests to the server
Socket = zmq.Context().socket(zmq.REQ)
#connects to the computers server on port 5555
Socket.connect("tcp://localhost:5554")

filename = input("Enter filename: ")
currentPythonPath = str(Path(__file__).resolve().parent)

print(currentPythonPath)



filePath = str(currentPythonPath) + "/testStates/"  + filename + ".txt"

if Path(filePath).is_file():
    Socket.send_string("L"+filePath)

    name = Socket.recv().decode()
    if name != "Error, no such file exists":
        print("Ah welcome: " + name)

    else:
        print(name)


else:
    newname = input("Enter your name: ")
    Socket.send_string("S" + filePath + ",S," + newname)




