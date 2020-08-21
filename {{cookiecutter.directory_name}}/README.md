# {{cookiecutter.directory_name}}

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black) [![pre-commit](https://img.shields.io/badge/pre--commit-enabled-brightgreen?logo=pre-commit&logoColor=white)](https://github.com/pre-commit/pre-commit) 



# FIRST THINGS TO DO ON CREATION (this section should not be seen by anyone on your repo, follow and remove it at the end!!!)

create a conda env with pre-commit installed: 
```sh
conda create -n {{cookiecutter.directory_name}} python=3.7
conda install -c conda-forge pre-commit #if you are not root, maybe you need to install git and openssh with conda
```

Once pre-commit installed run:
```sh
pre-commit install
```

Each time you'll commit, a pipeline will run to check your files (pep8 formatting, search for unused code...)


Last step is create an env.yml file in order to fix all python's modules and deps. 
To do that, you need to run:
```sh
conda env export > env.yaml
```
This file is mandatory for the installation script.

## Installation

To create a working env and setup all pre-commit hooks just run the installation script:
```sh
sh install.sh
```


## Usage
