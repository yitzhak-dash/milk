import socket

target_port = 80
target_host = "www.google.com"

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((target_host, target_port))
client.send("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n".encode('utf-8'))

response = client.recv(4096)

print(response)