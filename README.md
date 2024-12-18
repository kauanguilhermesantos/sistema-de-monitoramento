# Sistema de Monitoramento

Esse sistema foi construído com o objetivo de identificar e mapear as propriedades da máquina. Dessa forma, se quiser testar as funcionalidades desse sistema, siga as seguintes instruções.

``OBS.: Esse script funciona apenas em Windows.``

# Funcionamento do programa
## Função ``pegaInfoCpu()``

A função ``pegaInfoCpu()`` tem a função de coletar e exibir informações sobre a CPU do sistema da sua máquina.

- ``psutil.cpu_count(logical=True)``: realiza a contagem da quantidade total de núcleos lógicos da CPU.
- ``psutil.cpu_count(logical=False)``: realiza a contagem da quantidade de núcleos físicos da CPU, ignorando os núcleos virtuais.

```python
def pegaInfoCpu():
    nucleosLogicos = psutil.cpu_count(logical=True)
    nucleosFisicos = psutil.cpu_count(logical=False)
    
    return {
        "nucleosLogicos": nucleosLogicos,
        "nucleosFisicos": nucleosFisicos
    }
```

## Função ``pegaInfoMemoria()``

A função ``pegaInfoMemoria()`` tem a função de coletar e exibir informações sobre a memória RAM do sistema da sua máquina.

- ``psutil.virtual_memory().total``: retorna a quantidade total de memória RAM disponível no sistema.
- ``psutil.virtual_memory().used``: indica a memória em uso.
- ``psutil.virtual_memory().free``: mostra a quantidade de memória não utilizada e disponível
- ``psutil.virtual_memory().percent``: indica o percentual da memória usada.

```python
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
```

## Função ``listaProcessos()``

A função ``listaProcessos()`` tem a função de listar todos os processos que ocorrem na máquina, exibindo o PID, o nome do processo, o status de execução, percentual de uso da CPU e a quantidade de memória utilizada.

- ``process = psutil.Process(pid)``: mapeia cada processo em execução.
- ``process.name()``: exibe o nome do processo.
- ``process.status()``: exibe o status atual do processo.
- ``process.cpu_percent(interval=0)``: exibe a percentagem de uso da CPU em cada processo.
- ``process.memory_info().rss``: exibe a quantidade de memória utilizada em cada processo.
- ``psutil.NoSuchProcess``: tratamento de exceção, ocorre quando tenta-se acessar informações de um processo que não existe.
- ``psutil.AccessDenied``: tratamento de exceção, ocorre quando o programa tenta acessar informações de um processo que não têm-se permissão suficiente.

```python
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
```

## Função ``medeBateria()``

A função ``medeBateria()`` tem a função de coletar as informações sobre a bateira da máquina.

- ``bateria = psutil.sensors_battery()``: coleta todas as informações da bateria;
- ``bateria.percent``: mostra o percentual da bateria.
- ``bateria.power_plugged``: detecta se o carregador está ligado à máquina.
- ``bateria.secsleft``: calcula o tempo restante da bateria.

```python
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
```