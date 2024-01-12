#!/bin/sh
COMMAND="latexmk -pdf -cd -interaction=nonstopmode -file-line-error -jobname=analysis_III_full_portrait -outdir=../build ./src/main.tex ; 
    sed '0,/{1}/s//{0}/' -i src/headers/flags.tex ; 
    latexmk -pdf -cd -interaction=nonstopmode -file-line-error -jobname=analysis_III_full_landscape -outdir=../build ./src/main.tex ;
    sed '0,/{1}/s//{0}/' -i src/headers/flags.tex ;
    latexmk -pdf -cd -interaction=nonstopmode -file-line-error -jobname=analysis_III_landscape -outdir=../build ./src/main.tex ;
    sed '0,/{0}/s//{1}/' -i src/headers/flags.tex ;
    latexmk -pdf -cd -interaction=nonstopmode -file-line-error -jobname=analysis_III_portrait -outdir=../build ./src/main.tex ;
    sed '0,/{0}/s//{1}/' -i src/headers/flags.tex"
exec docker run --rm -i --user="$(id -u):$(id -g)" --net=none -v "$PWD":/usr/src/app -w /usr/src/app texlive/texlive:latest sh -c "$COMMAND"