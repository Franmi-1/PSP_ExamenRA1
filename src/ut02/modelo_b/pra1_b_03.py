from pathlib import Path
import subprocess

script = Path("src/scripts/hijo_tarea.py")
tareas = [("B-11", 9, False), ("B-12", 4, False), ("B-13", 6, True)]
procesos = []

# TODO: construir y lanzar todos los Popen antes de recoger resultados.
for id, valor, falla in tareas:
    args = ["python", script, "--id", id, "--valor", str(valor), "--retardo-ms", "200"]
    if falla:
        args.append("--fallo")

    procesos.append(subprocess.Popen(
        args,
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    ))

# TODO: recopilar stdout, stderr y returncode; continuar aunque uno falle.

# No me gusta cómo queda pero no se me ocurre otra manera de acceder al id de la tarea
for (id_tarea, _, _), proceso in zip(tareas, procesos):
    salida, error = proceso.communicate(timeout=3)
    if proceso.poll() == 0:
        print(f"{id_tarea}|OK|{salida.strip()}")
    else:
        print(f"{id_tarea}|ERROR|{proceso.poll()}|{error.strip()}")