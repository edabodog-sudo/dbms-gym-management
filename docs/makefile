TEX=main.tex
OUT=out
PDF=$(OUT)/documentation.pdf

all: $(PDF)

$(PDF): $(TEX)
	mkdir -p $(OUT)
	pdflatex -output-directory=$(OUT) $(TEX)
	pdflatex -output-directory=$(OUT) $(TEX)
	mv $(OUT)/main.pdf $(PDF)

clean:
	rm -f $(OUT)/*.aux $(OUT)/*.log $(OUT)/*.toc $(OUT)/*.out

distclean:
	rm -rf $(OUT)
