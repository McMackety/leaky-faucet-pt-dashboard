import socket
import serial
import threading

port = '/dev/tty.usbmodem14401'
baud = 115200

bind_ip = '0.0.0.0'
bind_port = 7997

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip, bind_port))
server.listen(5)

print('Listening on {}:{}'.format(bind_ip, bind_port))


def handle_client_connection_write(client_socket, ser):
    while True:
        try:
            ser.write(client_socket.recv(1024))
        except BlockingIOError:
            continue

def handle_client_connection_read(client_socket, ser):
    while True:
        client_socket.send(ser.readline())


while True:
    client_sock, address = server.accept()
    client_sock.setblocking(False)
    print('Accepted connection from {}:{}'.format(address[0], address[1]))
    ser = serial.Serial(port, baud)
    client_handler1 = threading.Thread(
        target=handle_client_connection_write,
        args=(client_sock,ser,)
    )
    client_handler2 = threading.Thread(
        target=handle_client_connection_read,
        args=(client_sock,ser,)
    )
    client_handler1.start()
    client_handler2.start()