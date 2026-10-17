import socket


def main():
   host = "127.0.0.1"
   port = 2208


   sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   sock.connect((host, port))


   topic = input("Inserire il topic: ")
   sock.sendall((f"sub:{topic}\n").encode())


   while True:


       print(sock.recv(1024).decode("utf-8"))


if __name__ == "__main__":
   main()
