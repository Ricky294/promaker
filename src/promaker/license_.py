import os.path
from datetime import datetime


supported_licenses = (
    "mit",
    "apache-2.0",
    "bsd-3-clause",
    "bsd-2-clause",
    "bsd-1-clause",
    "bsd-0-clause",
    "gpl-v3",
    "agpl-v3",
    "lgpl-v3",
    "mpl-2.0",
    "bsl-1.0",
    "unlicense",
)


def get_license(name: str, author: str) -> str:
    """
    :param name: License name.
    :param author: Project author.
    :return: License text
    """

    name = name.lower().replace("-", "").replace(".", "").replace("_", "")
    license_path = os.path.join("src", "promaker", "resources", "licenses", name)

    if not os.path.isfile(license_path):
        raise ValueError(
            f"License {name} is not supported.\n"
            f"Supported licenses: {supported_licenses}"
        )

    with open(license_path) as f:
        license_text = f.read()

    return license_text.replace("{year}", str(datetime.now().year)).replace(
        "{copyright_holder}", author
    )


def get_license_file_name(name: str) -> str:
    """
    :param name: License name.
    :return: File name of the license.
    """

    if name.lower() == "unlicense":
        return "UNLICENSE"
    return "LICENSE"
