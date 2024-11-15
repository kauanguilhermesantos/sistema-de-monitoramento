import psutil
from tabulate import tabulate

def get_cpu_info():
    print(f"Quantidade de núcleos (físicos): {psutil.cpu_count(logical=False)}")
    print(f"Quantidade de núcleos (lógicos): {psutil.cpu_count(logical=True)}\n")

def get_memory_info():
    memory = psutil.virtual_memory()
    print("Memória RAM:")
    print(f"  Total: {memory.total / 1e9:.2f} GB")
    print(f"  Usada: {memory.used / 1e9:.2f} GB")
    print(f"  Livre: {memory.available / 1e9:.2f} GB\n")

def get_process_list():
    processes = []
    for proc in psutil.process_iter(['pid', 'name', 'memory_info']):
        try:
            mem_info = proc.info['memory_info']
            processes.append([proc.info['pid'], proc.info['name'], mem_info.rss / 1e6])
        except (psutil.NoSuchProcess, psutil.AccessDenied):
            continue
    print(tabulate(processes, headers=["PID", "Nome", "Memória Usada (MB)"], tablefmt="pretty"))

def get_process_details(pid):
    try:
        proc = psutil.Process(pid)
        print(f"Detalhes do processo {pid}:")
        print(f"  Nome: {proc.name()}")
        print(f"  Status: {proc.status()}")
        print(f"  Tempo de execução: {proc.create_time()}")
        print(f"  Memória usada: {proc.memory_info().rss / 1e6:.2f} MB")
    except psutil.NoSuchProcess:
        print(f"Processo com PID {pid} não encontrado.")
    except psutil.AccessDenied:
        print(f"Acesso negado ao processo com PID {pid}.")

def get_battery_info():
    battery = psutil.sensors_battery()
    if battery:
        print("Informações da bateria:")
        print(f"  Nível de bateria: {battery.percent}%")
        print(f"  Carregando: {'Sim' if battery.power_plugged else 'Não'}")
    else:
        print("Informações de bateria não disponíveis.\n")

def main():
    print("Informações do Computador\n")
    get_cpu_info()
    get_memory_info()
    print("Lista de Processos:")
    get_process_list()
    print("\nDigite o PID de um processo para detalhes (ou 'sair' para finalizar):")
    while True:
        pid_input = input("PID: ")
        if pid_input.lower() == "sair":
            break
        elif pid_input.isdigit():
            get_process_details(int(pid_input))
        else:
            print("Entrada inválida. Digite um número válido ou 'sair'.")
    get_battery_info()

if __name__ == "__main__":
    main()
