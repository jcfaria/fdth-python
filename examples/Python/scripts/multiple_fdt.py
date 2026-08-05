"""
Mirrored from notebook: Multiple FDT.ipynb
Run with the fdth package installed (pip install fdth or pip install -e .).
"""

# Célula 1: Importações e criação dos dados
import pandas as pd
import numpy as np
from fdth import fdt

df = pd.DataFrame({
    'Altura': [170, 175, 180, 165, 172, 168, 175, 170, 160, 155],
    'Peso': [70, 75, 80, 65, 72, 68, 75, 70, 60, 55],
    'Idade': [30, 20, 30, 18, 30, 27, 24, 50, 60, 9],
    'Sexo': ['M', 'I', 'M', 'I', 'M', 'F', 'I', 'F', 'F', 'F']
})


# Célula 2: Criação do MultipleFDT agrupado por Sexo
mfdt_by = fdt(df, by="Sexo")

print("MultipleFDT agrupado por 'Sexo':")
print(mfdt_by)


# Célula 3: Estatísticas básicas por grupo
print("Médias por grupo:\n")
print(mfdt_by.mean())

print("\nMedianas por grupo:\n")
print(mfdt_by.median())

print("\nVariâncias por grupo:\n")
print(mfdt_by.var())

print("\nDesvios padrão por grupo:\n")
print(mfdt_by.sd())


# Célula 4: Valores modais (MFV)
print("Valores Modais (MFV) por grupo:\n")
mfv_result = mfdt_by.mfv()
print(mfv_result)


# Célula 5: Acessando variáveis específicas por grupo
print("Acessando variáveis específicas:")
print("\nAltura por grupo:")
alturas = mfdt_by['Altura']
for grupo, fdt_obj in alturas.items():
    print(f"\nGrupo {grupo}:")
    print(fdt_obj)

print("\n\nIdade por grupo:")
idades = mfdt_by['Idade']
for grupo, fdt_obj in idades.items():
    print(f"\nGrupo {grupo}:")
    print(fdt_obj)


# Célula 6: Quartis por grupo
print("Quartis (0.25, 0.5, 0.75) por grupo:")
quartis = mfdt_by.quantile([0.25, 0.5, 0.75])
print(quartis)


# Célula 7: Percentis específicos
print("Percentis 10, 50, 90 por grupo:")
percentis = mfdt_by.quantile([10, 50, 90], by=100)
print(percentis)


# Célula 8: Testando com dados categóricos
print("Testando com dados categóricos:")
cat_data = pd.DataFrame({
    'Cor': ['Vermelho', 'Azul', 'Verde', 'Azul', 'Vermelho', 'Verde', 'Azul', 'Vermelho'],
    'Tamanho': ['P', 'M', 'G', 'M', 'P', 'G', 'M', 'P'],
    'Grupo': ['A', 'A', 'B', 'B', 'A', 'B', 'A', 'B']
})

mfdt_cat = fdt(cat_data, by="Grupo")
print("FDT Categórico agrupado:")
print(mfdt_cat)

print("\nMFV categórico:")
print(mfdt_cat.mfv())
