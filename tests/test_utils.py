import os
import pytest
import utils


@pytest.fixture
def os_fixture():
    return os.path.join('../data', 'operations.json')


def test_load_json(os_fixture):
    assert type(utils.load_json(os_fixture)) is list
