# Resuelve aquí el ejercicio.
tamanos_kb = [68, 81, 76, 90, 74]

grandes = []
for tamano in tamanos_kb:
    if tamano >= 80:
        grandes.append(tamano)

print(grandes)