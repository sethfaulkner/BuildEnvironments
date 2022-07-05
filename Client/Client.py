
import socket

while(input("Send Message? (y/n)").lower() != 'n'):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    print(local_ip)
    sock.connect((local_ip, 11000))
    sock.send(b"Hello There!<EOF>")
    sock.recv(4096)
    sock.close()
