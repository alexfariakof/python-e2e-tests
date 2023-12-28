"""Test e2e Authentication With valid Account in Backend API"""
import requests


def test_api_authentication(config):
    api_endpoint = f"{config}/ControleAcesso/SignIn"
    print(api_endpoint)

    data = {
        "email": "teste@teste.com",
        "senha": "12345T!"
    }

    response = requests.post(api_endpoint, json=data)
    response.raise_for_status()
    resultado_autenticacao = response.json()

    assert "authenticated" in resultado_autenticacao and resultado_autenticacao[
        "authenticated"] is True
    assert "accessToken" in resultado_autenticacao
    assert "expiration" in resultado_autenticacao
    assert "message" in resultado_autenticacao and resultado_autenticacao["message"] == "OK"
