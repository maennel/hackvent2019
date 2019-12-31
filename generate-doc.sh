#!/usr/bin/env bash
# Requires pandoc 2.9.1
WORKDIR=docs

mkdir -p ${WORKDIR}
rm -f ${WORKDIR}/*

echo "# Copying files"
cp introduction.md pandoc.css style.pandoc metadata.yaml ${WORKDIR}/
for d in ./*; do
	[ -d $d ] || continue
	[[ "${d}" == "./${WORKDIR}" ]] && continue
	cp ${d}/description.md ${WORKDIR}/${d}_description.md
	cp ${d}/*.{zip,jpg,jpeg,png,data} ${WORKDIR}/ 2>/dev/null
done

cd ${WORKDIR}

echo "# Generating documentation"
name="hackvent2019-ludus"


# For argument details, check https://learnbyexample.github.io/tutorial/ebook-generation/customizing-pandoc/
pandoc --from gfm+emoji --to pdf --standalone --toc --toc-depth=2 -o ${name}.pdf --include-in-header=style.pandoc --highlight-style=tango --wrap=auto --css=pandoc.css introduction.md *description.md --metadata-file=metadata.yaml --pdf-engine=xelatex
pandoc --from gfm --to html5 --standalone --toc --toc-depth=2 -o index.html --wrap=auto --highlight-style=tango --css=pandoc.css --metadata-file=metadata.yaml introduction.md *description.md

cd ..

echo "# Done"
