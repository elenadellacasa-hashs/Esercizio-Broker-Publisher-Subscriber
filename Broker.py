import threading
import socket


class BrokerThreading(threading.Thread):
    def __init__(self, client, addr, diz):
        super().__init__()
        self.sock = client
        self.addr = addr
        self.dizionario = diz

    def readLine(self, sk):
        data = b''
        while (b'\n' not in data):
            data += sk.recv(1024)
            if not data: return b''
        return data.strip()

    def run(self):
        messaggio = self.readLine(self.sock).decode('utf-8')
        msg = messaggio.split(":")
        if msg[0] == "sub":
            topic = msg[1]
            if topic in self.dizionario.keys():
                self.dizionario[topic].append(self.sock)
                print("Client aggiunto al topic")
            else:
                self.dizionario[topic] = []
                self.dizionario[topic].append(self.sock)

        elif msg[0] == "pub":
            topic = msg[1]
            mess = msg[2].encode('utf-8')
            print("publisher!")
            if topic in self.dizionario.keys():
                self.sock.sendall("SI\n".encode())
                for sock in self.dizionario[topic]:
                    sock.sendall(mess)
            else:
                self.sock.sendall("NO\n".encode())

        print(self.dizionario)


def Main():
    host = ''
    port = 2208
    dizionario = {}

    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
    sock.bind((host, port))

    sock.listen(5)

    print('Broker started.')

    try:
        while True:
            client, addr = sock.accept()
            print('client connected ip:<' + str(addr) + '>')
            thread = BrokerThreading(client, addr, dizionario)
            thread.daemon = True
            thread.start()
    except KeyboardInterrupt:
        print("interruzione da tastiera, chiusura della connessione")
    finally:
        sock.close()


if __name__ == '__main__':
    Main()
