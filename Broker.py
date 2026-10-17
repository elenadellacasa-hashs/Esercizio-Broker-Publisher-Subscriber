import threading
import socket

class BrokerThreading(threading.Thread):
   def __init__(self, client, addr, diz):
       super().__init__()
       self.sock = client
       self.addr = addr
       self.dizionario = diz







def Main():
   host = ''
   port = 2208
   dizionario = {"meteo": []}


   sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
   sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
   sock.bind((host, port))


   sock.listen(5)


   print('Broker started.')


   while True:
       client, addr = sock.accept()
       print ('client connected ip:<' + str(addr) + '>')
       thread = BrokerThreading(client, addr, dizionario)
       thread.daemon = True
       thread.start()
   client.close()


if __name__ == '__main__':
   Main()
