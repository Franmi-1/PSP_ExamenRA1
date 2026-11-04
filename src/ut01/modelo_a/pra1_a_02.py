# Resuelve aquí el ejercicio.

def calcular_media(duraciones):

    res=0

    for numeros in duraciones:

       res=res+numeros

    resultado_final=res/len(duraciones)

    return resultado_final

duraciones=[2.0, 3.0, 4.0]

resultado=calcular_media(duraciones)

print(f"Media: {resultado:.1f}")