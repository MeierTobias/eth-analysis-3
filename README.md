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

If you use the [LaTeX Workshop extension](vscode:extension/James-Yu.latex-workshop) you can add the following line to your `.vscode/settings.json` file to specify the output directory :  
`"latex-workshop.latex.outDir": "../build",`

## Contributing

Feel free to fork this repository and create a pull request to integrate your corrections and extensions.

## Acknowledgements

Thanks to *S.* for creating this wonderful AMIV/ETHZ summaries LaTeX template which can be downloaded [here](https://de.overleaf.com/latex/templates/amiv-slash-ethz-summaries-template-landscape/trggddjtjhqr).

## License

Distributed under the MIT License. See [LICENSE](LICENSE) for more information.
