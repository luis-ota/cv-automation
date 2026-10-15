# -*- coding: utf-8 -*-
"""
Gera os 14 currículos específicos (7 ptbr + 7 ingles) em .docx.

ATS best practices aplicadas:
- coluna única, sem tabelas/text boxes/imagens
- Arial 9-16pt (fonte padrão)
- seções com nomes convencionais (Resumo/Experiência/Projetos/Habilidades/Formação/Idiomas)
- contato no corpo do texto
- bullets com hífen simples ("- ")
- datas em formato único (Mmm AAAA – Mmm AAAA)
- texto real (nada de artefatos gráficos)
"""
from docx import Document
from docx.shared import Pt, Inches, RGBColor
from docx.enum.text import WD_ALIGN_PARAGRAPH, WD_LINE_SPACING
from docx.oxml.ns import qn
from docx.oxml import OxmlElement
from docx.opc.constants import RELATIONSHIP_TYPE as RT
from docx.enum.text import WD_TAB_ALIGNMENT
import os

FONT = "Arial"
LINK_COLOR = "14406B"

# ----------------------------------------------------------------------------
# Helpers de formatação
# ----------------------------------------------------------------------------

def set_run_font(run, size, bold=False, italic=False, color=None, underline=False):
    run.font.name = FONT
    run.font.size = Pt(size)
    run.bold = bold
    run.italic = italic
    if color:
        run.font.color.rgb = RGBColor.from_string(color)
    rpr = run._element.get_or_add_rPr()
    rfonts = rpr.find(qn("w:rFonts"))
    if rfonts is None:
        rfonts = OxmlElement("w:rFonts")
        rpr.append(rfonts)
    for attr in ("w:ascii", "w:hAnsi", "w:cs", "w:eastAsia"):
        rfonts.set(qn(attr), FONT)


def add_hyperlink(paragraph, url, text, size=8):
    part = paragraph.part
    r_id = part.relate_to(url, RT.HYPERLINK, is_external=True)
    hyperlink = OxmlElement("w:hyperlink")
    hyperlink.set(qn("r:id"), r_id)
    new_run = OxmlElement("w:r")
    rPr = OxmlElement("w:rPr")
    rfonts = OxmlElement("w:rFonts")
    for attr in ("w:ascii", "w:hAnsi", "w:cs"):
        rfonts.set(qn(attr), FONT)
    rPr.append(rfonts)
    sz = OxmlElement("w:sz"); sz.set(qn("w:val"), str(int(size * 2))); rPr.append(sz)
    color = OxmlElement("w:color"); color.set(qn("w:val"), LINK_COLOR); rPr.append(color)
    new_run.append(rPr)
    t = OxmlElement("w:t"); t.text = text
    t.set(qn("xml:space"), "preserve")
    new_run.append(t)
    hyperlink.append(new_run)
    paragraph._p.append(hyperlink)


def para(doc, text="", size=9, bold=False, italic=False, after=0, before=0,
         align=None, color=None, keep_with_next=False):
    p = doc.add_paragraph()
    pf = p.paragraph_format
    pf.space_after = Pt(after)
    pf.space_before = Pt(before)
    pf.line_spacing_rule = WD_LINE_SPACING.SINGLE
    if align is not None:
        p.alignment = align
    if keep_with_next:
        pf.keep_with_next = True
    if text:
        r = p.add_run(text)
        set_run_font(r, size, bold=bold, italic=italic, color=color)
    return p


def run_para(doc, runs, after=0, before=0, align=None):
    """Parágrafo com múltiplos runs: lista de (texto, size, bold, italic, link ou None)."""
    p = doc.add_paragraph()
    pf = p.paragraph_format
    pf.space_after = Pt(after)
    pf.space_before = Pt(before)
    pf.line_spacing_rule = WD_LINE_SPACING.SINGLE
    if align is not None:
        p.alignment = align
    for item in runs:
        text, size, bold, italic, link = item
        if link:
            add_hyperlink(p, link, text, size=size)
        else:
            r = p.add_run(text)
            set_run_font(r, size, bold=bold, italic=italic)
    return p


