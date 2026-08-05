"""
Mirrored from notebook: Numerical FDT Plots.ipynb
Run with the fdth package installed (pip install fdth or pip install -e .).
"""

# ### Imports

import numpy as np
import pandas as pd
from fdth import fdt
import matplotlib.pyplot as plt


dados = [1, 3, 2, 10, 20, 32, 35, 38, 39, 48, 51, 50, 3, 45, 3, 2, 1, 3, 23, 3, 22, 17, 19, 25]
fd = fdt(dados)


# absolute frequency histogram
fd.plot(type_="fh")


# absolute frequency polygon
fd.plot(type_="fp")


# relative frequency histogram
fd.plot(type_="rfh")


# relative frequency polygon
fd.plot(type_="rfp")


# relative frequency (%) histogram
fd.plot(type_="rfph")


# relative frequency (%) polygon
fd.plot(type_="rfpp")


# density
fd.plot(type_="d")


# cumulative density histogram
fd.plot(type_="cdh")


# cumulative density polygon
fd.plot(type_="cdp")


# cumulative frequency histogram
fd.plot(type_="cfh")


# cumulative frequency polygon
fd.plot(type_="cfp")


# cumulative frequency (%) histogram
fd.plot(type_="cfph")


# cumulative frequency (%) polygon
fd.plot(type_="cfpp")

# Keep plot windows open when running as a script
plt.show()
