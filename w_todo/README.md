# w_todo — acompanhamento da publicação PyPI

Pasta de trabalho para textos SAP / CPR / plano do pacote **fdth** (Python).

Não contém o código do pacote (esse continua em `fdth/` na raiz).  
Siglas canónicas: [`../acronyms/`](../acronyms/) (preferir `acronyms_pt.txt`).

## Packs neste pasta

| Pack | Significado (ver glossário) | Arquivo |
|------|-----------------------------|---------|
| **SAP** | Situação Atual do Projeto | [`01_SAP_situacao_atual.md`](01_SAP_situacao_atual.md) |
| **CPR** | Controlo de Produção / Roadmap | [`02_CPR_checklist_release.md`](02_CPR_checklist_release.md) |
| **Plano** | Ordem sugerida até VCP/PyPI | [`03_plano_acoes.md`](03_plano_acoes.md) |

## Decisões

**D1 [F]** Estrutura de publicação

- **Não** criar pasta `PyPI-fdth` com cópia do código.
- Publicar a partir da **raiz** (`pyproject.toml` + `fdth/`).
- Opcional no futuro: layout `SRC` (`src/fdth/`).

**D2 [F]** Ramos

- **`work` é sempre o ramo local ativo** (desenvolvimento diário).
- `main` só via **CPMW** (estável / releases); após promover, voltar a `work`.

## Como usar

1. Atualizar o **SAP** quando o estado do projeto mudar.
2. Marcar VPs / itens no **CPR** conforme BOK.
3. Seguir o **Plano**; publicação completa = **VCP** (GO humano).
