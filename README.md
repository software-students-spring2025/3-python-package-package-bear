![Python build & test](https://github.com/software-students-spring2025/3-python-package-package-bear/actions/workflows/build.yaml/badge.svg)

# Python Package Exercise: Package Bear 🐻🐻‍❄️🐼

### Contents
#### buildabear.py
Contains all functions used to initialize, interact, and play with bear.

## Team Members
Jasmine Fan https://github.com/jasmine7310

Sophia Wang https://github.com/s-m-wang

Tadelin De Leon https://github.com/TadelinD

Alex Wang https://github.com/alw9411

## Package Description
Your own command line bear!

## Configuration
Before installing if you don't have pipenv:

```
pip install pipenv
```

Then Activate pipenv:
```
pipenv shell
```

On a new python project run:
```
pip install buildabear-jasmine7310-s-m-wang-TadelinD-alw9411
```

First use the command below for the welcome message
```
python -m buildabearpackage
```

Then use the command below to initialize the package
```
python -m buildabearpackage start
```

## Interacting with Pet
```
python -m buildabearpackage status
python -m buildabearpackage "change name"
python -m buildabearpackage work X  # X being an integer number!!
python -m buildabearpackage feed
python -m buildabearpackage clean
python -m buildabearpackage play
python -m buildabearpackage "buy food" X  # X being an integer number!!
```
## Set Up Environment Variables and Starter Data
To use the package you are going to need to create a file called Data.txt in the same directory in which you will use the package. 

In this txt file you will need to copy and paste the following:
```
happiness:100
hunger:100
cleanliness:100
food:10
budget:1000
name:Bear
initialized:False
lastChecked:0
```
Make sure that there is no new line after inputting this information.

## Link to Our Package Page
[Package Bear: buildabear](https://pypi.org/project/buildabear-jasmine7310-s-m-wang-TadelinD-alw9411/)

## Project Contribution

### Virtual Environment Setup
```
pip install pipenv
pipenv install pytest
pytest
pipenv shell
```
### Uploading to Pypi using Twine
If there are *.egg-info and dist directories delete them before proceeding. Be sure to update version number.

```
pip install build twine
python -m build
twine upload dist/*
```