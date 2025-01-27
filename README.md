# Theoretical Foundations of Buffer Stock Theory - REMARK

[![DOI](https://zenodo.org/badge/302430141.svg)](https://zenodo.org/badge/latestdoi/302430141)

The Endo directory contains code to reproduce the figures of the paper [Theoretical Foundations of Buffer Stock Saving](https://econ-ark.github.io/Endo/) by Christopher Carroll, and the LaTeX source to produce the paper once the figures have been created.

## Code 

Figures can be produced either:

#### Live in your browser using [MyBinder](https://mybinder.org): [![Binder](https://mybinder.org/badge_logo.svg)](http://econ-ark.org/materials/bufferstocktheory?launch)

#### Locally

If you want to reproduce the results locally, you will need python and pip.

##### In a local interactive [jupyter notebook](https://jupyter.org)
   1. Install the jupyter notebook tool per [Installation.md](https://github.com/econ-ark/REMARK)
   2. Download this repository using `git clone https://github.com/econ-ark/Endo` or a zip folder [using this link](https://github.com/econ-ark/Endo/archive/master.zip).
   3. Type `jupyter lab` at the command line
      - Click on `Endo-Dashboard.ipynb`; or 
      - Navigate to `Code/Python/Endo.ipynb`

##### Reproduce the figures and compile the paper locally using `nbreproduce`
   1. Install [nbreproduce](https://github.com/econ-ark/nbreproduce)
   2. Download this repository using `git clone https://github.com/econ-ark/Endo` or a zip folder [using this link](https://github.com/econ-ark/Endo/archive/master.zip).
   3. Execute `nbreproduce` from the command line.
	  
## Paper

The paper can be generated by compiling the LaTeX file `Endo.tex` using a standard distribution of LaTeX like TeXLive or Overleaf.
