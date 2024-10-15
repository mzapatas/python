import webbrowser
import os
from tkinter import *

def menu():
    os.system('cls')
    print("*** CURSO DE PROGRAMACION EN PYTHON\n")
    print("1. Que son los algoritmos")
    print("2. Introducción a Python")
    print("3. Tipos de datos, Variables, Operadores")
    print("4. Control de flujos, IF, WHILE, FOR, BOOLEAN, ETC")
    print("5. Funciones, DEF, PASS, RETURN, SCOPE, ETC")
    print("6. Funciones Integradas, STR, INT, FLOAT, BOOL, ETC\n")
    print("** P. ORIENTADA A OBJETOS\n")
    print("7. Conceptos, POO, Clase, Atributos, Metodos")
    print("8. Clases, Abstracción, Encapsulación, Herencia, Polimorfismo")
    print("9. Módulos, Sentencias, Namespace, Math, Random")
    print("0. Salir\n")

def main():
    while True:
        menu()
        op = input("Escriba la opción numeral: ")

        if op == "1":
            webbrowser.open_new('https://youtu.be/swpAfyZFt-8?si=1sZaTHWSCOMwXu8S')
        elif op == "2":
            webbrowser.open_new('https://youtu.be/YJiU79ZaLCM?si=1SeecOF_dzq94zjh')
        elif op == "3":
            webbrowser.open_new('https://youtu.be/numQzIgpOo0?si=NblpxafqfHA3zl3x')
        elif op == "4":
            webbrowser.open_new('https://youtu.be/w53HiWSZnzU?si=uvWXfXnpCDmRI_H2')
        elif op == "5":
            webbrowser.open_new('https://youtu.be/9k91jETchkI?si=rUv82J83hlz9tgN2')
        elif op == "6":
            webbrowser.open_new('https://youtu.be/hHhkLEnowLA?si=3eli6pgVb2RGY_6-')
        elif op == "7":
            webbrowser.open_new('https://youtu.be/SI7O81GMG2A?si=vwsB8ol7YJLnW4XY')
        elif op == "8":
            webbrowser.open_new('https://youtu.be/JVNirg9qs4M?si=JoP71yE459F8yxml')
        elif op == "9":
            webbrowser.open_new('https://youtu.be/hWbD_6xhYe0?si=dKVR_bP2aHYxg4ho')
        elif op == "0":
            print("\nAdiós!\n")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.\n")
            os.system('pause')
if __name__ == "__main__":
    main()
