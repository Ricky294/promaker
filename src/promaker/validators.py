import re

from .license_ import supported_licenses


def license_validator(license_str: str) -> bool:
    license_str = license_str.replace("_", "").replace("-", "").replace(".", "").lower()
    licenses = [
        lc.replace("_", "").replace("-", "").replace(".", "").lower()
        for lc in supported_licenses
    ]

    return license_str in licenses


def email_validator(email_str: str) -> bool:
    return (
        re.search(r"[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", email_str)
        is not None
    )


def option_validator(option_str: str) -> bool:
    return option_str == "package" or option_str == "project"


def versions_validator(versions_str: str) -> bool:
    versions_str = versions_str.replace("[", "").replace("]", "")

    versions_no_dot = [
        version.replace(".", "").strip() for version in versions_str.split(",")
    ]
    return all(len(v) <= 3 for v in versions_no_dot) and all(
        v.isnumeric() for v in versions_no_dot
    )
