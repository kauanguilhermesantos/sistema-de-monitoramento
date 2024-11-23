# Sistema de Monitoramento

Esse sistema foi construído com o objetivo de identificar e mapear as propriedades da máquina. Dessa forma, se quiser testar as funcionalidades desse sistema, siga as seguintes instruções.

# Funcionamento do programa
## Função ``pegaInfoCpu()``

A função ``pegaInfoCpu()`` tem a função de coletar e exibir informações sobre a CPU do sistema da sua máquina.

- ``psutil.cpu_count(logical=True)``: realiza a contagem da quantidade total de núcleos lógicos da CPU.
- ``psutil.cpu_count(logical=False)``: realiza a contagem da quantidade de núcleos físicos da CPU, ignorando os núcleos virtuais.

```python
def pegaInfoCpu():
    nucleosLogicos = psutil.cpu_count(logical=True)
    nucleosFisicos = psutil.cpu_count(logical=False)
    print("CPU:")
    print(f"Núcleos lógicos: {nucleosLogicos}")
    print(f"Núcleos físicos: {nucleosFisicos}\n")
```

## Função ``pegaInfoMemoria()``

A função ``pegaInfoMemoria()`` tem a função de coletar e exibir informações sobre a memória RAM do sistema da sua máquina.

- ``psutil.virtual_memory().total``: Retorna a quantidade total de memória RAM disponível no sistema.
- ``psutil.virtual_memory().used``: Indica a memória em uso.
- ``psutil.virtual_memory().free``: Mostra a quantidade de memória não utilizada e disponível
- ``psutil.virtual_memory().percent``: Indica o percentual da memória usada.

```python
def pegaInfoMemoria():
    memoriaTotal = psutil.virtual_memory().total
    memoriaUsada = psutil.virtual_memory().used
    memoriaLivre = psutil.virtual_memory().free
    memoriaUsadaPercentual = psutil.virtual_memory().percent
    
    print("Memória RAM:")
    print(f"Total: {memoriaTotal / (1024 ** 3):.2f} GB")
    print(f"Usada: {memoriaUsada / (1024 ** 3):.2f} GB")
    print(f"Livre: {memoriaLivre / (1024 ** 3):.2f} GB")
    print(f"Percetual usado: {memoriaUsadaPercentual:.2f} %")
```