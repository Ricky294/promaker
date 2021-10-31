from promaker.validators import (
    email_validator,
    option_validator,
    license_validator,
    versions_validator,
)


def test_email_validator():
    assert email_validator("test@gmail.com")
    assert email_validator("te.st@gmail.com")
    assert not email_validator("test@gmail")
    assert not email_validator("test.gmail.com")


def test_option_validator():
    assert option_validator("package")
    assert option_validator("project")
    assert not option_validator("test")


def test_license_validator():
    assert license_validator("Mit")
    assert license_validator("agpl-v3")
    assert license_validator("agplv3")
    assert license_validator("bsd-0_clause")
    assert license_validator("apache-2.0")
    assert not license_validator("xyz")
    assert not license_validator("1234-95")


def test_versions_validator():
    assert versions_validator("[3.8.1]")
    assert versions_validator("[381]")
    assert versions_validator("[381, 3.9.2, 2.7]")
    assert versions_validator("381, 3.9.2, 2.7")
    assert versions_validator("[3, 3.9.2, 2.7]")
    assert versions_validator("[3.1 , 3.9.2  ,  2.7 ]")
    assert not versions_validator("[381, 3.9.2.1, 2.7]")
