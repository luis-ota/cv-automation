# CV Automation — build pipeline
#
# Requisitos:
#   - uv            (https://docs.astral.sh/uv)
#   - tectonic      (https://tectonic-typesetting.github.io)
#   - libreoffice   (opcional, para converter DOCX -> PDF)
#
# Uso:
#   make docx    # gera os 14 currículos específicos (.docx) em output/docx/pt-BR e output/docx/en
#   make latex   # compila os 3 CVs LaTeX (.pdf) em output/latex
#   make pdf     # converte os .docx para .pdf em output/pdf/
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
	$(UV) run --with python-docx python src/docx/gen_all.py

latex:
	mkdir -p $(OUTPUT)/latex
	for f in src/latex/PT-*.tex src/latex/EN-*.tex; do $(TECTONIC) -X compile --outdir $(OUTPUT)/latex "$$f"; done

pdf: docx
	mkdir -p $(OUTPUT)/pdf/pt-BR
	$(SOFFICE) --headless --convert-to pdf --outdir $(OUTPUT)/pdf/pt-BR $(OUTPUT)/docx/pt-BR/*.docx
	mkdir -p $(OUTPUT)/pdf/en
	$(SOFFICE) --headless --convert-to pdf --outdir $(OUTPUT)/pdf/en $(OUTPUT)/docx/en/*.docx

check:
	$(UV) run --with pypdf python src/tools/check_ats.py

clean:
	@if [ -d $(OUTPUT) ]; then \
		destrito="$(OUTPUT)-arquivo-$$(date +%Y%m%d-%H%M%S)"; \
		mv "$(OUTPUT)" "$$destrito"; \
		echo "Saída movida para $$destrito (nada foi apagado)."; \
	fi
