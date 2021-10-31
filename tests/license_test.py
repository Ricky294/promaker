from datetime import datetime

from promaker.license_ import get_license, get_license_file_name


def test_get_license():
    license_text = get_license("BSD-2-clause", "John Doe")
    this_year = str(datetime.now().year)

    assert this_year in license_text
    assert "John Doe" in license_text


def test_get_license_file_name():
    assert "LICENSE" == get_license_file_name("BSL-1.0")
    assert "LICENSE" == get_license_file_name("AGPL-v3")
    assert "UNLICENSE" == get_license_file_name("unlicense")
