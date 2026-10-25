# Índice do projeto

Este diretório gera currículos em LaTeX e DOCX a partir de fontes versionadas.
A organização separa **código-fonte**, **saídas** e **documentação**, sem
remover nenhum arquivo existente.

## Estrutura

```text
cv-automation/
├── README.md                 # visão geral em inglês
├── README.pt-BR.md           # visão geral em português
├── LICENSE
├── Makefile                  # pipeline: docx, latex, pdf, check
├── INDICE.md                 # este arquivo
├── src/
│   ├── docx/
│   │   ├── gen_all.py        # conteúdo dos 14 currículos por vaga
│   │   └── gen_docx_base.py  # helpers de formatação DOCX
│   ├── latex/
│   │   ├── cv-preamble.tex
│   │   ├── PT-Luis-Otavio.tex
│   │   ├── EN-Luis-Otavio.tex
│   │   └── EN-Rust-Luis-Otavio.tex
│   └── tools/
│       └── check_ats.py      # verificação de ATS nos PDFs
├── output/
│   ├── docx/
│   │   ├── pt-BR/            # 7 currículos por vaga (.docx)
│   │   └── en/               # 7 currículos por vaga (.docx)
│   ├── pdf/
│   │   ├── pt-BR/            # PDFs convertidos dos .docx
│   │   └── en/
│   ├── latex/                # 3 PDFs gerais (PT, EN, EN-Rust)
│   └── legacy/               # saídas antigas preservadas (28 arquivos)
└── .git/
```

## Comandos

```sh
make docx    # gera os 14 .docx em output/docx/{pt-BR,en}
make latex   # compila os 3 .tex em output/latex
make pdf     # converte os .docx em output/pdf/{pt-BR,en}
make check   # valida ATS dos PDFs gerados
make all     # docx + latex + pdf + check
make clean   # move output/ para output-arquivo-<data> (não apaga)
```

## Onde editar

- Conteúdo por vaga: `src/docx/gen_all.py`.
- Blocos comuns e formatação DOCX: `src/docx/gen_docx_base.py`.
- Layout dos currículos gerais: arquivos `.tex` em `src/latex/`.
- Regras de verificação ATS: `src/tools/check_ats.py`.

## Observações

- `output/` é gerado e não é versionado (`.gitignore`).
- `make clean` preserva o material, movendo a pasta para
  `output-arquivo-<timestamp>`.
- Os caminhos antigos `output/ptbr` e `output/ingles` foram substituídos por
  `output/docx/pt-BR` e `output/docx/en`; os PDFs correspondentes ficam em
  `output/pdf/`.
- As saídas antigas (incluindo os três PDFs `CV-Luis-Otavio-*`) foram movidas
  para `output/legacy/`, sem exclusão.