def section(doc, title):
    p = para(doc, title, size=11, bold=True, before=6, after=2, keep_with_next=True)
    # linha fina inferior (borda), recurso de parágrafo — não é tabela/text box
    pPr = p._p.get_or_add_pPr()
    pbdr = OxmlElement("w:pBdr")
    bottom = OxmlElement("w:bottom")
    bottom.set(qn("w:val"), "single")
    bottom.set(qn("w:sz"), "6")
    bottom.set(qn("w:space"), "1")
    bottom.set(qn("w:color"), "000000")
    pbdr.append(bottom)
    pPr.append(pbdr)
    return p


def bullet(doc, text):
    return para(doc, "- " + text, size=9)


def job(doc, company, role, period, location):
    run_para(doc, [(company, 10, True, False, None)], before=4, after=0)
    run_para(doc, [(role + "  ", 9, False, False, None),
                   (period + "  ", 9, False, False, None),
                   (location, 9, False, False, None)], after=0)


def project(doc, name, link_text=None, link_url=None, tag=None):
    runs = [(name, 9, True, False, None)]
    if tag:
        runs.append(("  " + tag, 9, False, True, None))
    if link_text and link_url:
        runs.append(("  ", 8, False, False, None))
        runs.append((link_text, 8, False, False, link_url))
    run_para(doc, runs, before=3, after=0)


def new_doc(pdf_title):
    doc = Document()
    sec = doc.sections[0]
    sec.left_margin = Inches(0.7)
    sec.right_margin = Inches(0.7)
    sec.top_margin = Inches(0.55)
    sec.bottom_margin = Inches(0.5)
    normal = doc.styles["Normal"]
    normal.font.name = FONT
    normal.font.size = Pt(9)
    normal.paragraph_format.space_after = Pt(0)
    cp = doc.core_properties
    cp.author = "Luís Otávio Silva Santos"
    cp.title = pdf_title
    return doc


def header(doc, headline, lang="pt"):
    para(doc, "Luís Otávio Silva Santos", size=16, bold=True, after=0)
    if lang == "pt":
        run_para(doc, [("Rebouças, Curitiba, Paraná  ", 9, False, False, None),
                       ("(41) 9 9879-8238  ", 9, False, False, None),
                       ("luotasss@gmail.com", 9, False, False, "mailto:luotasss@gmail.com")], after=0)
        run_para(doc, [("linkedin.com/in/luis-ota", 9, False, False, "https://linkedin.com/in/luis-ota"),
                       ("  ", 9, False, False, None),
                       ("github.com/luis-ota", 9, False, False, "https://github.com/luis-ota"),
                       ("  ", 9, False, False, None),
                       ("wired.rs", 9, False, False, "https://wired.rs")], after=1)
    else:
        run_para(doc, [("Rebouças, Curitiba, Paraná, Brazil  ", 9, False, False, None),
                       ("+55 41 99879-8238  ", 9, False, False, None),
                       ("luotasss@gmail.com", 9, False, False, "mailto:luotasss@gmail.com")], after=0)
        run_para(doc, [("linkedin.com/in/luis-ota", 9, False, False, "https://linkedin.com/in/luis-ota"),
                       ("  ", 9, False, False, None),
                       ("github.com/luis-ota", 9, False, False, "https://github.com/luis-ota"),
                       ("  ", 9, False, False, None),
                       ("wired.rs", 9, False, False, "https://wired.rs")], after=1)
    if headline:
        para(doc, headline, size=11, bold=True, after=2, before=2)


# ----------------------------------------------------------------------------
# Blocos de conteúdo comuns (PT / EN)
# ----------------------------------------------------------------------------

