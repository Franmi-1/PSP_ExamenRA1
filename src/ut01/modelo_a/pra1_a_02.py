

def calcular_media(duraciones):
    media1 = 0
    acum = 0
    for num in duraciones:
        media1 += num
        acum +=1
    media = media1/acum
    print(f"Media: {media}")

duracion = [2.0,3.0,4.0]

calcular_media(duracion)

