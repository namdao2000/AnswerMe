import socket
socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
message = "Hello world!"
socket.sendto(message.encode(), ("127.0.0.1", 5000))