import socket


def main():
   host = "127.0.0.1"
   port = 2208


   sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   sock.connect((host, port))


   topic = input("Inserire il topic: ")
   messaggio = input("Inserire il messaggio: ")
   sock.sendall((f"pub:{topic}:{messaggio}\n").encode())
   messaggio = readLine(sock).decode("utf-8")
   if messaggio == "SI":
      print("Messaggio inviato correttamente")
   elif messaggio == "NO":
      print("Il topic inserito non esiste")

def readLine( sk):
   data = b''
   while (b'\n' not in data):
      data += sk.recv(1024)
      if not data: return b''
   return data.strip()


if __name__ == "__main__":
   main()
