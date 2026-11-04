# Resuelve aquí el ejercicio.
duraciones = [2.0, 3.0, 4.0]
def calcular_media(duraciones):
    calcular_media = [float(duraciones.strip()) for duraciones in duraciones]
    media = sum(calcular_media) / len(calcular_media)

    print(f"Media: {media:.2f}")
