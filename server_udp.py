#!/usr/bin/env python3
import socket
import sys

HOST = ""
PORT = 9090

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((HOST, PORT))

TRANSLATE_TABLE = {
    "hospedeiro": "host",
    "rede": "network",
    "protocolo": "protocol",
    "pacote": "packet",
    "roteador": "router",
    "enlace": "link",
    "comutação": "switching",
    "atraso": "delay",
    "fila": "queue",
    "vazão": "throughput",
}

while True:
    try:
        print(f"Esperando mensagem na porta {PORT}...")
        data, client_adress = sock.recvfrom(2048)
        text_data = data.decode()

        print("Recebido: ", text_data)

        if text_data in TRANSLATE_TABLE:
            translated_data = TRANSLATE_TABLE[text_data].encode()
        else:
            translated_data = "Palavra não encontrada.".encode()

        sock.sendto(translated_data, client_adress)

    except KeyboardInterrupt:
        print("\nEncerrando servidor...")
        sock.close()
        sys.exit(0)
