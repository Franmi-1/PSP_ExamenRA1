# Resuelve aquí el ejercicio.

class LoteArchivos:
    def __init__(self,nombre:str,archivos:list):
        self.nombre = nombre
        self.archivos = archivos

    def resumen(self):
        print(f"{self.nombre}: {len(self.archivos)} archivos")


LoteArchivos("backup",["informe.txt","copia.zip","datos.csv"]).resumen()