EXP_PT = [
    ("Amber Soluções de Tecnologia", "Desenvolvedor de Software", "Fev 2025 - Atual", "Curitiba, PR", [
        "Desenvolvi e mantive APIs REST em Python para integração com plataformas externas e sistemas de parceiros.",
        "Implementei novas funcionalidades de backend seguindo requisitos de negócio, com foco em confiabilidade e cobertura de testes.",
        "Otimizei a performance de sistemas legados via profiling e reescrita de consultas SQL, reduzindo o tempo de resposta em até 40%.",
        "Corrigi bugs críticos e refatorei código, melhorando a organização e a legibilidade da base de código.",
        "Colaborei com equipes de QA e Produto para garantir a confiabilidade dos recursos e a documentação técnica adequada.",
    ]),
    ("Wired Layer Co.", "Fundador e Desenvolvedor", "2025 - Atual", "Curitiba, PR", [
        "Desenvolvo e opero produtos SaaS completos em produção: cadastro, login com Google, onboarding, cobrança via Pix e cartão, e ledger.",
        "Gerencio a infraestrutura self-hosted em VPSes próprias (Docker Compose, Caddy, PostgreSQL, Redis, MinIO e CI/CD) com práticas cloud-native de containers, deploy automatizado e observabilidade, para produtos como Vitrines, manifestacao.online, Peladafy, ai.ther e Wired Leads.",
    ]),
    ("Serdia Eletrônica Industrial S.A.", "Estagiário de Pesquisa e Desenvolvimento", "Mar 2024 - Fev 2025", "Curitiba, PR", [
        "Desenvolvi sistema embarcado em Raspberry Pi para testes eletrostáticos com identificação biométrica digital, com rastreabilidade completa dos resultados.",
        "Implementei sincronização de dados entre SQLite local (camada de cache) e PostgreSQL centralizado, com API Flask para atualizações em tempo real e arquivamento automático de logs.",
        "Projetei sistema de chamados técnicos da produção com Next.js, TypeScript, PostgreSQL e Docker, incluindo cronômetro, gerenciamento de usuários e mapa interativo.",
        "Automatizei o preenchimento de planilhas comerciais com Python, Pandas e Openpyxl, reduzindo o processo de 3 dias para 1-2 minutos (mais de 99% de ganho).",
        "Desenvolvi automação de testes sequenciais via Bluetooth, com impressão automática de etiquetas e persistência de dados via API.",
    ]),
    ("Equalize IT Solutions", "Estagiário de Suporte Técnico", "Abr 2023 - Fev 2024", "Curitiba, PR", [
        "Forneci suporte L1/L2 a clientes Linux e Windows via VPN e SSH, resolvendo incidentes dentro do SLA.",
        "Automatizei tarefas de manutenção de servidores com scripts Bash e PowerShell, reduzindo o tempo de intervenção manual.",
        "Auxiliei na instalação de sistemas operacionais e elaborei manuais para o help desk.",
    ]),
]

EXP_EN = [
    ("Amber Soluções de Tecnologia", "Software Developer", "Feb 2025 - Present", "Curitiba, Brazil", [
        "Developed and maintained RESTful APIs in Python for integration with external platforms and partner systems.",
        "Implemented new backend features following business requirements, focusing on reliability and test coverage.",
        "Optimized legacy system performance through profiling and rewriting slow SQL queries, reducing response time by up to 40%.",
        "Fixed critical bugs and refactored code, improving codebase organization and readability.",
        "Collaborated with QA and Product teams to ensure feature reliability and proper technical documentation.",
    ]),
    ("Wired Layer Co.", "Founder and Developer", "2025 - Present", "Curitiba, Brazil", [
        "Build and operate complete SaaS products in production: sign-up, Google login, onboarding, Pix and card billing, and ledger.",
        "Manage the self-hosted infrastructure on my own VPSes (Docker Compose, Caddy, PostgreSQL, Redis, MinIO, CI/CD) with cloud-native practices for containers, automated deploys, and observability, powering products such as Vitrines, manifestacao.online, Peladafy, ai.ther and Wired Leads.",
    ]),
    ("Serdia Eletrônica Industrial S.A.", "Research and Development Intern", "Mar 2024 - Feb 2025", "Curitiba, Brazil", [
        "Developed an embedded system on Raspberry Pi for electrostatic testing with digital biometric identification and full result traceability.",
        "Implemented data synchronization between local SQLite (cache layer) and centralized PostgreSQL, with a Flask API for real-time updates and automated log archiving.",
        "Designed the production technical ticketing system with Next.js, TypeScript, PostgreSQL and Docker, including a timer, user management and an interactive map.",
        "Automated commercial spreadsheet filling with Python, Pandas and Openpyxl, reducing the process from 3 days to 1-2 minutes (99%+ efficiency gain).",
        "Developed a Bluetooth-based sequential test automation tool with automatic label printing and API-backed data persistence.",
    ]),
    ("Equalize IT Solutions", "Technical Support Intern", "Apr 2023 - Feb 2024", "Curitiba, Brazil", [
        "Provided L1/L2 support to Linux and Windows clients via VPN and SSH, resolving incidents within SLA.",
        "Automated server maintenance tasks with Bash and PowerShell scripts, reducing manual intervention time.",
        "Assisted in operating system installation and wrote help desk documentation.",
    ]),
]

