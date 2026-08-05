"""
Mirrored from notebook: Measures of dispersion.ipynb
Run with the fdth package installed (pip install fdth or pip install -e .).
"""

# ### Imports

import numpy as np
from fdth import fdt


# # FDT Standard Deviation and Variance Testing
# Este caderno demonstra o uso dos metodos FDT para calcular o desvio-padrão e a variância a partir de tabelas de distribuição de frequência e séries de dados padrão.
# Exploraremos diferentes exemplos para diversos casos de uso envolvendo cálculos de desvio-padrão e variância.

# ### FDT Standard Deviation Testing
# Esta seção demonstra o cálculo da variância das tabelas de distribuição de frequência usando o metodo `.sd()`.

# Teste 1
dados = [10, 12, 15, 20, 22, 25, 25, 30, 35, 40]
# Executando o teste
print('Teste 1 (Desvio Padrão):', fdt(dados).sd())


# Teste 2
data_test2 = fdt([0, 1, 3, 2, 6, 3, 8, 9, 4])
# Executando o teste
print('Teste 2 (Desvio Padrão):', data_test2.sd())


# ### FDT Variance Testing
# Esta seção demonstra o cálculo da variância das tabelas de distribuição de frequência usando o metodo `.var()`.

# Dados para o teste
dados = [10, 12, 15, 20, 22, 25, 25, 30, 35, 40]
# Executando o teste
print('Teste 1 (Variância):', fdt(dados).var())


# Dados para o teste
data_test2 = fdt([0, 1, 3, 2, 6, 3, 8, 9, 4])
# Executando o teste
print('Teste 2 (Variância):', data_test2.var())
