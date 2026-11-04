from pathlib import Path
import subprocess

script = Path("src/scripts/hijo_tarea.py")
tareas = [("B-11", 9, False), ("B-12", 4, False), ("B-13", 6, True)]
procesos = []

# TODO: construir y lanzar todos los Popen antes de recoger resultados.
# TODO: recopilar stdout, stderr y returncode; continuar aunque uno falle.
for id_tarea, valor, fallo in tareas:
     comandosh=["python",script,"--id",id_tarea,"--valor",str(valor),"--retardo-ms", "200"]
if fallo:
     