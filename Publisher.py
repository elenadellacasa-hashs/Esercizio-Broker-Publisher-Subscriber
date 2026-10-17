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
   if len(stringa.split(":")) != 3 or stringa.split(":")[0] != "pub":
      print("ERRORE! inserire solamente pub:topic:messaggio")
      return
   sock.sendall(stringa.encode())
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
