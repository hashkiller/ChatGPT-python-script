import socket
import sys

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('localhost', 10000)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)

# Scan the ports from 1 to 1024
for port in range(1, 1025):
    try:
        print('Scanning port {}'.format(port))
        sock.sendall(str(port).encode())

        # Receive data from the server
        data = sock.recv(1024)
        print(data)
    except:
        print('Connection error')
        sys.exit()

# Close the socket
sock.close()
