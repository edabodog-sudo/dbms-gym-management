PDF=main.pdf
TEX=main.tex

all: $(PDF)

$(PDF): $(TEX)
	pdflatex $(TEX)
	pdflatex $(TEX)

clean:
	rm -f *.aux *.log *.out *.toc

distclean: clean
	rm -f $(PDF)

