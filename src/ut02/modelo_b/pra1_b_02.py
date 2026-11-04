from pathlib import Path
import subprocess

script = Path("src/scripts/hijo_pipe.py")

# TODO: crear el proceso con los tres canales conectados y enviar el primer dato.
# TODO: iniciar una segunda instancia para LENTO y gestionar el timeout y la limpieza.

proceso = subprocess.Popen(
    ["python", script],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True
)

salida, error = proceso.communicate(input="DATO|conversion|archivo-B.zip", timeout=3)
print(f"OUT|{salida.strip()}")
print(f"ERR|{error.strip()}")
print(f"RC|{proceso.poll()}")

proceso_lento = subprocess.Popen(
    ["python", script],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True
)

try:
    salida, error = proceso_lento.communicate(input="LENTO", timeout=0.2)
except subprocess.TimeoutExpired:
    print("TIMEOUT|CONTROLADO")