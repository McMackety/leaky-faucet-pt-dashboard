import socket
import threading
import time
import math

def generateDigit(j):
    return math.sin(j + time.time()) * 500
testDigit = str(100)
printout = testDigit.encode()

bind_ip = '0.0.0.0'
bind_port = 7997

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip, bind_port))
server.listen(5)

print('Listening on {}:{}'.format(bind_ip, bind_port))


def handle_client_connection(client_socket):
    while True:
        for j in range(0, 8):
            client_socket.send(str(abs(round(generateDigit(j), 2))).encode() + b',')
        client_socket.send(b'\n')
        time.sleep(0.1)

while True:
    client_sock, address = server.accept()
    print('Accepted connection from {}:{}'.format(address[0], address[1]))
    client_handler = threading.Thread(
        target=handle_client_connection,
        args=(client_sock,)
    )
    client_handler.start()