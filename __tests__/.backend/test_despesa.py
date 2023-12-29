"""Test E2E Backend API Despesa Endpoint"""
from conftest import get_token_access
from faker import Faker
import requests

fake = Faker()
API_END_POINT = "Despesa"


def test_create_despesa(config):
    """ Test POST Despesa Endpoint """
    api_endpoint = f"{config}/{API_END_POINT}"

    new_despesa = {
        "id": 0,
        "data": fake.date_time_this_decade().isoformat(),
        "descricao": fake.sentence(),
        "valor": f'{fake.pydecimal(left_digits=4, right_digits=2, positive=True)}',
        "dataVencimento": fake.date_time_this_decade().isoformat(),
        "categoria": {
            "id": 1,
            "descricao": "Alimentação",
            "idTipoCategoria": 1
        }
    }

    print(new_despesa)
    headers = {
        "Authorization": f"Bearer {get_token_access(config)}"
    }

    response = requests.post(api_endpoint, json=new_despesa, headers=headers)
    response.raise_for_status()

    result = response.json()
    assert "message" in result
    assert result["message"] is True
    assert "despesa" in result
    created_despesa = result["despesa"]

    # Add assertions based on your specific response structure
    assert "data" in created_despesa
    assert "valor" in created_despesa
    assert "dataVencimento" in created_despesa
    assert "categoria" in created_despesa
    assert "id" in created_despesa["categoria"]
    assert "descricao" in created_despesa["categoria"]
    assert "idTipoCategoria" in created_despesa["categoria"]
    assert created_despesa["categoria"]["id"] == 1
    assert created_despesa["categoria"]["descricao"] == new_despesa["categoria"]["descricao"]
    assert created_despesa["categoria"]["idTipoCategoria"] == 1


def test_update_despesa(config):
    """ Test PUT Despesa Endpoint """
    api_endpoint = f"{config}/{API_END_POINT}"

    # Creating a new despesa to be updated later
    new_despesa = {
        "id": 0,
        "data": fake.date_time_this_decade().isoformat(),
        "descricao": fake.sentence(),
        "valor": f'{fake.pydecimal(left_digits=4, right_digits=2, positive=True)}',
        "dataVencimento": fake.date_time_this_decade().isoformat(),
        "categoria": {
            "id": 1,
            "descricao": "Alimentação",
            "idTipoCategoria": 1
        }
    }

    headers = {
        "Authorization": f"Bearer {get_token_access(config)}"
    }

    response = requests.post(api_endpoint, json=new_despesa, headers=headers)
    response.raise_for_status()
    created_despesa = response.json()

    result = response.json()
    assert "message" in result
    assert result["message"] is True
    assert "despesa" in result
    created_despesa = result["despesa"]

    # Updating the despesa
    updated_despesa = {
        "id": created_despesa["id"],
        "data": fake.date_time_this_decade().isoformat(),
        "descricao": fake.sentence(),
        "valor": f'{fake.pydecimal(left_digits=4, right_digits=2, positive=True)}',
        "dataVencimento": fake.date_time_this_decade().isoformat(),
        "categoria": {
            "id": 1,
            "descricao": "Alimentação",
            "idTipoCategoria": 1
        }
    }

    response = requests.put(api_endpoint, json=updated_despesa, headers=headers)
    response.raise_for_status()

    assert response.status_code == 200
    updated_despesa = response.json()
    assert "message" in updated_despesa
    assert updated_despesa["message"] is True
    assert "despesa" in updated_despesa
    updated_despesa = updated_despesa["despesa"]

    # Add assertions based on your specific response structure
    assert "data" in updated_despesa
    assert "valor" in updated_despesa
    assert "dataVencimento" in updated_despesa
    assert "categoria" in updated_despesa
    assert "id" in updated_despesa["categoria"]
    assert "descricao" in updated_despesa["categoria"]
    assert "idTipoCategoria" in updated_despesa["categoria"]
    assert updated_despesa["categoria"]["id"] == 1
    assert updated_despesa["categoria"]["descricao"] == new_despesa["categoria"]["descricao"]
    assert updated_despesa["categoria"]["idTipoCategoria"] == 1


