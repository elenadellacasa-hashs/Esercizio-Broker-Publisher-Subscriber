import socket
import sys


def main():
    if len(sys.argv) < 3:
        print(
            "Errore!!! non abbastanza argomenti inseriti. Formattazione corretta: python nome_file.py indirizzo_broker:porta_broker sub:topic")
        return

    broker = sys.argv[1].split(":")
    addr = str(broker[0])
    port = int(broker[1])

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect((addr, port))

    stringa = sys.argv[2] + "\n"
    if len(stringa.split(":")) != 2 or stringa.split(":")[0] != "sub":
        print("ERRORE! inserire solamente sub:topic")
        return

    sock.sendall(stringa.encode())

    try:
        while True:
            print(sock.recv(1024).decode("utf-8"))
    except KeyboardInterrupt:
        print("interruzione da tastiera")
        sock.close()

if __name__ == "__main__":
    main()
