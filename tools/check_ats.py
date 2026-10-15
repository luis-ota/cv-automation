# -*- coding: utf-8 -*-
"""
Verificação ATS dos PDFs gerados:
- texto extraível (nunca imagem)
- seções padrão presentes
- contato no corpo
- ordem linear (sem fragmentação de colunas)
- datas em formato consistente
- sem caracteres corrompidos
- palavras-chave essenciais presentes
"""
import re
import sys
from pathlib import Path
from pypdf import PdfReader

EMAIL = "luotasss@gmail.com"
PHONE_RE = re.compile(r"(\(41\)\s*9\s*9879-8238|\+55\s*41\s*99879-8238)")

SECTION_PT = ["Resumo Profissional", "Experiência Profissional", "Habilidades Técnicas", "Formação Acadêmica", "Idiomas"]
SECTION_EN = ["Professional Summary", "Professional Experience", "Technical Skills", "Education", "Languages"]
KEYWORDS = ["Python", "Rust", "PostgreSQL", "Docker", "GitHub", "React"]


def check_pdf(path: Path):
    problems, warnings = [], []
    reader = PdfReader(str(path))
    pages = len(reader.pages)
    text = "\n".join((p.extract_text() or "") for p in reader.pages)

    if not text.strip():
        problems.append("sem texto extraível (provável imagem)")
        return problems, warnings, pages

    low = text.lower()
    # seções
    is_pt = "resumo profissional" in low or "experiência profissional" in low
    sections = SECTION_PT if is_pt else SECTION_EN
    for s in sections:
        if s.lower() not in low:
            problems.append(f"seção ausente: {s}")

    # contato
    if EMAIL not in text:
        problems.append("e-mail ausente")
    if not PHONE_RE.search(text):
        problems.append("telefone ausente/formatado de forma diferente")
    if "github.com/luis-ota" not in text:
        problems.append("link do GitHub ausente")
    if "linkedin.com/in/luis-ota" not in text:
        warnings.append("link do LinkedIn ausente")

    # caracteres corrompidos
    for bad in ("\ufffd", "â€", "Ã©"):
        if bad in text:
            problems.append(f"caractere corrompido detectado: {bad!r}")

    # datas consistentes (Mmm AAAA)
    dates = re.findall(r"\b(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec|Fev|Abr|Mai|Ago|Set|Out|Dez|Atual|Present|expected|previsão)\b", text)
    if len(dates) < 6:
        warnings.append(f"poucas datas reconhecidas ({len(dates)})")

    # keywords
    missing_kw = [k for k in KEYWORDS if k.lower() not in low]
    if missing_kw:
        warnings.append(f"keywords ausentes: {', '.join(missing_kw)}")

    # heurística de ordem linear: bullets sempre iniciam linha
    bullet_lines = [l for l in text.splitlines() if l.strip().startswith("•") or l.strip().startswith("- ")]
    if len(bullet_lines) < 10:
        warnings.append(f"poucas linhas de bullet ({len(bullet_lines)})")

    return problems, warnings, pages


def main():
    root = Path(__file__).resolve().parent.parent
    roots = [Path(p) for p in sys.argv[1:]] or [
        root / "output" / "latex",
        root / "output" / "ptbr",
        root / "output" / "ingles",
    ]
    pdfs = []
    for r in roots:
        if r.exists():
            pdfs += sorted(r.glob("*.pdf"))
    if not pdfs:
        print("Nenhum PDF encontrado. Rode 'make all' antes, ou passe diretórios como argumento.")
        return 1

    ok = 0
    print(f"{'ARQUIVO':<58} {'PÁGS':<5} STATUS")
    print("-" * 100)
    for pdf in pdfs:
        problems, warnings, pages = check_pdf(pdf)
        try:
            name = str(pdf.relative_to(Path(__file__).resolve().parent.parent))
        except ValueError:
            name = str(pdf)
        if problems:
            status = "FALHA: " + "; ".join(problems)
        else:
            status = "OK" + ("  (avisos: " + "; ".join(warnings) + ")" if warnings else "")
            ok += 1
        print(f"{name:<58} {pages:<5} {status}")
    print("-" * 100)
    print(f"{ok}/{len(pdfs)} aprovados sem problemas.")
    return 0 if ok == len(pdfs) else 1


if __name__ == "__main__":
    sys.exit(main())
