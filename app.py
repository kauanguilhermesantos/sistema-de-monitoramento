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
    
def listaProcessos():
    for pid in psutil.pids():
        try:
            process = psutil.Process(pid)

            process.cpu_percent(interval=0)
            time.sleep(0.1)

            print(f"PID: {pid} | Nome: {process.name()} | Status: {process.status()} | CPU: {process.cpu_percent(interval=0):.2f}% | Memória usada: {process.memory_info().rss / (1024 ** 2):.2f} MB")    
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass

def medeBateria():
    bateria = psutil.sensors_battery()

    if bateria:
        print(f"Nível de bateria: {bateria.percent}%")
        print(f"Carregando: {"Sim" if bateria.power_plugged else "Não"}")

        def segundosParaHora(segundos):
            hora, resto = divmod(segundos, 3600)
            minutos, segundo = divmod(resto, 60)

            if hora > 0:
                return f"{hora}h {minutos}min"
            else:
                return f"{minutos}min"

        print(f"Tempo restante: {segundosParaHora(bateria.secsleft)}")

pegaInfoCpu()
pegaInfoMemoria()
listaProcessos()
medeBateria()