def test_delete_despesa(config):
    """ Test DELETE Despesa Endpoint"""
    api_endpoint = f"{config}/{API_END_POINT}"

    # Creating a new despesa to be deleted later
    new_despesa = {
        "id": 0,
        "data": fake.date_time_this_decade().isoformat(),
        "descricao": fake.sentence(),
        "valor": f'{fake.pydecimal(left_digits=4, right_digits=2, positive=True)}',
        "dataVencimento": fake.date_time_this_decade().isoformat(),
        "categoria": {
            "id": 1,
            "descricao": "Alimentação",
            "idTipoCategoria": 1
        }
    }

    headers = {
        "Authorization": f"Bearer {get_token_access(config)}"
    }

    response = requests.post(api_endpoint, json=new_despesa, headers=headers)
    response.raise_for_status()
    result = response.json()
    assert "message" in result
    assert result["message"] is True
    assert "despesa" in result
    created_despesa = result["despesa"]

    # Deleting the despesa
    response = requests.delete(f"{api_endpoint}/{created_despesa['id']}", headers=headers)
    response.raise_for_status()

    assert response.status_code == 200
    deleted_despesa = response.json()
    assert "message" in deleted_despesa
    assert deleted_despesa["message"] is True


def test_get_despesas(config):
    """ Test GET Despesas Endpoint """
    api_endpoint = f"{config}/{API_END_POINT}"

    headers = {
        "Authorization": f"Bearer {get_token_access(config)}"
    }

    response = requests.get(api_endpoint, headers=headers)
    response.raise_for_status()

    assert response.status_code == 200
    despesas = response.json()
    assert isinstance(despesas, list)


def test_get_despesa_by_id(config):
    """  Test GET Despesa/GetById Endpoint """
# Creating a new despesa to be deleted later
    api_endpoint = f"{config}/{API_END_POINT}"
    new_despesa = {
        "id": 0,
        "data": fake.date_time_this_decade().isoformat(),
        "descricao": fake.sentence(),
        "valor": f'{fake.pydecimal(left_digits=4, right_digits=2, positive=True)}',
        "dataVencimento": fake.date_time_this_decade().isoformat(),
        "categoria": {
            "id": 1,
            "descricao": "Alimentação",
            "idTipoCategoria": 1
        }
    }

    headers = {
        "Authorization": f"Bearer {get_token_access(config)}"
    }

    response = requests.post(api_endpoint, json=new_despesa, headers=headers)
    response.raise_for_status()
    result = response.json()
    assert "message" in result
    assert result["message"] is True
    assert "despesa" in result
    created_despesa = result["despesa"]
    id_Despesa = created_despesa['id']

    api_endpoint = f"{config}/{API_END_POINT}/GetById/{id_Despesa}"

    response = requests.get(api_endpoint, headers=headers)
    response.raise_for_status()

    assert response.status_code == 200
    result = response.json()
    assert "message" in result
    assert result["message"] is True
    despesa = result["despesa"]
    assert "id" in despesa
    assert despesa["id"] == created_despesa["id"]
    assert "descricao" in despesa
    assert despesa["descricao"] == created_despesa["descricao"]
    assert "data" in despesa
    assert "valor" in despesa
    assert "dataVencimento" in despesa
    assert "categoria" in despesa
    assert "id" in despesa["categoria"]
    assert "descricao" in despesa["categoria"]
    assert "idTipoCategoria" in despesa["categoria"]
    assert despesa["categoria"]["id"] == 1
    assert despesa["categoria"]["descricao"] == new_despesa["categoria"]["descricao"]
    assert despesa["categoria"]["idTipoCategoria"] == 1
