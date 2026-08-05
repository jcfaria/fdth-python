# Examples

Side-by-side material for the **fdth** Python port and the original R package.

```text
examples/
├── Python/
│   ├── notebooks/   # Jupyter notebooks (.ipynb)
│   └── scripts/     # Same examples as plain Python (.py)
└── R/               # R scripts mirroring CRAN/fdth usage
```

## Python

Install the package first (`pip install fdth` or `pip install -e .` from the repo root).

Notebooks:

```text
examples/Python/notebooks/
```

Mirrored scripts (snake_case names):

```text
examples/Python/scripts/
  categorical_fdt.py
  categorical_fdt_plots.py
  measures_of_central_tendency_and_position.py
  measures_of_dispersion.py
  multiple_fdt.py
  multiple_fdt_plots.py
  numerical_fdt.py
  numerical_fdt_plots.py
```

Run a script from the repository root, for example:

```powershell
python examples/Python/scripts/numerical_fdt.py
```

Plotting scripts open Matplotlib windows; close them to continue when several plots run in sequence.

## R

Comparable R examples live under `examples/R/` (organized by topic, each with a `test.R`).
