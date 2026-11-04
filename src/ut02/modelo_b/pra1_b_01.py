from pathlib import Path
import subprocess

script = Path("src/scripts/hijo_resultado.py")
casos = [("backup-04", "copia.tar"), ("convertir-05", "ERROR")]

# TODO: recorrer los casos, ejecutar el proceso con subprocess.run,
# capturar sus dos canales de salida y examinar returncode.
for id, dato in casos:
    resultado = subprocess.run(
        ["python", script, "--tarea", id, "--dato", dato],
        capture_output=True,
        text=True
    )
    # añado strip para que no hayan saltos de línea
    if resultado.returncode == 0:
        print(f"OK|{resultado.stdout.strip()}")
    else:
        print(f"FALLO|{resultado.returncode}|{resultado.stderr.strip()}")