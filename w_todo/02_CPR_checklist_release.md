# CPR — Controlo de Produção / Roadmap

Marque com `[x]` quando concluir (BOK no chat).  
Objetivo: primeira publicação do `fdth` no **TPYPI** e depois no **PYPI**.  
Siglas: `acronyms/acronyms_pt.txt`. Cadeia VP: **VP-FDTH**.

---

## A. Bloqueadores (obrigatório antes do upload)

- [x] `pyproject.toml` completo (PEP 621): name, version, description, readme, license, authors, requires-python, dependencies, urls, classifiers
- [x] `[build-system]` com setuptools (ou outro backend)
- [x] `pandas-stubs` removido das dependências de runtime (só em extras `dev`)
- [x] Versão no formato PEP 440 (ex.: `1.0.0`)
- [x] LICENSE alinhada aos metadados (GPL-2.0)
- [x] README com instalação: `pip install fdth`
- [x] Build local sem erro: `python -m build`
- [x] Checagem do artefato: `twine check dist/*`
- [x] Teste de instalação a partir do wheel em venv limpo
- [x] Testes passam após instalar o wheel (`python -m unittest discover -s tests`)

## B. Importantes (recomendado na 1ª release)

- [x] `project.urls`: Homepage, Repository, Issues (+ link do pacote R)
- [x] Classifiers (Python versions, License, Topic :: Scientific/Engineering :: ...)
- [x] Keywords: frequency distribution, histogram, statistics, fdt
- [x] Extras `[project.optional-dependencies]` `dev` (mypy, black, pdoc, pandas-stubs, build, twine)
- [ ] CHANGELOG.md (pelo menos entrada `1.0.0`)
- [ ] Conta no PyPI + TestPyPI (ou Trusted Publishing via GitHub)
- [ ] Upload de ensaio no **TestPyPI** e `pip install` a partir dele
- [ ] Decisão: manter material de disciplina (`HelpGit.md`, `examples/R`) no sdist ou excluir via `MANIFEST`/config

## C. Desejáveis (polish)

- [ ] GitHub Actions: testes em 3.10–3.12 (+ build)
- [ ] Trusted Publishing (OIDC) para upload sem senha de API
- [ ] Migrar para layout `src/fdth/`
- [ ] Docs hospedadas (Read the Docs / GitHub Pages com pdoc)
- [ ] `py.typed` se tipagem estiver estável
- [ ] Badge de versão PyPI no README

---

## D. Sequência de comandos (referência)

```bash
# ambiente limpo
python -m venv .venv-release
# Windows PowerShell:
.\.venv-release\Scripts\Activate.ps1

pip install -U pip build twine
python -m build
twine check dist/*

# ensaio
twine upload --repository testpypi dist/*
pip install -i https://test.pypi.org/simple/ fdth

# produção (só depois do ensaio OK)
twine upload dist/*
```

## E. Registro de releases

| Versão | Data | Ambiente | Notas |
|--------|------|----------|-------|
| 1.0.0 | 2026-08-05 | TestPyPI | https://test.pypi.org/project/fdth/1.0.0/ |
| 1.0.0 | 2026-08-05 | **PyPI** | https://pypi.org/project/fdth/1.0.0/ — VCP BOK |
