duraciones = [1.2,3.6,2.4,4.1,0.9]
lentas = []

for tiempo in duraciones:
    if tiempo>3.0:
        lentas.append(tiempo)

print(lentas)