import socket
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()  # Replace 'server_hostname_or_ip' with the actual hostname or IP address of the server
port = 1234
s.connect((host, port))
outp=""

def receive_msg():
    while True:
        outp = s.recv(1024).decode('ascii')
        print(f"Received msg: {outp}")

def send_msg():
    while True:
        text = input().split('\n')[-1]
        s.send(text.encode('ascii'))

# Start the receive and send message threads
threading.Thread(target=receive_msg).start()
threading.Thread(target=send_msg).start()

# Wait for the threads to finish
while True:
    continue

# Close the socket when the user decides to terminate the client
s.close()
