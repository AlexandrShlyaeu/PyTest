import pytest


@pytest.mark.usefixtures('init_driver', scope='class')
class BaseTest:
    pass
