from typing import Any, Dict


def get_readme(args: Dict[str, Any]):
    return f"""# {args["name"]}

---

![Tests]({args["repository"]}/actions/workflows/tests.yaml/badge.svg)
![License](https://img.shields.io/pypi/l/{args["name"]}?label=License)
![Version](https://img.shields.io/pypi/v/{args["name"]}?label=Latest)
![Versions](https://img.shields.io/pypi/pyversions/{args["name"]}?label=Python)
![Repo size](https://img.shields.io/github/repo-size/{args["author"]}/{args["name"]}?label=Size)

{args["description"]}

TODO: Customize README."""
