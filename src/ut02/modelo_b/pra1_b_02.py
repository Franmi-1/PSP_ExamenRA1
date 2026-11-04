from pathlib import Path
import subprocess

script = Path("src/scripts/hijo_pipe.py")

# TODO: crear el proceso con los tres canales conectados y enviar el primer dato.
# TODO: iniciar una segunda instancia para LENTO y gestionar el timeout y la limpieza.
proceso = subprocess.Popen(["python",script],stdin=subprocess.PIPE, stdout=subprocess.PIPE,stderr=subprocess.PIPE,text=True)


salida, err= proceso.communicate(input="DATO|RECIBIDO|conversion|archivo-B.zip",timeout=3)
print(f"OUT|{salida.strip()}")
print(f"ERR|{err.strip()}")
print(f"RC|{proceso.returncode}")
proceso.terminate()

proceso2=subprocess.Popen(["python",script],stdin=subprocess.PIPE,stdout=subprocess.PIPE,stderr=subprocess.PIPE, text=True)
try:
    salida, err= proceso2.communicate("LENTO", timeout=0.2)
except subprocess.TimeoutExpired:
    proceso2.kill()
    proceso2.communicate()
    print("TIMEOUT|CONTROLADO")



