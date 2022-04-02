import socket
import re

my_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
my_sock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
my_sock.send(cmd)

data = my_sock.recv(512)
message = data.decode()
header_end_pos = message.find('\r\n\r\n') + 4

print(message[header_end_pos:], end='')
characters = message[header_end_pos:].__len__()

while data.__len__() > 0:                                 
    data = my_sock.recv(512)
    dec = data.decode()
    if(3000 < characters + dec.__len__()):
        if(characters < 3000):
            print(dec[0: 3000 - characters], end='')
    else:
        print(dec, end = '')
    characters += dec.__len__()
print('\nCharacters:', characters)
my_sock.close()

