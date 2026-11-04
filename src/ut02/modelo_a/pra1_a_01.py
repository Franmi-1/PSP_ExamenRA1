from pathlib import Path
import subprocess

script = Path("src/scripts/hijo_resultado.py")
casos = [("exportar-01", "paquete.zip"), ("convertir-02", "ERROR")]

# TODO: recorrer los casos, ejecutar el proceso con subprocess.run,
# capturar sus dos canales de salida y examinar returncode.


for id, texto in casos:

    subproceso=subprocess.run(["python", script, "--tarea", id, "--dato", texto], capture_output=True, text=True)


    if subproceso.returncode==0:
        
        print(f"|OK|{subproceso.stdout}")
    else:
        
        print(f"|FALLO|{subproceso.returncode}|{subproceso.stderr}")