EDU_PT = ("Bacharelado em Engenharia de Software - PUCPR",
          "Mar 2023 - Dez 2026 (previsão)  Disciplinas relevantes: Sistemas Operacionais, Redes, Estrutura de Dados, Sistemas Embarcados, Banco de Dados, Fundamentos de IA, Desenvolvimento Web")
EDU_EN = ("B.S. in Software Engineering - PUCPR",
          "Mar 2023 - Dec 2026 (expected)  Relevant coursework: Operating Systems, Networks, Data Structures, Embedded Systems, Database Design, AI Fundamentals, Web Development")

LANG_PT = "Português (nativo)  |  Inglês (intermediário, B2)  |  Alemão (básico)"
LANG_EN = "Portuguese (native)  |  English (intermediate, B2)  |  German (basic)"

COURSES_PT = [
    "Arquiteto de Software (PUCPR)", "Analista de Sistemas (PUCPR)",
    "Analista de Requisitos (PUCPR)", "Desenvolvedor WEB (PUCPR)",
    "Curso Completo de Python 3: do Iniciante ao Avançado (Udemy, 2021)",
    "Operador e Manutenção de Computadores (SPAE, 2019)",
]
COURSES_EN = [
    "Software Architect (PUCPR)", "Systems Analyst (PUCPR)",
    "Requirements Analyst (PUCPR)", "Web Developer (PUCPR)",
    "The Complete Python 3 Course: Beginner to Advanced (Udemy, 2021)",
    "Computer Operator and Maintenance (SPAE, 2019)",
]


def build_cv(path, lang, headline, summary, projects, skills, exps,
             edu, languages, courses):
    doc = new_doc(path)
    header(doc, headline, lang)

    section(doc, "Resumo Profissional" if lang == "pt" else "Professional Summary")
    para(doc, summary, size=9, after=0)

    section(doc, "Experiência Profissional" if lang == "pt" else "Professional Experience")
    for company, role, period, loc, bl in exps:
        job(doc, company, role, period, loc)
        for b in bl:
            bullet(doc, b)

    section(doc, "Projetos" if lang == "pt" else "Projects")
    for name, tag, link_text, link_url, descs in projects:
        project(doc, name, link_text=link_text, link_url=link_url, tag=tag)
        for d in descs:
            bullet(doc, d)

    section(doc, "Habilidades Técnicas" if lang == "pt" else "Technical Skills")
    for cat, val in skills:
        run_para(doc, [("- " + cat + ": ", 9, True, False, None), (val, 9, False, False, None)], after=0)

    section(doc, "Formação Acadêmica" if lang == "pt" else "Education")
    para(doc, edu[0], size=10, bold=True, after=0)
    para(doc, edu[1], size=9, after=0)

    section(doc, "Idiomas" if lang == "pt" else "Languages")
    para(doc, languages, size=9, after=0)

    section(doc, "Cursos e Certificações" if lang == "pt" else "Courses and Certifications")
    for c in courses:
        bullet(doc, c)

    os.makedirs(os.path.dirname(path), exist_ok=True)
    doc.save(path)
    return path
