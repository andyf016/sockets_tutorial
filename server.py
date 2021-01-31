import socket

HEADERSIZE = 10

# A socket is an endpoint that recieves data
# socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Tuple of IP and Port
s.bind((socket.gethostname(), 1235))
s.listen(5)

while True:
    # accpt all incomming connections
    clientsocket, address = s.accept()
    print(f"Connection from {address} has been established")

    msg = "Welcome to the Server"
    # Fixed length header
    msg = f'{len(msg): < {HEADERSIZE}}' + msg

    # send information to client socket
    clientsocket.send(bytes(msg, "utf-8"))
   
