def taximetro(tiempo_minutos, distancia_km, hora):
    costo_base = 5
    if hora >= 22 or hora < 6:
        costo_por_km = 850
    else:
        costo_por_km = 650
    
    costo_distancia = distancia_km * costo_por_km
    costo_tiempo = tiempo_minutos * 0.1
    costo_total = costo_base + costo_distancia + costo_tiempo
    return costo_total

tiempo = float(input("Ingresa el tiempo de viaje en minutos: "))
distancia = float(input("Ingresa la distancia recorrida en kilómetros: "))
hora = int(input("Ingresa la hora actual (en formato de 24 horas): "))

costo_viaje = taximetro(tiempo, distancia, hora)
print(f"El costo total del viaje es: ${costo_viaje}")