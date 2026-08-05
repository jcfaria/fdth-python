# Plano de ações — caminho até o PyPI

Ordem sugerida. Atualizar o CPR conforme cada passo fechar.

---

## Fase 0 — Organização (feita nesta sessão)

1. Criar `w_todo/` com SAP, CPR e este plano.
2. Confirmar: publicar a partir da **raiz** (sem pasta `PyPI-fdth` duplicando código).
3. Confirmar nome `fdth` aparentemente livre no PyPI.

## Fase 1 — Metadados e build (próximo)

1. Completar `pyproject.toml` (bloqueadores do CPR).
2. Ajustar dependências (runtime vs `dev`).
3. Gerar sdist + wheel e validar com `twine check`.
4. Instalar wheel em venv limpo e rodar testes.

## Fase 2 — Documentação voltada ao usuário

1. Seção clara de instalação no README (`pip install fdth`).
2. Manter exemplo curto de uso no topo.
3. Criar `CHANGELOG.md` com `1.0.0`.
4. (Opcional) enxugar tom “disciplina” no README público, movendo detalhes para `HelpGit.md` / docs internas.

## Fase 3 — Ensaio TestPyPI

1. Criar contas TestPyPI / PyPI (ou configurar Trusted Publishing).
2. Upload para TestPyPI.
3. Instalar e validar de ponta a ponta.

## Fase 4 — Release PyPI

1. Tag git `v1.0.0` (ou a versão escolhida).
2. Upload para PyPI.
3. Atualizar README com badge e link.
4. Registrar na tabela do CPR.

## Fase 5 — Pós-release

1. CI (GitHub Actions).
2. Avaliar layout `src/`.
3. Docs geradas automaticamente.

---

## Responsável sugerido

- **Maintainer PyPI:** José Cláudio Faria  
- **Apoio técnico (empacotamento):** este fluxo assistido no Cursor + colaboradores do fork
