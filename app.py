import psutil
import time

# CPU

def pegaInfoCpu():
    nucleosLogicos = psutil.cpu_count(logical=True)
    nucleosFisicos = psutil.cpu_count(logical=False)
    print("CPU:")
    print(f"Núcleos lógicos: {nucleosLogicos}")
    print(f"Núcleos físicos: {nucleosFisicos}\n")

def pegaInfoMemoria():
    memoriaTotal = psutil.virtual_memory().total
    memoriaDisponivel = psutil.virtual_memory().available
    memoriaUsada = psutil.virtual_memory().used
    memoriaLivre = psutil.virtual_memory().free
    memoriaUsadaPercentual = psutil.virtual_memory().percent
    
    print("Memória RAM:")
    print(f"Total: {memoriaTotal / (1024 ** 3):.2f} GB")
    # print(f"Disponível: {memoriaDisponivel / (1024 ** 3):.2f} GB")
    print(f"Usada: {memoriaUsada / (1024 ** 3):.2f} GB")
    print(f"Livre: {memoriaLivre / (1024 ** 3):.2f} GB")
    print(f"Percetual usado: {memoriaUsadaPercentual:.2f} %")
    
def pegaListaDeProcessos():
    for pid in psutil.pids():
        try:
            process = psutil.Process(pid)

            process.cpu_percent(interval=0)
            time.sleep(0.1)

            print(f"PID: {pid} | Nome: {process.name()} | Status: {process.status()} | CPU: {process.cpu_percent(interval=0):.2f}% | Memória usada: {process.memory_info().rss / (1024 ** 2):.2f} MB")    
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass

pegaInfoCpu()
pegaInfoMemoria()
pegaListaDeProcessos()