from pathlib import Path
import subprocess

script = Path("src/scripts/hijo_pipe.py")

# TODO: crear el proceso con los tres canales conectados y enviar el primer dato.
# TODO: iniciar una segunda instancia para LENTO y gestionar el timeout y la limpieza.

proceso=subprocess.Popen(["python",script], stderr=subprocess.PIPE,stdout=subprocess.PIPE,stdin=subprocess.PIPE,text=True)

salida , error = proceso.communicate(input="DATO|copia|archivo-A.zip",timeout=3)
print("OUT|"+salida.strip())
print("ERR|"+error.strip())
print(f"RC| {proceso.returncode}")


proceso_2=subprocess.Popen(["python",script],stderr=subprocess.PIPE,stdout=subprocess.PIPE,stdin=subprocess.PIPE,text=True)
try:
    salida2 , error2 = proceso_2.communicate(input="LENTO",timeout=0.2)
except subprocess.TimeoutExpired:
    print("TIMEOUT|CONTROLADO")
