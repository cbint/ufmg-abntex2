all: exemplo.pdf exemplo.tex

exemplo.pdf: exemplo.md exemplo.yaml
	pandoc exemplo.yaml exemplo.md --template=template_ufmg.tex \
	--from markdown+raw_html+smart \
	--pdf-engine=pdflatex \
	--citeproc \
	--filter filtro_citacao.py \
	--top-level-division=chapter \
	-o out/exemplo.pdf

exemplo.tex: exemplo.md exemplo.yaml
	pandoc exemplo.yaml exemplo.md --template=template_ufmg.tex \
	--from markdown+raw_html+smart \
	--pdf-engine=xelatex \
	--citeproc \
	--filter filtro_citacao.py \
	--top-level-division=chapter \
	-o out/exemplo.tex

clean:
	rm -rf out/*
