def TareaProceso(nombre, duracion):
    def superar_limite(duracion):
        if duracion>=5:
            return True
        else:
            return False
    if superar_limite(duracion):
       print(f"{nombre}: LARGA")
    else:
        print(f"{nombre}: NORMAL") 
TareaProceso("backup", 6.5)
    
    
