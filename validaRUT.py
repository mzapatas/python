def validar_rut(rut):
    rut = rut.replace(".", "").replace("-", "").lower()
    if len(rut) < 2:
        return False
    rut_sin_dv = rut[:-1]
    dv = rut[-1]
    
    if not rut_sin_dv.isdigit():
        return False
    
    suma = 0
    multiplicador = 2
    
    for i in range(len(rut_sin_dv) - 1, -1, -1):
        suma += int(rut_sin_dv[i]) * multiplicador
        multiplicador = 2 if multiplicador == 7 else multiplicador + 1
    
    resto = suma % 11
    dv_calculado = 11 - resto if resto != 0 else 0
    
    if dv == 'k':
        dv = '10'
    return str(dv_calculado) == dv

# Ejemplo de uso
while(True):
    rut = input("(+) Ingrese RUN para validar (para salir: 0)\n=> ")
    if rut == "0":
        break   
    elif validar_rut(rut):
        print("El RUT es válido.\n")
    else:
        print("El RUT no es válido.\n")