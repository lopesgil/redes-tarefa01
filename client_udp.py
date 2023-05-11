#!/usr/bin/env python3
import socket

HOST = "localhost"
PORT = 9090

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    msg = input("Digite sua mensagem: ")
    sock.sendto(msg.encode(), (HOST, PORT))
    if msg == "\quit":
        break
    data, server_adress = sock.recvfrom(2048)
    print("Tradução: ", data.decode())

sock.close()
print("Conexão encerrada.")
