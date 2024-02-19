
#server
import socket
import threading

client_list = list()


def on_new_client(clientsocket, addr):
    while True:
        try:
            msg = clientsocket.recv(1024).decode('ascii')
            if not msg:
                break
            for client in client_list:
                if client[0] != clientsocket:
                    messg = "<" + str(addr[1]) + "> " + str(msg)
                    client[0].send(messg.encode('ascii'))
            if msg == "Goodbye":
                break
        except ConnectionResetError:
            break
    clientsocket.close()
    client_list.remove((clientsocket, addr))

serversocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

host = socket.gethostname()
port = 1234

serversocket.bind((host,port))
serversocket.listen(5)
print("Server listening...")

while True:
    clientsocket,addr=serversocket.accept()
    client_list.append((clientsocket,addr))
    print("Got connection from %s"%str(addr))
    threading._start_new_thread(on_new_client,(clientsocket,addr))
    
   


  
