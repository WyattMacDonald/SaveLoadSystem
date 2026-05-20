import os
import random
import time
from pathlib import Path

import zmq





#sets the type of Socket we work with to send requests to the server
Socket = zmq.Context().socket(zmq.REQ)
#connects to the computers server on port 5555
Socket.connect("tcp://localhost:5554")

filename = input("Enter filename: ")
currentPythonPath = str(Path(__file__).resolve().parent)

filePath = str(currentPythonPath) + "/testStates/"  + filename + ".txt"

if Path(filePath).is_file():

    Socket.send_string("L," + filePath)
    pos = Socket.recv_string()

    Socket.send_string("L,"+filePath)
    age = Socket.recv_string()

    Socket.send_string("L," + filePath)
    name = Socket.recv_string()
    if name != "Error, no such file exists":

        print("Ah welcome: " + name)
        print("You are currently: " + str(age) + " years old")
        print("Random Position: " + pos)

        time.sleep(2)
        Socket.send_string("S," + filePath + ",S," + name)
        Socket.recv()
        Socket.send_string("S," + filePath + ",I," + str(age))
        Socket.recv()

        x = random.randint(-200, 200)
        y = random.randint(-200, 200)
        Socket.send_string("S," + filePath + ",C," + str((x, y)))

    else:
        print(name)


else:
    newname = input("Enter your name: ")
    Socket.send_string("S," + filePath + ",S," + newname)
    Socket.recv()
    newAge = input("Enter new age: ")

    Socket.send_string("S," + filePath + ",I," + str(newAge))

    Socket.recv()

    x = random.randint(-200, 200)
    y = random.randint(-200, 200)
    Socket.send_string("S," + filePath + ",C," + str((x,y)))




