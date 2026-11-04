from pathlib import Path
import subprocess

script = Path("src/scripts/hijo_pipe.py")

proceso = subprocess.Popen(
    ["python",script],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True
)

salida = proceso.communicate(input="DATO|copia|archivo-A.zip")
proceso.wait(3.0)
print(salida)
proceso.terminate()

proceso2 = subprocess.Popen(
    ["python",script],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    text=True
)
try:
    input = proceso2.communicate(input="LENTO")
except subprocess.TimeoutExpired:
    print("TIMEOUT|CONTROLADO")


