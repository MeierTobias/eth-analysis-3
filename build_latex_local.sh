#!/bin/sh
COMMAND="latexmk -pdf -cd -interaction=nonstopmode -file-line-error -jobname=analysis_III_full -outdir=../build ./src/main.tex ; 
    sed 's/^.\{1\}//g' -i src/headers/flags.tex ; 
    latexmk -pdf -cd -interaction=nonstopmode -file-line-error -jobname=analysis_III -outdir=../build ./src/main.tex ; 
    sed 's/^/%/' -i src/headers/flags.tex"
exec docker run --rm -i --user="$(id -u):$(id -g)" --net=none -v "$PWD":/usr/src/app -w /usr/src/app texlive/texlive:latest sh -c "$COMMAND"