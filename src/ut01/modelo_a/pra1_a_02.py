# Resuelve aquí el ejercicio.
def calcula_media(duraciones):
    suma_total = sum(duraciones)
    cantidad = len(duraciones)
    return suma_total/cantidad

resultado = calcula_media([2.0,3.0,4.0])
print(f"Media: {resultado:.1f}")