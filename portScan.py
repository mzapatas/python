import sys
import socket
from datetime import datetime

def main():
    ip = "10.1.1.2"
    p_min = int(input("Puerto desde: "))
    p_max = int(input("Puerto hasta: "))

    print("-"*50)
    print("La IP es: "+ip)
    print("Inicio de escaneo "+str(datetime.now()))
    print("-"*50)

    for puerto in range(p_min,p_max):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((ip,puerto))

        if result == 0:
            print("(+) El puerto {} se encuentra abierto".format(puerto))
        else:
            print("No encontro nada.")
        s.close()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()