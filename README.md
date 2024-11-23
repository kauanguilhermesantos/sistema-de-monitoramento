# Sistema de Monitoramento

Esse sistema foi construído com o objetivo de identificar e mapear as propriedades da máquina. Dessa forma, se quiser testar as funcionalidades desse sistema, siga as seguintes instruções.

# Funcionamento do programa
## Função ``pegaInfoPcu()``

A função ``pegaInfoCpu()`` tem a função de coletar e exibir informações sobre a CPU do sistema da sua máquina.

- O trecho ``psutil.cpu_count(logical=True)`` é utilizada para realizar a contagem da quantidade total de núcleos lógicos da CPU.
- O trecho ``psutil.cpu_count(logical=False)`` é utilizada para realizar a contagem da quantidade de núcleos físicos da CPU, ignorando os núcleos virtuais.

```python
def pegaInfoCpu():
    nucleosLogicos = psutil.cpu_count(logical=True)
    nucleosFisicos = psutil.cpu_count(logical=False)
    print("CPU:")
    print(f"Núcleos lógicos: {nucleosLogicos}")
    print(f"Núcleos físicos: {nucleosFisicos}\n")
```