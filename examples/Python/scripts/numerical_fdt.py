"""
Mirrored from notebook: Numerical FDT.ipynb
Run with the fdth package installed (pip install fdth or pip install -e .).
"""

#. Imports
import pandas as pd
import numpy as np
from fdth import fdt, Binning

#.. Function Testing
# Este caderno demonstra o uso das funções FDT para gerar tabelas de distribuição de frequência e sumarizar dados em diferentes formatos.
# Exploraremos diferentes exemplos para diversos casos de uso, incluindo quadros de dados, matrizes e séries de dados personalizadas.

#.. Default Testing
# Os testes a seguir demonstram como usar a função `fdt`, incluindo diferentes métodos de cálculo de classes, como Freedman-Diaconis, Sturges e intervalos fixos.

#... Test 1
# Testa o método de cálculo de classes usando a regra de Freedman-Diaconis ('FD').
dados = np.array([2, 5, 7, 10, 12, 15, 18])
resultado = fdt(dados, binning=Binning.from_fd)
print(resultado)

#... Teste 2
# Testa a criação de uma tabela de frequência definindo um número fixo de classes (k=4).
dados = np.array([3, 6, 9, 12, 15, 18, 21])
resultado = fdt(dados, k=4)
print(resultado)

#... Teste 3
# Testa o uso de valores iniciais (start) e finais (end) personalizados para a tabela.
dados = np.array([1, 4, 7, 10, 13, 16, 19])
resultado = fdt(dados, start=0, end=20)
print(resultado)

#... Teste 4
# Testa a especificação de um intervalo fixo (h=8) para as classes, com limites iniciais e finais definidos.
dados = np.array([10, 15, 20, 25, 30, 35, 40])
resultado = fdt(dados, start=10, end=50, h=8)
print(resultado)

#... Teste 5
# Testa o comportamento da função ao encontrar valores ausentes (None) no array, com remove_nan=False.
try:
    dados = np.array([2, None, 8, 10, None, 18])
    resultado = fdt(dados, kind="numerical", remove_nan=False)
    print(resultado)
except ValueError as e:
    print('Erro:', e)


#... Teste 6
# Testa se a função detecta inconsistências nos parâmetros (k e h definidos simultaneamente).
try:
    dados = np.array([1, 2, 3, 4])
    resultado = fdt(dados, start=1, end=5, k=2, h=1)
    print(resultado)
except ValueError as e:
    print('Erro:', e)


#.. Matrix Testing
# Os exemplos a seguir mostram o uso de `fdt`, que calcula tabelas de distribuição de frequência a partir de matrizes usando diferentes métodos de cálculo de classe.

#... Matriz de entrada para teste
data_matrix = np.array([
    [1, 10],
    [2, 20],
    [3, 30],
    [4, 40],
    [5, 50]
])

# Teste com um número especificado de classes
result_k3 = fdt(data_matrix, k=3)
print(result_k3)

#.. Multiple Testing
# Esta seção testa a função `fdt` que manipula múltiplas séries de dados e calcula a tabela de distribuição de frequência.

#... Teste 1
x_uniform = pd.Series([10, 15, 20, 25, 30, 35, 40])
result_uniform_python = fdt(
    data=x_uniform,
    binning=Binning.from_sturges,
    right=False,
    remove_nan=True
)
print(result_uniform_python)
print(result_uniform_python.binning)


#... Test 1: A simple DataFrame with a single numeric column
df1 = pd.DataFrame({
    'A': [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
})
result1 = fdt(df1)
print(result1)


#... Test 2: A DataFrame with two numeric columns
df2 = pd.DataFrame({
    'A': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'B': [11, 9, 8, 7, 6, 5, 4, 3, 2, 1]
})
print('\nTest 2 (without grouping):')
result2 = fdt(df2)
print(result2)


#.. Simple Testing
# A função `fdt` nos permite calcular uma tabela de distribuição de frequência para intervalos simples.

#... Teste 1: Intervalos básicos
x = np.array([5, 10, 15, 20, 25, 30, 35])
start = 0
end = 40
h = 10
print('Test 1 - Basic intervals')
print(fdt(x, start=start, end=end, h=h))
