"""
Mirrored from notebook: Categorical FDT.ipynb
Run with the fdth package installed (pip install fdth or pip install -e .).
"""

#. Imports
import numpy as np
import pandas as pd
from fdth import fdt

#.. fdt
# A função `fdt` calcula tabelas de distribuição de frequência para vetores ou DataFrames, considerando tanto dados categóricos quanto numéricos. Ela permite análise de frequência simples, com a opção de ordenação e agrupamento.

x1 = ['A', 'B', 'A', 'C', 'B', 'B', 'C', 'A', 'C', 'C']
x2 = ['X', 'Y', 'X', 'Z', 'Y', 'Y', 'Z', 'Z', 'Z', 'Z']
x3 = ['Red', 'Blue', 'Green', 'Red', 'Green', 'Blue', 'Blue', 'Green']

#... Test 1
print('Test 1')
print(fdt(x1,
          sort=True,
          decreasing=True))  # Ordena da maior p/ menor frequência

#... Test 2
print('\nTest 2')
print(fdt(x2,
          sort=False,
          decreasing=False)) # Não ordena, mantém a ordem original

#... Test 3
print('\nTest 3')
print(fdt(x3,
          sort=True,
          decreasing=False))  # Ordena alfabeticamente (crescente)


# Essa função é usada para gerar tabelas de frequência para um DataFrame contendo dados categóricos. Ela permite a análise de distribuições de categorias nas colunas do DataFrame, com ou sem agrupamento, e possibilita a ordenação dos resultados.

#... Test 1: Sem agrupamento
# Verifica a geração de tabelas de frequência para um DataFrame com colunas categóricas,
# sem considerar agrupamento. Ordena os resultados de forma decrescente.

df1 = pd.DataFrame({
    'col1': pd.Categorical(['A', 'B', 'A', 'C', 'C']),
    'col2': pd.Categorical(['X', 'X', 'Y', 'X', 'Y'])
})

result1 = fdt(df1,
              sort=True,
              decreasing=True)
print(result1)


#... Test 2: Com agrupamento
# Avalia a funcionalidade da função ao agrupar os dados por uma coluna específica ('group'),
# criando tabelas de frequência para as colunas categóricas dentro de cada grupo.
# Ordena os resultados de forma crescente.

df2 = pd.DataFrame({
    'group': pd.Categorical(['G1', 'G1', 'G2', 'G2', 'G2']),
    'col1': pd.Categorical(['A', 'B', 'A', 'C', 'C']),
    'col2': pd.Categorical(['X', 'X', 'Y', 'X', 'Y'])
})

result2 = fdt(df2,
              sort=True,
              decreasing=False) # ordena os resultados em ordem crescente
print(result2)


#... Test 3: Com coluna numérica
# Testa a função em um DataFrame que contém colunas categóricas e uma coluna numérica.
# Gera tabelas de frequência para todas as colunas.
# Não realiza ordenação nas tabelas.

df3 = pd.DataFrame({
    'col1': pd.Categorical(['A', 'B', 'A', 'C', 'C']),
    'col2': pd.Categorical(['X', 'X', 'Y', 'X', 'Y']),
    'col3': [1, 2, 3, 4, 5]  # Numeric column
})

result3 = fdt(df3)
print(result3)


# Essa função gera tabelas de distribuição de frequência a partir de matrizes contendo dados categóricos. Ela oferece a capacidade de realizar a análise em várias colunas e de organizar os resultados de maneira ordenada.

#... Test 1: Verifica a criação de tabelas de distribuição de frequência
# para uma matriz de categorias distintas distribuídas igualmente
# em várias colunas. Ordena os resultados em ordem decrescente.

x = np.array([
    ['A', 'B', 'C'],
    ['A', 'B', 'C'],
    ['B', 'A', 'C'],
    ['C', 'A', 'B']
])

df = pd.DataFrame(x,
                  columns=['Col1', 'Col2', 'Col3']) # Cria uma matriz com valores categóricos.

res = fdt(df,
          sort=True,
          decreasing=True) # Ordena os resultados de forma decrescente
print(res)

#... Test 2: Testa a criação de tabelas de distribuição de frequência
# para uma matriz com valores homogêneos (mesmas categorias em todas
# as colunas e linhas). Ordena os resultados em ordem decrescente.

x = np.array([
    ['X', 'Y', 'Z'],
    ['X', 'Y', 'Z'],
    ['X', 'Y', 'Z'],
    ['X', 'Y', 'Z']
])

df = pd.DataFrame(x,
                  columns=['Col1', 'Col2', 'Col3'])

res = fdt(df,
          sort=True,
          decreasing=True)
print(res)

#... Test 3: Avalia a criação de tabelas de frequência para uma matriz
# com categorias variadas em cada coluna. Ordena os resultados em
# ordem crescente.

x = np.array([
    ['Dog', 'Cat', 'Fish'],
    ['Dog', 'Dog', 'Bird'],
    ['Cat', 'Cat', 'Fish'],
    ['Fish', 'Dog', 'Bird']
])

df = pd.DataFrame(x, columns=['Col1', 'Col2', 'Col3'])

res = fdt(df,
          sort=True,
          decreasing=False)
print(res)


# Essa função também permite criar múltiplas tabelas de frequência para conjuntos de dados categóricos. Ela é útil quando se deseja gerar distribuições de frequência para vários vetores ou séries de dados ao mesmo tempo, oferecendo flexibilidade para ajustes nos intervalos e agrupamentos.

# ...Test Data 1
data = {
    'col1': ['A', 'B', 'A', 'C', 'B', 'B', 'C', 'A', 'C', 'C'],
    'col2': ['X', 'Y', 'X', 'Z', 'Y', 'Y', 'Z', 'Z', 'Z', 'Z']
}

df = pd.DataFrame(data)
df['col1'] = df['col1'].astype('category')
df['col2'] = df['col2'].astype('category')

# Execute Test 1
result = fdt(df,
             sort=True,
             decreasing=True)
print(result)

#... Test Data 2
data = {
    'col1': ['Red', 'Blue', 'Red', 'Green', 'Blue', 'Blue', 'Green', 'Red', 'Green', 'Green'],
    'col2': ['Dog', 'Cat', 'Dog', 'Bird', 'Cat', 'Cat', 'Bird', 'Bird', 'Bird', 'Bird'],
    'col3': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]  # Non-categorical
}

df = pd.DataFrame(data)
df['col1'] = df['col1'].astype('category')
df['col2'] = df['col2'].astype('category')

#... Execute Test 2
result = fdt(df) # Calcula a distribuição de frequência sem ordenação
print(result)

#... Test Data 3
data = {
    'col1': ['Apple', 'Apple', 'Banana', 'Banana', 'Banana', 'Grape', 'Grape', 'Apple', 'Apple', 'Grape'],
    'col2': ['Small', 'Small', 'Large', 'Large', 'Large', 'Small', 'Small', 'Large', 'Large', 'Large'],
    'col3': ['Low', 'Low', 'High', 'High', 'High', 'Medium', 'Medium', 'Low', 'Low', 'Medium']
}

df = pd.DataFrame(data)
df['col1'] = df['col1'].astype('category')
df['col2'] = df['col2'].astype('category')
df['col3'] = df['col3'].astype('category')

#... Execute Test 3
result = fdt(df,
             sort=True,
             decreasing=False)
print(result)
