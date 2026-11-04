from pathlib import Path
import subprocess

script = Path("src/scripts/hijo_pipe.py")

# TODO: crear el proceso con los tres canales conectados y enviar el primer dato.
# TODO: iniciar una segunda instancia para LENTO y gestionar el timeout y la limpieza.

subproceso=subprocess.Popen(["python", script], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

salida, error= subproceso.communicate(input="DATO|copia|archivo-A.zip",timeout=3)

print(f"OUT|{salida.strip()}")
print(f"ERR{error.strip()}")
print(f"RC|{subproceso.returncode}")


subproceso_secundario=subprocess.Popen(["python",script],stderr=subprocess.PIPE,stdout=subprocess.PIPE, stdin=subprocess.PIPE, text=True)



