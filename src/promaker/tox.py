from typing import List, Any, Dict

from .version import py_versions, dot_versions


def __generate_tox(versions: List[str]) -> str:
    envlist = ", ".join(py_versions(versions)) + ", flake8"

    return f"""[tox]
minversion = 3.8.0
envlist = {envlist}
isolated_build = true
"""


def __generate_gh_actions(versions: List[str]) -> str:

    concat_versions = [
        dv + ": " + pv for dv, pv in zip(dot_versions(versions), py_versions(versions))
    ]
    concat_versions[0] += ", flake8"

    linesep_tab = "\n\t"

    return f"""[gh-actions]
python =
    {linesep_tab.join(concat_versions)}
"""


def __generate_testenv() -> str:
    return """[testenv]
setenv =
    PYTHONPATH = {toxinidir}
deps =
    -r{toxinidir}{/}requirements.txt
    -r{toxinidir}{/}requirements_dev.txt
commands =
    pytest --basetemp={envtmpdir}
"""


def __generate_testenv_flake8(src_dir: str, tests_dir: str) -> str:
    return f"""[testenv:flake8]
basepython = python3.8
deps = flake8
commands = flake8 {src_dir} {tests_dir}
"""


def generate_tox_ini(config: Dict[str, Any]):
    tox_ini = (
        __generate_tox(config["versions"]),
        __generate_gh_actions(config["versions"]),
        __generate_testenv(),
        __generate_testenv_flake8(config["source"], config["tests"]),
    )
    return "\n".join(tox_ini)
