from pathlib import Path
import subprocess

script = Path("src/scripts/hijo_pipe.py")

# TODO: crear el proceso con los tres canales conectados y enviar el primer dato.
# TODO: iniciar una segunda instancia para LENTO y gestionar el timeout y la limpieza.

proceso = subprocess.Popen(["python",script], stdin=subprocess.PIPE, stderr=subprocess.PIPE,stdout=subprocess.PIPE,text=True)

re1, re2 = proceso.communicate(input="DATO|conversion|archivo-B.zip",timeout=3)
print(re1)
print(re1)
print(proceso.returncode)
try: 
    res1,res2 = proceso.communicate(input="LENTO",timeout=0.2)
except subprocess.TimeoutExpired:
    print("TIMEOUT|CONTROLADO")