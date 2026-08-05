# fdth

**Frequency distribution tables, histograms, and polygons** for numerical and
categorical data in Python.

A feature-complete port of the [fdth](https://github.com/jcfaria/fdth) R package
([CRAN](https://cran.r-project.org/package=fdth)).

```text
pip install fdth
```

Package page: [pypi.org/project/fdth](https://pypi.org/project/fdth/) · Release notes: [NEWS.md](NEWS.md)

Alternative installs (source / repo wheel):

```text
pip install git+https://github.com/jcfaria/fdth-python.git
pip install https://github.com/jcfaria/fdth-python/raw/main/dist/fdth-1.0.0-py3-none-any.whl
```

Canonical repository: [github.com/jcfaria/fdth-python](https://github.com/jcfaria/fdth-python)

---

## Features

- Frequency distribution tables (**FDT**) from lists, NumPy arrays, and pandas objects
- Numerical and categorical variables, plus multi-column / grouped tables
- Histograms and frequency polygons (absolute, relative, cumulative)
- Summary measures from grouped data (mean, median, mode, quantiles, variance, …)
- Grouping with multiple keys via `by=` (beyond the original R single-key limit)

Requires **Python 3.10+**. Depends on `pandas`, `numpy`, and `matplotlib`.

---

## Quick start

```python
from fdth import fdt

data = [1, 5, 8, 3, 12, 7, 4, 9]
table = fdt(data)
print(table)
table.plot()
```

`fdt()` detects the data type and returns `NumericalFDT`, `CategoricalFDT`, or
`MultipleFDT` as appropriate.

---

## Grouped example

Build FDTs for every column, split by several grouping variables, and plot:

```python
import pandas as pd
from fdth import fdt

df = pd.DataFrame({
    "Height": [170, 175, 180, 165, 172, 168, 175, 170, 160, 155],
    "Weight": [70, 75, 80, 65, 72, 68, 75, 70, 60, 55],
    "Age": [30, 20, 30, 18, 30, 27, 24, 50, 60, 9],
    "Sex": ["M", "I", "M", "I", "M", "F", "I", "F", "F", "F"],
    "Region": [
        "Northeast", "Southeast", "Northeast", "Southeast", "North",
        "North", "Southeast", "Northeast", "North", "Southeast",
    ],
    "MaritalStatus": [
        "Married", "Single", "Single", "Married", "Single",
        "Single", "Married", "Married", "Single", "Married",
    ],
})

mfdt = fdt(df, by=["Sex", "MaritalStatus", "Region"])
mfdt.plot(numeric_type="fh", categorical_type="fb")
```

**Page 1**

<img width="1588" height="802" alt="Grouped FDT plots — page 1" src="https://github.com/user-attachments/assets/7dbc6c71-8c40-438f-83dc-83e2ba94849f" />

**Page 2**

<img width="1599" height="811" alt="Grouped FDT plots — page 2" src="https://github.com/user-attachments/assets/68852616-0e8f-4174-8c92-2fd15f82f320" />

More notebooks and mirrored `.py` scripts live under [`examples/Python`](examples/Python).
Comparable R examples are under [`examples/R`](examples/R).

---

## Development

```sh
git clone https://github.com/jcfaria/fdth-python.git
cd fdth-python

python -m venv venv
# Linux / macOS:  source venv/bin/activate
# Windows CMD:    venv\Scripts\activate.bat
# Windows PS:     venv\Scripts\Activate.ps1

pip install -e ".[dev]"
```

| Task | Command |
|------|---------|
| Tests | `python -m unittest discover -s tests` |
| Format | `black .` |
| Type check | `mypy --strict --cache-fine-grained .` |
| API docs | `pdoc -o doc fdth` |
| Build | `python -m build` |

A short Git tutorial in Portuguese is available in [HelpGit.md](HelpGit.md).

---

## Background

This package is a **collective Python port** of the R **fdth** library,
developed at **UESC** (Computer Science — Probability and Statistics) with
successive student cohorts and earlier community ports. The object-oriented
design solidified over that collaborative work. The public reference
repository is [jcfaria/fdth-python](https://github.com/jcfaria/fdth-python);
version **1.0.0** is on [PyPI](https://pypi.org/project/fdth/).

---

## Credits

**Original R package** — [jcfaria/fdth](https://github.com/jcfaria/fdth)

- [José Cláudio Faria](https://github.com/jcfaria)
- [Ivan Bezerra Allaman](https://github.com/ivanalaman)
- [Jakson Alves de Aquino](https://github.com/jalvesaq)

**Initial Python port** — [yuriccosta/fdth-python](https://github.com/yuriccosta/fdth-python)

- [Emyle Silva](https://github.com/EmyleSilva)
- [Lucas Gabriel Ferreira](https://github.com/lgferreiracic)
- [Yuri Coutinho Costa](https://github.com/yuriccosta)
- [Maria Clara](https://github.com/MaryClaraSimoes)

**UESC collaborators — first course cohort** — Gabriel Galdino,
Luciene Mª Torquato C. Batista, Stella Ribas, Thainá Guimarães,
Yohanan Santana

**UESC collaborators — second course cohort** — Alex Amaral dos Santos,
Isaque Silva Passos Ribeiro, Kaiala de Jesus Santos, Olinoedson Silva Sena

**UESC collaborators — PyPI 1.0.0 release** — Ariel Mariano Vieira,
Eduardo Ferreira Diniz da Silva, Pedro Lucas do Nascimento de Oliveira

---

## Author / Maintainer

**Faria, J. C.**  
Universidade Estadual de Santa Cruz — UESC  
Departamento de Ciências Exatas — DCEX  
Ilhéus — Bahia — Brazil

- Email: [joseclaudio.faria@gmail.com](mailto:joseclaudio.faria@gmail.com)
- GitHub: [jcfaria](https://github.com/jcfaria)
- R package: [GitHub](https://github.com/jcfaria/fdth) · [CRAN](https://cran.r-project.org/package=fdth)

---

## License

This package is free software under the
**GNU General Public License, version 2** (**GPL-2.0**).

See [LICENSE](LICENSE) for the full text.
