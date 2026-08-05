"""
Mirrored from notebook: Measures of central tendency and position.ipynb
Run with the fdth package installed (pip install fdth or pip install -e .).
"""

# ### Imports

import numpy as np
from fdth import fdt


# # FDT Central Tendency and Position
#
# Este caderno demonstra o uso dos metodos FDT para calcular a média, a mediana e a moda a partir de tabelas de distribuição de frequência e séries de dados padrão.
#
# Exploraremos diferentes exemplos para diversos casos de uso, incluindo cálculos de média, mediana e moda.
#
# Além disso, também exploraremos a medida de posição do quantil.
#
# ### FDT Mean Testing
# Esta seção demonstra o cálculo da média usando o metodo `.mean()`.

# Dados para o 1° teste
data_test1 = fdt([1, 5, 3, 8, 10, 5.1, 3.2, 9.1, 8])
# Executando o teste
print('Teste 1:', data_test1.mean())


# Dados para o 2° teste
data_test2 = fdt([0,1,3,2,6,3,8,9,4])

# Executando o teste
print('Teste 2:', data_test2.mean())


# ### FDT QUANTILE Testing
# Esta seção demonstra o uso do método `.quantile()` para estimar valores posicionais com base na distribuição de frequências dos dados agrupados.

dados = fdt([1, 2, 3, 4, 5, 6, 7, 8, 9])

# O primeiro tercil do conjunto de dados.
print("Teste 1:", dados.quantile(1, by=3))

# O quantil 0.5 é equivalente à mediana.
print("Teste 2:", dados.quantile(0.5))

# O segundo quartil (índice 1 nos quartiles abaixo)
quartiles = np.arange(0, 1, 0.25)
print("Teste 3:", dados.quantile(1, by=quartiles))

# Mostrando todos os decis
print("Teste 4:")
for i in range(10):
    print(f"  {i}º decil: {dados.quantile(i, by=10):.4f}")


# ### FDT Median Testing
#
# Esta seção demonstra o cálculo da mediana a partir de tabelas de distribuição de frequência usando o metodo `.median()`.

# Dados de exemplo
dados = [10, 12, 15, 20, 22, 25, 25, 30, 35, 40]

# Criar uma tabela de frequências agrupada (fdt)
tabela_fdt = fdt(dados)

# Visualizar o resultado
print(tabela_fdt)

# Calcular a mediana
mediana = tabela_fdt.median()
print('A mediana é:', mediana)


# ### FDT Mode Testing
# Esta seção demonstra o cálculo do modo usando o metodo `.mfv()`. Exploraremos vários casos com diferentes padrões de dados.

# Conjunto de dados com uma única moda
data1 = [1, 2, 2, 3, 4]
moda = fdt(data1).mfv()
print('A moda de data1 é:', moda)


# Conjunto de dados com múltiplas modas
data2 = [1, 1, 2, 2, 3]
moda2 = fdt(data2).mfv()
print('A moda de data2 é:\n ', moda2)


# Conjunto de dados onde todos os valores são únicos
data3 = [1, 2, 3, 4, 5]
moda3 = fdt(data3).mfv()
print('A moda de data3 é:', moda3)


# Conjunto de dados onde todos os valores são iguais
data4 = [2, 2, 2, 2, 2]
moda4 = fdt(data4).mfv()
print('A moda de data4 é:', moda4)


# Conjunto de dados com valores não numéricos
data5 = ['a', 'b', 'b', 'c']
moda5 = fdt(data5).mfv()
print('A moda de data5 é:', moda5)


# Conjunto de dados com valores não numéricos
data5 = ['a', 'b', 'b', 'c', 'c']
moda5 = fdt(data5).mfv()
print('A moda de data5 é:\n', moda5)
