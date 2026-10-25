# CV Automation

**Pipeline de currículos ATS-friendly.** Um comando gera todas as versões do meu
currículo: 3 documentos LaTeX principais (PT / EN / foco Rust) e 14 currículos por
vaga (7 PT-BR + 7 EN) em `.docx`, seguido de uma verificação automática de que
cada PDF gerado sobrevive à leitura de um ATS (Applicant Tracking System):
coluna única, texto real, seções padrão e sem nomes de fornecedores.

![License](https://img.shields.io/badge/license-MIT-yellow.svg)
![Python](https://img.shields.io/badge/python-3.12%2B-blue.svg)
![LaTeX](https://img.shields.io/badge/LaTeX-Tectonic-008080.svg)
![ATS](https://img.shields.io/badge/ATS-friendly-brightgreen.svg)

*Read in English: [README.md](README.md)*

---

## O que ele gera

```
output/
├── docx/
│   ├── pt-BR/                      # 7 currículos por vaga (.docx)
│   └── en/                         # os mesmos 7 papéis em inglês (.docx)
├── pdf/
│   ├── pt-BR/                      # PDFs convertidos dos .docx
│   └── en/
└── latex/                          # 3 PDFs gerais (PT, EN e EN-Rust)
```

## Quick start

```sh
# requisitos: uv, tectonic e (opcional) libreoffice
make all      # docx + latex + pdf + verificação ATS
make docx     # 14 currículos .docx (output/docx/pt-BR, output/docx/en)
make latex    # 3 PDFs LaTeX                     (output/latex)
make pdf      # converte .docx -> .pdf (output/pdf/)
make check    # verificação ATS de todos os PDFs gerados
make clean
```

As ferramentas são parametrizáveis, ex.: `make latex TECTONIC=~/.local/bin/tectonic`.

### Instalando o toolchain

| Ferramenta | Instalação |
|---|---|
| [uv](https://docs.astral.sh/uv) | `curl -LsSf https://astral.sh/uv/install.sh \| sh` |
| [tectonic](https://tectonic-typesetting.github.io) | `cargo install tectonic` (ou binário do release) |
| LibreOffice (opcional, p/ DOCX -> PDF) | gerenciador de pacotes do sistema |

As dependências Python são resolvidas na hora pelo `uv run --with ...` — sem
virtualenv para criar e sem `requirements.txt` para manter.

## Como funciona

- **`src/latex/`** — um `cv-preamble.tex` compartilhado (Arial via `fontspec`, coluna
  única, hifenização desativada para nunca quebrar palavras) + um `.tex` por CV.
  Compilado com Tectonic (XeTeX autocontido).
- **`src/docx/`** — `gen_docx_base.py` concentra os helpers de formatação e os blocos
  comuns (experiência, formação, idiomas); `gen_all.py` declara o conteúdo por
  vaga (resumo, projetos, habilidades) e renderiza os 14 arquivos com
  [python-docx](https://python-docx.readthedocs.io).
- **`src/tools/check_ats.py`** — extrai o texto de cada PDF gerado e verifica: seções
  padrão, contato no corpo, sem caracteres corrompidos, datas consistentes e
  palavras-chave esperadas. Saída: uma linha por arquivo, `OK` ou a lista de
  problemas.

## Regras de ATS aplicadas

Com base nas orientações de ATS vigentes para 2026:

- coluna única, sem tabelas, sem caixas de texto, sem imagens
- contato como texto real no corpo (nunca em cabeçalho/rodapé de página)
- nomes de seção convencionais (`Resumo Profissional`, `Experiência`,
  `Habilidades`, `Formação`...) para o parser mapear os campos
- fonte padrão (Arial) entre 9 e 16 pt, com texto embutido e selecionável
- bullets simples com `-`, sem fontes de ícones ou glifos decorativos
- um único formato de data em todo o documento (`Fev 2025 - Atual`)
- palavras-chave da vaga, sustentadas por bullets de projetos reais
- sem travessões longos, sem nomes de fornecedores, sem keyword stuffing

## Faça seu

O conteúdo é dado, não código: faça fork e então

1. edite o conteúdo por vaga em `src/docx/gen_all.py` (resumos, projetos,
   habilidades) e os blocos comuns em `src/docx/gen_docx_base.py`;
2. edite ou substitua os arquivos `.tex` em `src/latex/`;
3. rode `make all` e confira o relatório no final.

Toda afirmação no resultado deve ser verificável — as minhas apontam para
repositórios públicos em [github.com/luis-ota](https://github.com/luis-ota).

## Licença

MIT — use o pipeline, o template e as regras de ATS; guarde a sua própria história.
