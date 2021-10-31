from typing import Any, Dict

from .license_ import get_license_file_name


def setup_cfg(args: Dict[str, Any]):
    newline_tab = "\n\t"
    return f"""[metadata]
name = {args["name"]}
description = {args["description"]}
author = {args["author"]}
author_email = {args["email"]}
license = {args["license"].upper()}
license_file = {get_license_file_name(args["license"])}
platforms = unix, linux, osx, cygwin, win32
url = {args["repository"]}
classifiers =
    {newline_tab.join(args['classifiers'])}

[options]
packages =
    {args["name"]}

package_dir =
    ={args["source"]}
test_suite = {args["tests"]}
include_package_data = True
zip_safe = False

[options.extras_require]
testing =
    pytest>=6.0
    pytest-cov>=2.0
    flake8>=3.9
    tox>=3.24

[options.package_data]
{args["name"]} = py.typed

[flake8]
max-line-length = 120
"""


setup_py = """from setuptools import setup

if __name__ == '__main__':
    setup()
"""
