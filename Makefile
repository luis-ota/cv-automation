# CV Automation — build pipeline
#
# Requisitos:
#   - uv            (https://docs.astral.sh/uv)
#   - tectonic      (https://tectonic-typesetting.github.io)
#   - libreoffice   (opcional, para converter DOCX -> PDF)
#
# Uso:
#   make docx    # gera os 14 currículos específicos (.docx) em output/ptbr e output/ingles
#   make latex   # compila os 3 CVs LaTeX (.pdf) em output/latex
#   make pdf     # converte os .docx para .pdf (LibreOffice)
#   make check   # roda a verificação ATS em todos os PDFs gerados
#   make all     # docx + latex + pdf + check
#   make clean   # apaga output/

UV       ?= uv
TECTONIC ?= tectonic
SOFFICE  ?= soffice
OUTPUT   := output

.PHONY: all docx latex pdf check clean

all: docx latex pdf check

docx:
	$(UV) run --with python-docx python docx/gen_all.py

latex:
	mkdir -p $(OUTPUT)/latex
	for f in latex/CV-*.tex; do $(TECTONIC) -X compile --outdir $(OUTPUT)/latex "$$f"; done

pdf: docx
	$(SOFFICE) --headless --convert-to pdf --outdir $(OUTPUT)/ptbr $(OUTPUT)/ptbr/*.docx
	$(SOFFICE) --headless --convert-to pdf --outdir $(OUTPUT)/ingles $(OUTPUT)/ingles/*.docx

check:
	$(UV) run --with pypdf python tools/check_ats.py

clean:
	rm -rf $(OUTPUT)
