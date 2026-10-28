import socket
import sys


def main():

   if len(sys.argv) < 3:
       print("Errore!!! non abbastanza argomenti inseriti. Formattazione corretta: python nome_file.py indirizzo_broker:porta_broker pub:topic:message")
       return

   broker = sys.argv[1].split(":")
   addr = str(broker[0])
   port = int(broker[1])

   sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   sock.connect((addr, port))

   stringa = sys.argv[2] + "\n"
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
