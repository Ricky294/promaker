from promaker.config_reader import make_config
from promaker.tox import generate_tox_ini

from config_reader_test import config_lines


def test_generate_tox():
    print(generate_tox_ini(make_config(config_lines)))
