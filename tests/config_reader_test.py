import pytest

from promaker.config_reader import ConfigError, make_config


config_lines = [
    "author=testUser",
    "description=Project description.",
    "email=test.email@mail.com",
    "license=MIT",
    "name=test_project",
    "option=package",
    "path=Project path",
    "repository=https://github.com/testUser/test_project.git",
    "source=src",
    "tests=tests",
    "versions=[3.7, 3.8, 3.9]",
]


def test_read_config():
    config = make_config(config_lines)
    assert config["author"] == "testUser"
    assert config["description"] == "Project description."
    assert config["email"] == "test.email@mail.com"
    assert config["license"] == "MIT"
    assert config["name"] == "test_project"
    assert config["option"] == "package"
    assert config["path"] == "Project path"
    assert config["repository"] == "https://github.com/testUser/test_project.git"
    assert config["source"] == "src"
    assert config["tests"] == "tests"
    assert config["versions"] == ["37", "38", "39"]

    cp1 = config_lines.copy()
    cp1[0] = "name"
    with pytest.raises(ConfigError):
        make_config(cp1)

    cp3 = config_lines.copy()
    cp3[3] = "email=invalid_email@"
    with pytest.raises(ConfigError):
        make_config(cp3)

    cp2 = config_lines.copy()
    cp2[5] = "option=invalid_option"
    with pytest.raises(ConfigError):
        make_config(cp2)
