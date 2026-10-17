import socket
import sys


def main():
   host = "127.0.0.1"
   port = 2208


   sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   sock.connect((host, port))
   if len(sys.argv) < 2:
       print("Errore!!! non abbastanza argomenti inseriti")
       return

   stringa = sys.argv[1] + "\n"
   if len(stringa.split(":")) != 2 or stringa.split(":")[0] != "sub":
       print("ERRORE! inserire solamente sub:topic")
       return

   sock.sendall(stringa.encode())

   while True:
       print(sock.recv(1024).decode("utf-8"))


if __name__ == "__main__":
   main()
