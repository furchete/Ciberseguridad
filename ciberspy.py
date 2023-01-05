'''
hostname = socket.gethostname dice el nombre de tu ordenador para activar la funcion print + hostname
ip print + ip 
'''

import sys
import socket

hostname = socket.gethostname()
ip = socket.gethostbyname(hostname)

print("El nombre de tu ordenador es: " + hostname)
print("Tu direccion IP es " + ip)
