# News — fdth (Python)

User-facing notes for each release. Newest first.

For packaging status and internal checklists, see `w_todo/`.
For acronyms used in development, see `acronyms/`.

---

## 1.0.0 (2026-08-05)

First packaging-oriented release of the Python **fdth** port, prepared for
distribution via PyPI.

### Highlights

- Frequency distribution tables for numerical and categorical data
- Automatic entry point `fdt()` → `NumericalFDT` / `CategoricalFDT` / `MultipleFDT`
- Plots: histograms and frequency polygons
- Summary measures from grouped data (mean, median, mode, quantiles, variance, …)
- Multi-key grouping with `by=` (beyond the original R single-key limit)

### Packaging

- Modern `pyproject.toml` (PEP 621): metadata, GPL-2.0, classifiers, project URLs
- Runtime dependencies: `pandas`, `numpy`, `matplotlib`
- Optional extras: `pip install "fdth[dev]"` (mypy, black, pdoc, build, twine, …)
- Verified locally: `python -m build`, `twine check`, install from wheel, **20** unit tests OK
- **D3:** built artifacts under `dist/` are committed to the remote (unusual on
  purpose) so users can install the wheel before PyPI is live

### Documentation

- README rewritten in English (install, features, examples, development)
- Author / maintainer and license sections added
- This `NEWS.md` file introduced

### Install

```text
pip install fdth
```

Until the package appears on PyPI:

```text
pip install git+https://github.com/jcfaria/fdth-python-fork_2026.1.git
```

Or from the repository wheel:

```text
pip install https://github.com/jcfaria/fdth-python-fork_2026.1/raw/main/dist/fdth-1.0.0-py3-none-any.whl
```

### Compatibility

- Python **3.10+**
- Companion to the R package [fdth](https://cran.r-project.org/package=fdth)
  (same author / maintainer)

### Notes for users coming from R

- The high-level idea matches R **fdth** (tables + plots + grouped summaries)
- Prefer `from fdth import fdt` as the usual entry point
- See notebooks under `examples/python/` for worked examples
- Side-by-side R scripts live under `examples/r/`
