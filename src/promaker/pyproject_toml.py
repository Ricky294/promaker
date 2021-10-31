def get_pyproject_toml(args):
    return f"""[build-system]
requires = ["setuptools>=42", "wheel"]
build-backend = "setuptools.build_meta"

[tool.pytest.ini_options]
addopts = "--cov={args["name"]}"
testpaths = [
    "{args["tests"]}",
]"""
