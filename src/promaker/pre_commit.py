pre_commit_config = """repos:
  - repo: https://github.com/psf/black
    rev: 21.9b0
    hooks:
      - id: black
        args: [--safe]

  - repo: https://github.com/hadialqattan/pycln
    rev: v1.0.3
    hooks:
      - id: pycln
        args: [--all]

  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v4.0.1
    hooks:
      - id: check-yaml
      - id: check-xml
      - id: check-toml
      - id: check-json
      - id: check-docstring-first
      - id: end-of-file-fixer
      - id: trailing-whitespace
      - id: name-tests-test
      - id: check-added-large-files
      - id: pretty-format-json
      - id: debug-statements
      - id: requirements-txt-fixer
        language_version: python3

  - repo: https://github.com/PyCQA/flake8
    rev: 3.9.2
    hooks:
      - id: flake8
        language_version: python3

  - repo: https://github.com/asottile/pyupgrade
    rev: v2.29.0
    hooks:
      - id: pyupgrade
        args: [--py36-plus]

  - repo: local
    hooks:
      - id: pytest-check
        name: pytest-check
        entry: pytest
        language: system
        pass_filenames: false
        always_run: true
"""
