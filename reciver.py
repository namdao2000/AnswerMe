import socket

socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
socket.bind(("127.0.0.1", 5000))

while True:
    print("On stand by...")
    packet = socket.recv(500).decode("utf-8")
    print(packet)