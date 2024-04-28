"""Test e2e Create Account Backend API"""
from faker import Faker
import requests

fake = Faker()
API_END_POINT = "ControleAcesso"


def test_api_create_account_success(config: str):
    # Arrange
    password = fake.password()
    data = {
        "nome": fake.first_name(),
        "sobreNome": fake.last_name(),
        "telefone": fake.phone_number(),
        "email": fake.email(),
        "senha": password,
        "confirmaSenha": password,
    }

    # Act
    response = requests.post(f"{config}/{API_END_POINT}", json=data)
    response.raise_for_status()
    result = response.json()

    # Assert
    assert result is not None
    assert result is True


def test_api_create_account_invalid_email(config: str):
    # Arrange
    password = fake.password()
    data = {
        "nome": fake.first_name(),
        "sobreNome": fake.last_name(),
        "telefone": fake.phone_number(),
        "email": "email_invalido",
        "senha": password,
        "confirmaSenha": password,
    }

    # Act
    response = requests.post(f"{config}/{API_END_POINT}", json=data)
    result = response.json()

    # Assert
    assert result is not None
    assert "errors" in result
    assert "Email" in result["errors"]
    assert result["errors"]["Email"][0] == "O campo Email é inválido."


def test_api_create_account_password_mismatch(config: str):
    # Arrange
    data = {
        "nome": fake.first_name(),
        "sobreNome": fake.last_name(),
        "telefone": fake.phone_number(),
        "email": fake.email(),
        "senha": fake.password(),
        "confirmaSenha": fake.password(),
    }

    # Act
    response = requests.post(f"{config}/{API_END_POINT}", json=data)
    result = response.json()

    # Assert
    assert result is not None
    assert "errors" in result
    assert result["errors"][""][0] == "Senha e Confirma Senha são diferentes!"


def test_api_create_account_user_exists(config: str):
    # Arrange
    password = fake.password()
    data = {
        "nome": fake.first_name(),
        "sobreNome": fake.last_name(),
        "telefone": fake.phone_number(),
        "email": "teste@teste.com",
        "senha": password,
        "confirmaSenha": password,
    }

    # Act
    response = requests.post(f"{config}/{API_END_POINT}", json=data)
    
    # Assert
    assert response.status_code == 400