import socket
# import time
import pickle


HEADERSIZE = 10

# A socket is an endpoint that recieves data
# socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Tuple of IP and Port
s.bind((socket.gethostname(), 1235))
s.listen(5)

while True:
    # accept all incomming connections
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established")

    d = {1: "HEY", 2: "There"}
    msg = pickle.dumps(d)

    # Fixed length header
    msg = bytes(f'{len(msg): < {HEADERSIZE}}', "utf-8") + msg

    # send information to client socket
    clientsocket.send(msg)
