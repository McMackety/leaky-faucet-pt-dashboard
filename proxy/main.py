import socket
import serial
import threading

port = 'COM2'
baud = 115200

bind_ip = '0.0.0.0'
bind_port = 7997

ser = serial.Serial(port, baud)

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip, bind_port))
server.listen(5)

print('Listening on {}:{}'.format(bind_ip, bind_port))


def handle_client_connection(client_socket):
    while True:
        client_socket.send(ser.read(1024))

while True:
    client_sock, address = server.accept()
    print('Accepted connection from {}:{}'.format(address[0], address[1]))
    client_handler = threading.Thread(
        target=handle_client_connection,
        args=(client_sock,)
    )
    client_handler.start()