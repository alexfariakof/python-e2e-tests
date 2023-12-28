"""Test e2e Create Account Backend API"""
from faker import Faker
import requests

fake = Faker()
API_END_POINT = "ControleAcesso"


def test_api_create_account_success(config):
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
    assert "message" in result and result["message"] is True


def test_api_create_account_invalid_email(config):
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
    assert "message" in result and result["message"] == "Email inválido!"


def test_api_create_account_password_mismatch(config):
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
    assert "message" in result and result["message"] == "Senha e Confirma Senha são diferentes!"


def test_api_create_account_user_exists(config):
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
    result = response.json()

    # Assert
    assert "message" in result and result["message"] == "Não foi possível realizar o cadastro."