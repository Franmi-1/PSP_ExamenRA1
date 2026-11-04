# Resuelve aquí el ejercicio.
def nombres_en_mayusculas(nombres):
    resultado = []
    for nombre in nombres:
        resultado.append(nombre.upper())
    return resultado

print(nombres_en_mayusculas(["informe.txt", "copia.zip", "datos.csv"]))