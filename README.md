# Save and Load Microservice
The Save and Load Microservice is a mini tool used to save and load data into readable text files. it is very simple to use

# Saving:
saving is pretty easy to do as you need to submit a string that is built like this:

```
 "S,[filepath],[inputType],[input]"
```
for example it can be something like this:
```
"S,testpath/testfolder/test.txt,F,200.4"
```
the reason why there needs to be a S at front is because thats the basic command to save something

code example:
```
#sets the type of Socket we work with to send requests to the server
Socket = zmq.Context().socket(zmq.REQ)
#connects to the computers server on port 5555
Socket.connect("tcp://localhost:5554")

filename = input("Enter filename: ")
currentPythonPath = str(Path(__file__).resolve().parent)

filePath = str(currentPythonPath) + "/"  + filename + ".txt"
newname = input("Enter your name: ")
Socket.send_string("S," + filePath + ",S," + newname)

```
list of variable types:
```
I = Integer
F = Floating point number
B = bool
S = String
C = custom
A = array type. when converting it will also have a letter in front for the data it holds
```

# Loading:
loading is pretty straight forward you need to submit a string like this:

```
"L,[filePath]"
```
and example:
```
"L,testpath/testfolder/test.txt"
```
The reason why we need a L in front is because that is the main command
once you send this you will recive the unicode for the last data put into the file which you will have to decode

code example along with a instance of reciving the data:
```
#sets the type of Socket we work with to send requests to the server
Socket = zmq.Context().socket(zmq.REQ)
#connects to the computers server on port 5555
Socket.connect("tcp://localhost:5554")

filename = input("Enter filename: ")
currentPythonPath = str(Path(__file__).resolve().parent)

filePath = str(currentPythonPath) + "/"  + filename + ".txt"
newname = input("Enter your name: ")
Socket.send_string("L," + filePath)
#calling socet.recv().decode() will be the only thing you will have to do to grab your data
name = Socket.recv().decode()
```

diagram: 
<img width="1898" height="1134" alt="image" src="https://github.com/user-attachments/assets/f2024e17-7380-4852-bbe7-a0e612aa086a" />



