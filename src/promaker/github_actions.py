from typing import Dict, Any


def get_release_github_action(args: Dict[str, Any]):
    return f"""name: Publish 🐍 📦 to PyPI

on:
  - push
  - pull_request

jobs:
  test:
    runs-on: "ubuntu-latest"

    steps:
      - name: Checkout source
        uses: actions/checkout@v2

      - name: Set up Python 3.8
        uses: actions/setup-python@v1
        with:
          python-version: 3.8

      - name: Install build dependencies
        run: python -m pip install build wheel

      - name: Build distributions
        shell: bash -l {0}
        run: python setup.py sdist bdist_wheel

      - name: Publish 📦 to PyPI
        if: github.event_name == 'push' && startsWith(github.ref, 'refs/tags')
        uses: pypa/gh-action-pypi-publish@release/v1
        with:
          user: __token__
          password: ${{ secrets.PYPI_API_TOKEN }}
"""


def get_tests_github_action(args: Dict[str, Any]):
    return f"""name: Tests

on:
  - push
  - pull_request

jobs:
  test:
    runs-on: ${{ matrix.os }}
    strategy:
      matrix:
        os: [ubuntu-latest, windows-latest]
        python-version: {list(set(".".join(version.split(".")[0:-1]) for version in args["versions"]))}

    steps:
    - uses: actions/checkout@v2
    - name: Set up Python ${{ matrix.python-version }}
      uses: actions/setup-python@v2
      with:
        python-version: ${{ matrix.python-version }}
    - name: Install dependencies
      run: |
        python -m pip install --upgrade pip
        pip install tox tox-gh-actions
    - name: Test with tox
      run: tox
"""
