import psutil
import time
import streamlit as st


# CPU

def pegaInfoCpu():
    nucleosLogicos = psutil.cpu_count(logical=True)
    nucleosFisicos = psutil.cpu_count(logical=False)
    
    return {
        "nucleosLogicos": nucleosLogicos,
        "nucleosFisicos": nucleosFisicos
    }

def pegaInfoMemoria():
    memoriaTotal = psutil.virtual_memory().total
    memoriaUsada = psutil.virtual_memory().used
    memoriaLivre = psutil.virtual_memory().free
    memoriaUsadaPercentual = psutil.virtual_memory().percent

    return {
        "memoriaTotal": memoriaTotal,
        "memoriaUsada": memoriaUsada,
        "memoriaLivre": memoriaLivre,
        "memoriaUsadaPercentual": memoriaUsadaPercentual
    }
    
def listaProcessos():
    st.subheader("Lista de Processos")
    processos = []
    TodosOsProcessos = psutil.pids()
    total = len(TodosOsProcessos)

    progresso = st.progress(0)
    textoStatus = st.empty()

    for i, pid in enumerate(TodosOsProcessos):
        try:
            process = psutil.Process(pid)

            process.cpu_percent(interval=0)
            time.sleep(0.1)

            processos.append({
                "pid": pid,
                "processName": process.name(),
                "status": process.status(),
                "cpu (%)": f"{process.cpu_percent(interval=0):.2f}",
                "memoriaUsada (MB)": f"{process.memory_info().rss / (1024**2):.2f}"
            })

        except (psutil.NoSuchProcess, psutil.AccessDenied):
            pass

        progresso.progress((i+1)/total)
        textoStatus.text(f"Carregando processos... {i+1}/{total}")

    progresso.empty()
    textoStatus.empty()
    
    st.table(processos)

def medeBateria():
    bateria = psutil.sensors_battery()

    if bateria:
        def segundosParaHora(segundos):
            hora, resto = divmod(segundos, 3600)
            minutos, segundo = divmod(resto, 60)

            if hora > 0:
                return f"{hora}h {minutos}min"
            else:
                return f"{minutos}min"

        return{
            "nivelDeBateria": f"{bateria.percent}%",
            "carregando": "Sim" if bateria.power_plugged else "Não",
            "tempoRestante": segundosParaHora(bateria.secsleft)
        }
    else:
        return "Bateria não encontrada."

def main():
    infoCpu = pegaInfoCpu()
    infoMemoria = pegaInfoMemoria()
    infoBateria = medeBateria()

    col1, col2, col3 = st.columns(3)

    with col1:
        with st.container():
            st.subheader("CPU")
            st.write(f"Núcleos Lógicos: {infoCpu['nucleosLogicos']}")
            st.write(f"Núcleos físicos: {infoCpu['nucleosFisicos']}")

    with col2:
        with st.container():
            st.subheader("Memória RAM")
            st.write(f"Total: {infoMemoria['memoriaTotal'] / (1024 ** 3):.2f} GB")
            st.write(f"Usada: {infoMemoria['memoriaUsada'] / (1024 ** 3):.2f} GB")
            st.write(f"Livre: {infoMemoria['memoriaLivre'] / (1024 ** 3):.2f} GB")
            st.write(f"Percetual usado: {infoMemoria['memoriaUsadaPercentual']:.2f} %")

    with col3:
        with st.container():
            st.subheader("Bateria")
            st.write(f"Nível de bateria: {infoBateria['nivelDeBateria']}")
            st.write(f"Carregando: {infoBateria['carregando']}")
            st.write(f"Tempo restante: {infoBateria['tempoRestante']}")

    st.title("Processos do Sistema")
    listaProcessos()

if __name__ == "__main__":
    main()
