from typing import List, Dict, Any

from .validators import (
    license_validator,
    email_validator,
    option_validator,
    versions_validator,
)
from .version import versions_str_to_list


class ConfigError(Exception):
    def __init__(self, msg: str):
        self.msg = msg

    @classmethod
    def missing_required_key(cls, key: str):
        return cls(f"You forgot to define {key} in config file.")

    @classmethod
    def invalid_value(cls, key: str):
        return cls(f"Invalid value defined for {key!r} in config file.")


config_characteristics = {
    "author": {"required": True, "default": None},
    "description": {"required": False, "default": "TODO: Write a description."},
    "email": {
        "required": False,
        "default": "TODO: Add your email for contact.",
        "validator": email_validator,
    },
    "license": {"required": True, "default": "MIT", "validator": license_validator},
    "name": {"required": True, "default": None},
    "option": {"required": True, "default": "package", "validator": option_validator},
    "path": {"required": True, "default": None},
    "repository": {"required": False},
    "source": {"required": True, "default": "src"},
    "tests": {"required": True, "default": "tests"},
    "versions": {"required": True, "default": None, "validator": versions_validator},
}


def filter_empty(lst: List[str]):
    return [i.strip() for i in lst if i.strip()]


def filter_comment(lst: List[str]):
    return [i for i in lst if not i.strip().startswith("#")]


def read_lines(path: str):
    with open(path, encoding="UTF-8") as f:
        return f.readlines()


def make_config(lines: List[str]) -> Dict[str, Any]:
    lines = filter_comment(filter_empty(lines))

    try:
        parsed_lines = {
            line.split("=")[0].strip(): line.split("=")[1].strip() for line in lines
        }
    except IndexError:
        raise ConfigError("Config format must be: key=value line by line.")

    for name, characteristics in config_characteristics.items():
        if name not in parsed_lines.keys() and characteristics["required"]:
            raise ConfigError.missing_required_key(name)
        if "validator" in characteristics:
            if not characteristics["validator"](parsed_lines[name]):
                raise ConfigError.invalid_value(name)

    parsed_lines["versions"] = versions_str_to_list(parsed_lines["versions"])
    return parsed_lines
