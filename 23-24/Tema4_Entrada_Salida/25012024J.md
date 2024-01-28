# Clase 25012024.md

## Hoy veremos

* Creación de sockets cliente/servidor
* envío de ficheros entre cliente/ servidor


## Cliente

``` python

import os
import socket

HOST = "localhost"
PORT =  9999

client = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

file = open("./imagen.png", 'rb')
data = file.read()

client.sendall (data)
client.send(b"<END>")

file.close()
client.close()

```

## Servidor

Al servidor le llega un fichero y lo crea y lo genera en el servidor.

``` python
import socket

HOST = "localhost"
PORT = 9999

server = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen()

client, addr = server.accept()
file = open("imagen.jpg", "wb")
file_bytes = b""

done = False

while not done:
    data = client.recv(1024)
    if file_bytes [-5:] == b"<END>":
        done = True
    else:       
        file_bytes += data

file.write(file_bytes) 
file.close ()
client.close()
server.close()
