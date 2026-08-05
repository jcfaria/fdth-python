# News — fdth (Python)

User-facing notes for each release. Newest first.

For packaging status and internal checklists, see `w_todo/`.
For acronyms used in development, see `acronyms/`.

---

## Unreleased

### Repository

- Canonical GitHub project is now **[jcfaria/fdth-python](https://github.com/jcfaria/fdth-python)**
  (standalone reference repo, not a course/semester fork)
- Examples reorganized: `examples/Python/{notebooks,scripts}` and `examples/R`

---

## 1.0.0 (2026-08-05)

First release of the Python **fdth** port on **PyPI** and **TestPyPI**.

- PyPI: https://pypi.org/project/fdth/1.0.0/
- TestPyPI: https://test.pypi.org/project/fdth/1.0.0/

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
- Verified: build, `twine check`, TestPyPI install + **20** unit tests, then PyPI upload
- **D3:** `dist/` wheel/sdist also kept in the GitHub repository

### Documentation

- README in English (install, features, examples, development)
- Author / maintainer and license sections
- This `NEWS.md` file

### Install

```text
pip install fdth
```

### Compatibility

- Python **3.10+**
- Companion to the R package [fdth](https://cran.r-project.org/package=fdth)
  (same author / maintainer)

### Notes for users coming from R

- The high-level idea matches R **fdth** (tables + plots + grouped summaries)
- Prefer `from fdth import fdt` as the usual entry point
- See notebooks and mirrored scripts under `examples/Python/`
- Side-by-side R scripts live under `examples/R/`
