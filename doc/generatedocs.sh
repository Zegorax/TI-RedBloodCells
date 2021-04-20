#!/bin/bash

echo "[0/1] Generating all documents..."

# Main report
echo "[1/1] Generate main report ..."
cd report
pandoc report.md ./chap/chap*.md -o ../HEArc-TI-RedBloodCells-JDSF_LV_LF.pdf --from markdown --template ../theme/eisvogel.tex --listings --filter pandoc-citeproc

# Done job !
echo "Done !"
cd ..
