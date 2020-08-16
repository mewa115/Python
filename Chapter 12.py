import socket
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # Connect to the socket we created
mysock.connect(('data.pr4e.org', 80))  # Connect to the host using port 80 via earlier created socket
# Below is what we will send to the server. \r\n\r\n Is the action of ENTER. It is the simulation of manual input
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()  # .encode converts unicode internally to UTF-8
# On HTTP the server does the receive first and I do the send first after the connection has been established
mysock.send(cmd)  # Send action

while True:
    data = mysock.recv(512)  # We could receive several packages of data. We allow to receive up to 512 characters.
    if len(data) < 1:  # If we do not receive in response then stop receiving data
        break  # end of transmission
    print(data.decode())  # If did get data we decode it from UTF-8 to unicode format.
mysock.close()  # close the created socket
