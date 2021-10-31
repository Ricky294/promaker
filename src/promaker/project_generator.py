import argparse
import os.path
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path
from typing import Any, Dict, Tuple

from .github_actions import get_tests_github_action, get_release_github_action
from .gitignore import get_gitignore
from .license_ import supported_licenses, get_license, get_license_file_name
from .pre_commit import pre_commit_config
from .config_reader import make_config, read_lines
from .version import versions_str_to_list, dot_versions, classifier
from .pyproject_toml import get_pyproject_toml
from .readme import get_readme
from .requirements import dev_requirements
from .setup import setup_cfg, setup_py
from .tox import generate_tox_ini


def create_folder(*args: str):
    p = os.path.join(*args)
    Path(p).mkdir(parents=True, exist_ok=True)
    return os.path.join(p)


def add_arguments(parser: argparse.ArgumentParser):
    parser.add_argument(
        "-a", "--author", help="Author of this package/project.", required=True
    )
    parser.add_argument(
        "-d",
        "--description",
        help="Project description",
        default="TODO: Write a project description.",
    )
    parser.add_argument(
        "-e",
        "--email",
        help="Author's email address.",
        default="TODO: Your email address.",
    )
    parser.add_argument(
        "-l",
        "--license",
        help="License to use.",
        choices=supported_licenses,
        default="MIT",
    )
    parser.add_argument("-n", "--name", help="Package name.", required=True)
    parser.add_argument(
        "-o",
        "--option",
        help="Value: 'package' or 'project'",
        choices=("package", "project"),
        default="package",
    )
    parser.add_argument("-p", "--path", required=True)
    parser.add_argument(
        "-r", "--repository", help="Remote repository url.", required=True
    )
    parser.add_argument("-s", "--source", help="Source folder's name.", default="src")
    parser.add_argument("-t", "--tests", help="Test folder location.", default="tests")
    parser.add_argument(
        "-v",
        "--versions",
        action="append",
        help="List of supported python versions. e.g., 3.8",
        required=True,
    )


def _write(args: Tuple[str]):
    with open(os.path.join(*args[1:]), "w") as f:
        f.write(args[0])


def generate_project(args: Dict[str, Any]):

    root_folder = create_folder(args["path"], args["name"])
    # test_folder = create_folder(root_folder, args["tests"])
    # src_folder = create_folder(root_folder, args["source"])
    github_actions_folder = create_folder(root_folder, ".github", "workflows")

    args["classifiers"] = classifier(
        dot_versions(versions_str_to_list(args["versions"]))
    )

    contents = [
        (pre_commit_config, root_folder, ".pre-commit-config.yaml"),
        (get_gitignore("python", "pycharm"), root_folder, ".gitignore"),
        (dev_requirements, root_folder, "requirements_dev.txt"),
        ("", root_folder, "requirements.txt"),
        (generate_tox_ini(args), root_folder, "tox.ini"),
        (get_pyproject_toml(args), root_folder, "pyproject.toml"),
        (setup_py, root_folder, "setup.py"),
        (setup_cfg(args), root_folder, "setup.cfg"),
        (
            get_license(args["license"], args["author"]),
            root_folder,
            get_license_file_name(args["license"]),
        ),
        (get_readme(args), root_folder, "README.md"),
        (get_tests_github_action(args), github_actions_folder, "tests.yaml"),
        (get_release_github_action(args), github_actions_folder, "release.yaml"),
    ]

    with ThreadPoolExecutor(max_workers=4) as exe:
        exe.map(_write, contents)


def main():
    if os.path.isfile("project_generator.cfg"):
        lines = read_lines("project_generator.cfg")
        args = make_config(lines)
    else:
        parser = argparse.ArgumentParser()
        add_arguments(parser)

        namespace = parser.parse_args()
        args = namespace.__dict__

    unique_versions = list(set(args["versions"]))
    unique_versions.sort()
    args["versions"] = unique_versions

    generate_project(args)


if __name__ == "__main__":
    main()
