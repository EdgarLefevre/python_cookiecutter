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
