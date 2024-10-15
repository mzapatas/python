import sys
import subprocess

def mostrar_cred():
    perfiles = subprocess.check_output(['netsh','wlan','show','profiles']).decode('utf-8').split('\n')
    print(perfiles)

    nombre_perfiles = []

    for i in perfiles:
        if "Perfil de todos" in i:
            i = i.split(":")
            nombre_perfiles.append(i[1].strip())
    
    for nombre_perfil in nombre_perfiles:
        resultado = subprocess.check_output(['netsh','wlan','show','profile',nombre_perfil,'key=clear']).decode('utf-8').split('\n')
        contrasenas = [linea.split(':')[1].strip() for linea in resultado if 'Contenido de la clave' in linea]
        print(f"{nombre_perfil} - {contrasenas[0] if contrasenas else 'No se encontro contrasena'}")

def main():

    mostrar_cred()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()