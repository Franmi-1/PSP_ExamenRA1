from pathlib import Path
import subprocess

script = Path("src/scripts/hijo_pipe.py")

# TODO: crear el proceso con los tres canales conectados y enviar el primer dato.
proceso = subprocess.Popen(
    [script],
    stdin = subprocess.PIPE,
    stdout= subprocess.PIPE,
    stderr= subprocess.PIPE,
    text=True
    )

salida, _ = proceso.communicate(script)

# TODO: iniciar una segunda instancia para LENTO y gestionar el timeout y la limpieza.
