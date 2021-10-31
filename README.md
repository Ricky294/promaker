# Promaker

Python library to create projects with CI/CD features.

## First steps after creating a project

### pre-commit

* ```pip install pre-commit```

* ```pre-commit install```

### setup.cfg

Change it to fit package requirements.

### Others

* Review requirements.txt

* Review requirements_dev.txt

## Publishing to PYPI

* 0.1 Create a PYPI package.
* 0.2 Create an API token for the package.
* 0.3 Create a project secret named: **PYPI_API_TOKEN** with the API token value.

1. Change version in setup.cfg

2. git add .

3. git commit (Make sure pre-commit git hooks are not **Failed** -
   if **Failed**, fix issues and repeat step number 2 and 3)

4. git switch branch (e.g., git switch main)

5. git merge branch (e.g., git switch develop)

6. git tag -a version -m "msg" (e.g., git tag -a v0.1.0 -m "Version 0.1.0 release")

7. git push origin branch (e.g., git push origin main)

8. git push tag (e.g., git push v0.1.0)

## Badge examples

Create badges: https://shields.io/

![Tests](https://github.com/Ricky294/promaker/actions/workflows/tests.yaml/badge.svg)
![License](https://img.shields.io/pypi/l/promaker?label=License)
![Version](https://img.shields.io/pypi/v/promaker?label=Latest)
![Versions](https://img.shields.io/pypi/pyversions/promaker?label=Python)
![Repo size](https://img.shields.io/github/repo-size/Ricky294/promaker?label=Size)
