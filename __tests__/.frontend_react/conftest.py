import pytest
from config.environments import get_config


@pytest.mark.react
@pytest.fixture
def config(request):
    env = request.config.getoption("--env")
    base_url = get_config(env)["react"]
    return base_url
