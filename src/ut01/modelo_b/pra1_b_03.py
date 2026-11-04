# Resuelve aquí el ejercicio.
class LoteArchivos:
    def __init__(self, nombre, archivos):
        self.nombre = nombre
        self.archivos = archivos

    def resumen():
        return "f{nombre}: {len(archivos)} {archivos}"

LoteArchivos("backup", ["informe.txt", "copi.zip", "datos.csv"])
print(resumen(LoteArchivos))