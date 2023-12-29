"""Test E2E Backend API Receita Endpoint"""
from conftest import get_token_access
from faker import Faker
import requests

fake = Faker()
API_END_POINT = "Receita"


def test_create_receita(config):
    """ Test POST Receita Endpoint """
    api_endpoint = f"{config}/{API_END_POINT}"

    new_receita = {
        "id": 0,
        "data": fake.date_time_this_decade().isoformat(),
        "descricao": fake.sentence(),
        "valor": f'{fake.pydecimal(left_digits=4, right_digits=2, positive=True)}',
        "categoria": {
            "id": 22,
            "descricao": "Salário",
            "idTipoCategoria": 2
        }
    }

    print(new_receita)
    headers = {
        "Authorization": f"Bearer {get_token_access(config)}"
    }

    response = requests.post(api_endpoint, json=new_receita, headers=headers)
    response.raise_for_status()

    result = response.json()
    assert "message" in result
    assert result["message"] is True
    assert "receita" in result
    created_receita = result["receita"]

    # Add assertions based on your specific response structure
    assert "data" in created_receita
    assert "valor" in created_receita
    assert "categoria" in created_receita
    assert "id" in created_receita["categoria"]
    assert "descricao" in created_receita["categoria"]
    assert "idTipoCategoria" in created_receita["categoria"]
    assert created_receita["categoria"]["id"] == 22
    assert created_receita["categoria"]["descricao"] == new_receita["categoria"]["descricao"]
    assert created_receita["categoria"]["idTipoCategoria"] == 2


def test_update_receita(config):
    """ Test PUT Receita Endpoint """
    api_endpoint = f"{config}/{API_END_POINT}"

    # Creating a new receita to be updated later
    new_receita = {
        "id": 0,
        "data": fake.date_time_this_decade().isoformat(),
        "descricao": fake.sentence(),
        "valor": f'{fake.pydecimal(left_digits=4, right_digits=2, positive=True)}',
        "categoria": {
            "id": 22,
            "descricao": "Salário",
            "idTipoCategoria": 2
        }
    }

    headers = {
        "Authorization": f"Bearer {get_token_access(config)}"
    }

    response = requests.post(api_endpoint, json=new_receita, headers=headers)
    response.raise_for_status()
    created_receita = response.json()

    result = response.json()
    assert "message" in result
    assert result["message"] is True
    assert "receita" in result
    created_receita = result["receita"]

    # Updating the receita
    updated_receita = {
        "id": created_receita["id"],
        "data": fake.date_time_this_decade().isoformat(),
        "descricao": fake.sentence(),
        "valor": f'{fake.pydecimal(left_digits=4, right_digits=2, positive=True)}',
        "categoria": {
            "id": 22,
            "descricao": "Salário",
            "idTipoCategoria": 2
        }
    }

    response = requests.put(api_endpoint, json=updated_receita, headers=headers)
    response.raise_for_status()

    assert response.status_code == 200
    updated_receita = response.json()
    assert "message" in updated_receita
    assert updated_receita["message"] is True
    assert "receita" in updated_receita
    updated_receita = updated_receita["receita"]

    # Add assertions based on your specific response structure
    assert "data" in updated_receita
    assert "valor" in updated_receita
    assert "categoria" in updated_receita
    assert "id" in updated_receita["categoria"]
    assert "descricao" in updated_receita["categoria"]
    assert "idTipoCategoria" in updated_receita["categoria"]
    assert updated_receita["categoria"]["id"] == 22
    assert updated_receita["categoria"]["descricao"] == new_receita["categoria"]["descricao"]
    assert updated_receita["categoria"]["idTipoCategoria"] == 2


def test_delete_receita(config):
    """ Test DELETE Receita Endpoint"""
    api_endpoint = f"{config}/{API_END_POINT}"

    # Creating a new receita to be deleted later
    new_receita = {
        "id": 0,
        "data": fake.date_time_this_decade().isoformat(),
        "descricao": fake.sentence(),
        "valor": f'{fake.pydecimal(left_digits=4, right_digits=2, positive=True)}',
        "categoria": {
            "id": 22,
            "descricao": "Salário",
            "idTipoCategoria": 2
        }
    }

    headers = {
        "Authorization": f"Bearer {get_token_access(config)}"
    }

    response = requests.post(api_endpoint, json=new_receita, headers=headers)
    response.raise_for_status()
    result = response.json()
    assert "message" in result
    assert result["message"] is True
    assert "receita" in result
    created_receita = result["receita"]

    # Deleting the receita
    response = requests.delete(f"{api_endpoint}/{created_receita['id']}", headers=headers)
    response.raise_for_status()

    assert response.status_code == 200
    deleted_receita = response.json()
    assert "message" in deleted_receita
    assert deleted_receita["message"] is True


def test_get_receitas(config):
    """ Test GET Receitas Endpoint """
    api_endpoint = f"{config}/{API_END_POINT}"

    headers = {
        "Authorization": f"Bearer {get_token_access(config)}"
    }

    response = requests.get(api_endpoint, headers=headers)
    response.raise_for_status()

    assert response.status_code == 200
    receitas = response.json()
    assert isinstance(receitas, list)


def test_get_receita_by_id(config):
    """  Test GET Receita/GetById Endpoint """
# Creating a new receita to be deleted later
    api_endpoint = f"{config}/{API_END_POINT}"
    new_receita = {
        "id": 0,
        "data": fake.date_time_this_decade().isoformat(),
        "descricao": fake.sentence(),
        "valor": f'{fake.pydecimal(left_digits=4, right_digits=2, positive=True)}',
        "categoria": {
            "id": 22,
            "descricao": "Salário",
            "idTipoCategoria": 2
        }
    }

    headers = {
        "Authorization": f"Bearer {get_token_access(config)}"
    }

    response = requests.post(api_endpoint, json=new_receita, headers=headers)
    response.raise_for_status()
    result = response.json()
    assert "message" in result
    assert result["message"] is True
    assert "receita" in result
    created_receita = result["receita"]
    id_Receita = created_receita['id']

    api_endpoint = f"{config}/{API_END_POINT}/GetById/{id_Receita}"

    response = requests.get(api_endpoint, headers=headers)
    response.raise_for_status()

    assert response.status_code == 200
    result = response.json()
    assert "message" in result
    assert result["message"] is True
    receita = result["receita"]
    assert "id" in receita
    assert receita["id"] == created_receita["id"]
    assert "descricao" in receita
    assert receita["descricao"] == created_receita["descricao"]
    assert "data" in receita
    assert "valor" in receita
    assert "categoria" in receita
    assert "id" in receita["categoria"]
    assert "descricao" in receita["categoria"]
    assert "idTipoCategoria" in receita["categoria"]
    assert receita["categoria"]["id"] == 22
    assert receita["categoria"]["descricao"] == new_receita["categoria"]["descricao"]
    assert receita["categoria"]["idTipoCategoria"] == 2
