def taximetro(tiempo_minutos, distancia_km, hora, precio_combustible_litro):
    costo_base = 5
    if hora >= 22 or hora < 6:
        costo_por_km = 800
    else:
        costo_por_km = 600
    
    costo_combustible = (distancia_km / 10) * precio_combustible_litro
    costo_distancia = distancia_km * costo_por_km
    costo_tiempo = tiempo_minutos * 0.1
    costo_total = costo_base + costo_distancia + costo_tiempo + costo_combustible
    return costo_total

tiempo = float(input("Ingresa el tiempo de viaje en minutos: "))
distancia = float(input("Ingresa la distancia recorrida en kilómetros: "))
hora = int(input("Ingresa la hora actual (en formato de 24 horas): "))
precio_combustible = float(input("Ingresa el precio del combustible por litro: "))

costo_viaje = taximetro(tiempo, distancia, hora, precio_combustible)
print(f"El costo total del viaje es: ${costo_viaje}")