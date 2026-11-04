# Resuelve aquí el ejercicio.
def nombres_en_mayusculas(nombres):
    lista = []
    for nombre in nombres:
        lista.append(nombre.upper())
    print(lista)

nombres_en_mayusculas(['informe.txt','copia.zip','datos.csv'])