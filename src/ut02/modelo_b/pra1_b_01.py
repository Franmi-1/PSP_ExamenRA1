from pathlib import Path
import subprocess

script = Path("src/scripts/hijo_resultado.py")
casos = [("backup-04", "copia.tar"), ("convertir-05", "ERROR")]

# TODO: recorrer los casos, ejecutar el proceso con subprocess.run,
# capturar sus dos canales de salida y examinar returncode.

for id, texto in casos:
    result = subprocess.run(["python", script, "--tarea", id, "--dato", texto], capture_output=True, text=True)
    if result.returncode == 0:
        print(f'OK|{result.stdout}')
    else:
        print(f'FALLO|{result.returncode}|{result.stderr}')