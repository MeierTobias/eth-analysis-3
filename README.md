# ETHZ Analysis III

![action status](https://github.com/meiertobias/eth-analysis-3/actions/workflows/build_deploy.yml/badge.svg)

This repository contains the LaTex source of the Analysis III course summary.  
It was originally created by Benno Kaeslin, Linard Furck, Sandro Christen, Markus Fuchs, Andre Jauch in 2016 and extended by the contributors of this repository.

A pre-build pdf file can be downloaded here:

- [Analysis_III_full.pdf](https://meiertobias.github.io/eth-analysis-3/analysis_III_full.pdf)
- [Analysis_III.pdf (without examples)](https://meiertobias.github.io/eth-analysis-3/analysis_III.pdf)

## Getting-Started

After you cloned this repo there are two options to build the LaTeX files ether you [use the Docker Container](#docker-recommended) or build it with your [native installed LaTeX compile](#native-latex-compiler) of choice.
If you want a hassle-free way to work with our LaTeX project, we recommend using Docker.

### Docker (recommended)

1. Make sure you have Docker installed on your system. If you don't have it already, you can download and install it from the [official Docker website](https://www.docker.com/get-started/).

2. After you launched the docker daemon (started Docker Desktop) you can simply run execute the `./build_latex_local.sh` file to generate the pdf files. They are located in a newly created subfolder called `build`.  
(Most probably you have to change the execution permissions with `chmod +x build_latex_local.sh` before you are able to run the script for the first time.)

### Native LaTeX compiler

If you want to use your own native installed LaTeX compiler we recommend to use [TeXLive](https://www.tug.org/texlive/) which integrates well within visual studio code.

If you use the [LaTeX Workshop extension](vscode:extension/James-Yu.latex-workshop) you can add the following lines to your `.vscode/settings.json` file to configure the system:

Specify an output directory:

```json
"latex-workshop.latex.outDir": "../build",
```

Remove unnecessary build files:

```json
"latex-workshop.latex.clean.fileTypes" : [ "*.aux", "*.fls", "*.synctex.gz", "*.out", "*.log", "*.fdb_latexmk" ],
"latex-workshop.latex.autoClean.run": "onBuilt",
"latex-workshop.latex.clean.method": "glob",

// if using subfolder
"latex-workshop.latex.outDir": "../build",
"latex-workshop.latex.clean.subfolder.enabled": true,
```

To enable the LaTeX checker ChkTeX:

```json
"latex-workshop.linting.chktex.enabled": true, 
"latex-workshop.linting.chktex.exec.args": ["-wall","-n8","-n13","-n21","-n22","-n30","-n46","-e16","-q"],
```

To get more information about the different warnings search for your warning code in the ChkTeX [documentation](https://mirror.init7.net/ctan/support/chktex/ChkTeX.pdf). If you want to disable a checker warning on a specific line you can add `% chktex ##` to the end of the line with the warning number you want to suppress.

## Setup on macOS
This repository is configured for Git [LFS](https://git-lfs.com/) (Large File Storage). If you don't already have it installed run `brew install git-lfs` or check the linked website to install it.

To use the formatter by LaTeX Workshop install `brew install latexindent`.

## Contributing

Feel free to fork this repository and create a pull request to integrate your corrections and extensions.

## Acknowledgements

Thanks to *S.* for creating this wonderful AMIV/ETHZ summaries LaTeX template which can be downloaded [here](https://de.overleaf.com/latex/templates/amiv-slash-ethz-summaries-template-landscape/trggddjtjhqr).

## License

Distributed under the MIT License. See [LICENSE](LICENSE) for more information.
