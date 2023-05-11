#!/usr/bin/env python3
import socket
import sys

HOST = ""
PORT = 9090

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((HOST, PORT))
sock.listen(1)

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
        print(f"Esperando conexão em {HOST}:{PORT}...")
        (conn, addr) = sock.accept()

        print("Cliente conectado: ", addr)
        while True:
            data = conn.recv(1024)
            text_data = data.decode()
            if text_data == "\quit" or not data:
                break

            print("Recebido: ", text_data)

            if text_data in TRANSLATE_TABLE:
                translated_data = TRANSLATE_TABLE[text_data].encode()
            else:
                translated_data = "Palavra não encontrada.".encode()

            conn.send(translated_data)

        conn.close()
        print("Conexão encerrada.")

    except KeyboardInterrupt:
        print("\nEncerrando servidor...")
        sock.close()
        sys.exit(0)
