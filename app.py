import psutil

# CPU

def pegaInfoCpu():
    nucleosLogicos = psutil.cpu_count(logical=True)
    nucleosFisicos = psutil.cpu_count(logical=False)
    print("CPU:")
    print(f"Núcleos lógicos: {nucleosLogicos}")
    print(f"Núcleos físicos: {nucleosFisicos}")

def pegaInfoMemoria():
    memoria = psutil.virtual_memory()
    
    print("Memória")
    print(memoria)

pegaInfoCpu()
pegaInfoMemoria()