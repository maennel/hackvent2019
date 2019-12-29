#!/usr/bin/env bash
# Requires pandoc 2.9.1

mkdir -p tmp
rm -f tmp/*

echo "# Copying files"
cp introduction.md pandoc.css style.pandoc metadata.yaml tmp/
for d in ./*; do
	[ -d $d ] || continue
	[[ "${d}" == "./tmp" ]] && continue
	cp ${d}/description.md tmp/${d}_description.md
	cp ${d}/*.{zip,jpg,jpeg,png,data} tmp/ 2>/dev/null
done

cd tmp

echo "# Generating documentation"
name="hackvent2019-ludus"


# For argument details, check https://learnbyexample.github.io/tutorial/ebook-generation/customizing-pandoc/
pandoc --from gfm+emoji --to pdf --standalone --toc --toc-depth=2 -o ${name}.pdf --include-in-header=style.pandoc --highlight-style=tango --wrap=auto --css=pandoc.css introduction.md *description.md --metadata-file=metadata.yaml --pdf-engine=xelatex
pandoc --from gfm --to html5 --standalone --toc --toc-depth=2 -o ${name}.html --wrap=auto --highlight-style=tango --css=pandoc.css --metadata-file=metadata.yaml introduction.md *description.md

cd ..

echo "# Done"

