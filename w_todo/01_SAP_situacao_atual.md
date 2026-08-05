# SAP — Situação Atual do Projeto

**Pacote:** `fdth` (Python) · **FDTH**  
**Repositório canónico:** https://github.com/jcfaria/fdth-python  
**PyPI:** https://pypi.org/project/fdth/  
**Atualizado em:** 2026-08-05  
**Origem:** port coletivo do pacote **R-FDTH** [fdth](https://github.com/jcfaria/fdth) (CRAN)  
**Glossário:** `acronyms/` (PT preferido)

---

## 1. O que o projeto é

Biblioteca Python para tabelas de distribuição de frequências (FDT),
histogramas e polígonos, espelhando a API/conceito do `fdth` em R.

API pública principal (`fdth/__init__.py`):

- `fdt` — detecção automática / atalho
- `NumericalFDT`, `CategoricalFDT`, `MultipleFDT`
- `Binning`

---

## 2. Estrutura atual (raiz)

```
fdth-python/
├── fdth/                 # código do pacote
├── tests/                # unittest
├── examples/             # Python (notebooks + scripts) e R
├── pyproject.toml
├── README.md
├── NEWS.md
├── LICENSE               # GPL-2.0
├── HelpGit.md
├── acronyms/
└── w_todo/
```

Layout: **flat** (pacote na raiz). Adequado para primeira publicação.

---

## 3. Empacotamento hoje

| Item | Estado |
|------|--------|
| `pyproject.toml` | **Atualizado** (PEP 621 + build-system) |
| Build backend (PEP 517) | setuptools (`[build-system]`) |
| Metadados PyPI (descrição, authors, license, URLs, classifiers) | Preenchidos |
| `README` como long description | `readme = "README.md"` |
| Nome no PyPI (`fdth`) | **Livre** (não há pacote oficial `fdth` no PyPI) |
| Versão | `1.0.0` (PEP 440) |
| Dependências runtime | `pandas`, `numpy`, `matplotlib` |
| `pandas-stubs` | Movido para extras `dev` |
| LICENSE | GPL-2.0 presente (alinhado ao R: GPL >= 2) |
| Wheel / sdist | Ainda não validados com `python -m build` |
| Conta / Trusted Publishing PyPI | Não configurado |

---

## 4. Documentação e qualidade

| Item | Estado |
|------|--------|
| README | Existe; mistura PT/EN; bom exemplo; pouco focado em “usuário PyPI” |
| CHANGELOG | Ausente |
| Docs API (`pdoc`) | Mencionado no README; pasta `doc/` no `.gitignore` |
| Exemplos | Notebooks + scripts em `examples/Python`; R em `examples/R` |
| Testes | `tests/` com unittest |
| CI (GitHub Actions) | Ausente |

---

## 5. Créditos / manutenção

- Autor original (R): José Cláudio Faria e colaboradores
- Port Python: várias turmas UESC (2024–2026) + fork atual
- Maintainer sugerido para PyPI: José Cláudio Faria  
  (`joseclaudio.faria@gmail.com`, conforme pacote R no CRAN)

---

## 6. Veredito SAP

O código e os testes já formam um pacote **funcionalmente maduro** para
uma primeira release. O que falta é sobretudo **higiene de distribuição**:
metadados, build, README de instalação via `pip`, e processo de upload.

**Não** é necessário criar `PyPI-fdth/` com cópia do código.
