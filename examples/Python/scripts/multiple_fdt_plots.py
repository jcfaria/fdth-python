"""
Mirrored from notebook: Multiple FDT Plots.ipynb
Run with the fdth package installed (pip install fdth or pip install -e .).
"""

# Importações e criação dos dados
import pandas as pd
from fdth import fdt
import matplotlib.pyplot as plt

df = pd.DataFrame({
    'Altura': [170, 175, 180, 165, 172, 168, 175, 170, 160, 155],
    'Peso': [70, 75, 80, 65, 72, 68, 75, 70, 60, 55],
    'Idade': [30, 20, 30, 18, 30, 27, 24, 50, 60, 9],
    'Sexo': ['M', 'I', 'M', 'I', 'M', 'F', 'I', 'F', 'F', 'F']
})

mfdt_by = fdt(df, by="Sexo")


# Histogramas básicos
mfdt_by.plot()


# Polígono
mfdt_by.plot(numeric_type="fp")


# Histograma (frequencia relativa)
mfdt_by.plot(numeric_type="rfh")


# Densidade cumulativa
mfdt_by.plot(numeric_type="cdh")

# Keep plot windows open when running as a script
plt.show()
