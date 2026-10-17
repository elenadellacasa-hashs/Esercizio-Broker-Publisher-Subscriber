import socket


def main():
   host = "127.0.0.1"
   port = 2208


   sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   sock.connect((host, port))


   topic = input("Inserire il topic: ")
   messaggio = input("Inserire il messaggio: ")
   sock.sendall((f"pub:{topic}:{messaggio}\n").encode())


def readLine(self, sk):
   data = b''
   while (b'\n' not in data):
      data += sk.recv(1024)
      if not data: return b''
   return data.strip()


if __name__ == "__main__":
   main()
