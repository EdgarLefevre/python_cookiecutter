# Python Cookie Cutter

This is a template for python projects.


## Installation
```sh
pip install cookiecutter
```

Or with conda: 
```sh
conda install -c conda-forge cookiecutter
```

##  Usage
First, create a new github repo, do not check `Initialize this repository with a README`.

Then we will call cookiecutter in order to download the template:

Over SSH :
```sh
cookiecutter git@github.com:EdgarLefevre/python_cookiecutter.git
```

Over https:
```sh
cookiecutter https://github.com/EdgarLefevre/python_cookiecutter.git
```

Once everything is downloaded, run git commands:
```sh
git init
git remote add origin git@github.com:YOURNAME/YOURREPO.git
git add *
git commit -am "First commit"
git push -u origin master
```
## Architecture


## Pre-commit

Along side with this template, a [pre-commit](pre-commit.com) pipeline is setup.
Once installed, this pipeline will run each time you do a commit, the main purpose of this pipeline is to check the code (style formating, imports, unused function...) and other things such as the conda environement file. The linters that we use here are mostly [flake8](https://flake8.pycqa.org/en/latest/) and [black](https://github.com/psf/black). 

The hooks are setup in `.pre-commit-config.yaml`, if you want to add (or remove) some, you have to edit this file.

Several usefull commands:
```sh
pre-commit install # install hooks
pre-commit clean # clean hooks (usefull when a hook is updated)
pre-commit run --all-files # run all hooks on all files
```

> Note: to avoid pre-commit running on a commit just do `git commit -am "msg" --no-verify` but this not really recommended.
