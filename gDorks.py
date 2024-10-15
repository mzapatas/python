import webbrowser

def mostrar_menu():
    print("----- Mejores Google Dorks -----")
    print("1. Búsqueda de directorios expuestos en servidores web")
    print("2. Búsqueda de archivos sensibles en servidores web")
    print("3. Búsqueda de documentos confidenciales en servidores web")
    print("4. Búsqueda de cámaras web en línea")
    print("5. Búsqueda de contraseñas en archivos expuestos")
    print("6. Salir")

def abrir_en_navegador(query):
    url = "https://www.google.com/search?q=" + query
    webbrowser.open_new_tab(url)

def buscar_directorios_expuestos():
    abrir_en_navegador("intitle:\"index of\" site:example.com")

def buscar_archivos_sensibles():
    abrir_en_navegador("filetype:log inurl:log")

def buscar_documentos_confidenciales():
    abrir_en_navegador("filetype:pdf site:example.com")

def buscar_camaras_web():
    abrir_en_navegador("inurl:/view/index.shtml")

def buscar_contrasenas():
    abrir_en_navegador("filetype:env intext:DB_PASSWORD")

# Función principal del programa
def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            buscar_directorios_expuestos()
        elif opcion == '2':
            buscar_archivos_sensibles()
        elif opcion == '3':
            buscar_documentos_confidenciales()
        elif opcion == '4':
            buscar_camaras_web()
        elif opcion == '5':
            buscar_contrasenas()
        elif opcion == '6':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, seleccione una opción válida.")

if __name__ == "__main__":
    main()