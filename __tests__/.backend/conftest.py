import pytest
from config.environments import get_config


@pytest.fixture
def config(request):
    env = request.config.getoption("--env")
    return get_config(env)["api"]
