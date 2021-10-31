from typing import List


def versions_str_to_list(versions: str):
    ret = [
        version.strip().replace(".", "")
        for version in versions.replace("[", "").replace("]", "").split(",")
    ]

    if ret == [""]:
        raise ValueError("Parameter must contain at least one version!")

    ret.sort()
    return ret


def py_versions(versions: list):
    return ["py" + version for version in versions]


def dot_versions(versions: list):
    return [".".join(version) for version in versions]


def version_depth(versions: list, depth: int):
    if depth > 3 or depth < 1:
        raise ValueError("Version depth must be between 1 and 3.")

    return [version.replace(".", "")[0:depth] for version in versions]


def classifier(versions: List[str]):
    pre_str = "Programming Language :: Python :: "
    only_str = " :: Only"
    ret = []

    major_versions = [version[0] for version in versions]
    major_versions.sort()
    major_versions = set(major_versions)

    ret.extend([pre_str + major_version for major_version in list(major_versions)])
    if len(major_versions) == 1:
        ret.append(pre_str + major_versions.pop() + only_str)

    ret.extend([pre_str + version[0:3] for version in dot_versions(versions)])

    ret = list(set(ret))
    ret.sort()
    return ret
