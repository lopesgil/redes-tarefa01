#!/usr/bin/env python3
import socket

HOST = "localhost"
PORT = 9090

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((HOST, PORT))
print("Conectado ao servidor.")

while True:
    msg = input("Digite sua mensagem: ")
    sock.sendall(msg.encode())
    if msg == "\quit":
        break
    data = sock.recv(1024)
    print("Tradução: ", data.decode())

sock.close()
print("Conexão encerrada.")
