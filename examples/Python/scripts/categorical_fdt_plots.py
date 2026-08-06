"""
Mirrored from notebook: Categorical FDT Plots.ipynb
Run with the fdth package installed (pip install fdth or pip install -e .).
"""

#. Imports
import numpy as np
import pandas as pd
from fdth import fdt
import matplotlib.pyplot as plt

dados = ["Carro", "Moto", "Moto", "Bicicleta", "Carro", "Caminhão", "Moto", "Carro", "Bicicleta", "Iate", "Iate", "Moto", "Ônibus"]
fd = fdt(dados)

# bar plot with frequencies
fd.plot(type_="fb")

# polygon plot with frequencies
fd.plot(type_="fp")

# dot chart with frequencies
fd.plot(type_="fd")

# pareto plot with cumulative frequencies
fd.plot(type_="pa")

# bar plot with relative frequencies
fd.plot(type_="rfb")

# polygon plot with relative frequencies
fd.plot(type_="rfp")

# dot chart with relative frequencies
fd.plot(type_="rfd")

# bar plot with relative frequencies in %
fd.plot(type_="rfpb")

# polygon plot with relative frequencies in %
fd.plot(type_="rfpp")

# dot chart with relative frequencies in %
fd.plot(type_="rfpd")

# bar plot with cumulative frequencies
fd.plot(type_="cfb")

# polygon plot with cumulative frequencies
fd.plot(type_="cfp")

# dot chart with cumulative frequencies
fd.plot(type_="cfd")

# bar plot with cumulative frequencies in %
fd.plot(type_="cfpb")

# polygon plot with cumulative frequencies in %
fd.plot(type_="cfpp")

# dot chart with cumulative frequencies in %
fd.plot(type_="cfpd")

# Keep plot windows open when running as a script
plt.show()
