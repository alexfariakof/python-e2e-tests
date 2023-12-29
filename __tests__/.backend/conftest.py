import pytest
import requests
from config.environments import get_config


@pytest.fixture
def config(request):
    env = request.config.getoption("--env")
    return get_config(env)["api"]


def get_token_access(config):
    api_endpoint = f"{config}/ControleAcesso/SignIn"

    data = {
        "email": "teste@teste.com",
        "senha": "12345T!"
    }

    response = requests.post(api_endpoint, json=data)
    response.raise_for_status()
    resultado_autenticacao = response.json()
    assert "accessToken" in resultado_autenticacao
    return resultado_autenticacao["accessToken"]
