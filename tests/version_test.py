import pytest
from promaker.version import (
    classifier,
    dot_versions,
    py_versions,
    versions_str_to_list,
    version_depth,
)

v1 = "[3.6, 3.8, 3.9]"
v2 = "[3, 3.9,391]"
v3 = "2, 36, 27"
v4 = ""

v1_list = versions_str_to_list(v1)
v2_list = versions_str_to_list(v2)
v3_list = versions_str_to_list(v3)


def test_version_str_to_list():
    assert ["36", "38", "39"] == v1_list
    assert ["3", "39", "391"] == v2_list
    assert ["2", "27", "36"] == v3_list
    with pytest.raises(ValueError):
        assert versions_str_to_list(v4)


def test_py_versions():
    assert ["py36", "py38", "py39"] == py_versions(v1_list)
    assert ["py3", "py39", "py391"] == py_versions(v2_list)
    assert ["py2", "py27", "py36"] == py_versions(v3_list)


def test_dot_versions():
    assert ["3.6", "3.8", "3.9"] == dot_versions(v1_list)
    assert ["3", "3.9", "3.9.1"] == dot_versions(v2_list)
    assert ["2", "2.7", "3.6"] == dot_versions(v3_list)


def test_classifier():
    assert [
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ] == classifier(v1_list)
    assert [
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.9",
    ] == classifier(v2_list)
    assert [
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
    ] == classifier(v3_list)


def test_version_depth():
    assert ["3", "3", "3"] == version_depth(v1_list, 1)
    assert ["36", "38", "39"] == version_depth(v1_list, 2)
    assert ["36", "38", "39"] == version_depth(v1_list, 3)
    assert ["36", "38", "39"] == version_depth(dot_versions(v1_list), 3)
    with pytest.raises(ValueError):
        assert version_depth(v1_list, 4)
    with pytest.raises(ValueError):
        assert version_depth(v1_list, 0)
