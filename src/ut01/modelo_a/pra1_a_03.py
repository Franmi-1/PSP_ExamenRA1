# Resuelve aquí el ejercicio.
class TareaProceso:
    def __init__(self,nombre,duracion):
        self.nombre=nombre
        self.duracion=duracion

    def supera_limite(self):
        if self.duracion >=5.0:
              return True
        else:
              return False

tarea=TareaProceso("backup",6.5)

if tarea.supera_limite():
        estado="LARGA"
else:
        estado="NORMAL"
print(f"{tarea.nombre}: {estado}")
