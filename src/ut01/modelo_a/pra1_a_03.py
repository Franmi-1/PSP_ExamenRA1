# Resuelve aquí el ejercicio.

class TareaProceso:
    
    def __init__(self, nombre, duracion):

        self.nombre=nombre
        self.duracion=duracion

    def supera_limite(self):

        if self.duracion>=5.0:

            return True
        
        else:

            return False

resultado=TareaProceso("backup", 6.5)

if resultado.supera_limite==True:

    print("backup: LARGA")

else:

    print("backup: NORMAL")



