"""Test E2E Backend API Categoria Endpoint"""
from faker import Faker
import requests
from conftest import get_token_access

fake = Faker()
API_END_POINT = "Categoria"


def test_create_category(config):
    """ Test POST Categoria Endpoint """
    api_endpoint = f"{config}/{API_END_POINT}"

    new_category = {
        "id": 0,
        "descricao": fake.word(),
        "idTipoCategoria": 1
    }

    headers = {
        "Authorization": f"Bearer {get_token_access(config)}"
    }

    response = requests.post(api_endpoint, json=new_category, headers=headers)
    response.raise_for_status()

    result = response.json()
    assert "message" in result
    assert result["message"] is True
    assert "categoria" in result
    created_category = result["categoria"]
    assert "id" in created_category
    assert "descricao" in created_category
    assert created_category["descricao"] == new_category["descricao"]
    assert "idTipoCategoria" in created_category
    assert created_category["idTipoCategoria"] == 1


def test_update_category(config):
    """ Test PUT Categoria Endpoint """
    api_endpoint = f"{config}/{API_END_POINT}"

    # Creating a new category to be updated later
    new_category = {
        "id": 0,
        "descricao": fake.word(),
        "idTipoCategoria": 1
    }

    headers = {
        "Authorization": f"Bearer {get_token_access(config)}"
    }

    response = requests.post(api_endpoint, json=new_category, headers=headers)
    response.raise_for_status()
    created_category = response.json()

    result = response.json()
    assert "message" in result
    assert result["message"] is True
    assert "categoria" in result
    created_category = result["categoria"]

    # Updating the category
    updated_category = {
        "id": created_category["id"],
        "descricao": fake.sentence(),
        "idTipoCategoria": 1
    }

    response = requests.put(api_endpoint, json=updated_category, headers=headers)
    response.raise_for_status()

    assert response.status_code == 200
    updated_category = response.json()
    assert "message" in updated_category
    assert updated_category["message"] is True
    assert "categoria" in updated_category
    updated_category = result["categoria"]
    assert "id" in updated_category
    assert "descricao" in updated_category
    assert updated_category["descricao"] == new_category["descricao"]
    assert "idTipoCategoria" in updated_category
    assert updated_category["idTipoCategoria"] == 1


def test_delete_category(config):
    """ Test DELETE Categoria Endpoint"""
    api_endpoint = f"{config}/{API_END_POINT}"
    new_category = {
        "id": 0,
        "descricao": fake.word(),
        "idTipoCategoria": 1
    }

    headers = {
        "Authorization": f"Bearer {get_token_access(config)}"
    }

    response = requests.post(api_endpoint, json=new_category, headers=headers)
    response.raise_for_status()
    result = response.json()
    assert "message" in result
    assert result["message"] is True
    assert "categoria" in result
    created_category = result["categoria"]

    # Deleting the category
    response = requests.delete(f"{api_endpoint}/{created_category['id']}", headers=headers)
    response.raise_for_status()

    assert response.status_code == 200
    deleted_category = response.json()
    assert "message" in deleted_category
    assert deleted_category["message"] is True


def test_get_categories(config):
    """ Test GET Categoria Endpoint """
    api_endpoint = f"{config}/{API_END_POINT}"

    headers = {
        "Authorization": f"Bearer {get_token_access(config)}"
    }

    response = requests.get(api_endpoint, headers=headers)
    response.raise_for_status()

    assert response.status_code == 200
    categories = response.json()
    assert isinstance(categories, list)


def test_get_category_by_id(config):
    """  Test GET Categoria/GetById Endpoint """
    api_endpoint = f"{config}/{API_END_POINT}"
    new_category = {
        "id": 0,
        "descricao": fake.word(),
        "idTipoCategoria": 1
    }

    headers = {
        "Authorization": f"Bearer {get_token_access(config)}"
    }

    response = requests.post(api_endpoint, json=new_category, headers=headers)
    response.raise_for_status()
    result = response.json()
    assert "message" in result
    assert result["message"] is True
    assert "categoria" in result
    created_category = result["categoria"]
    id_categoria = created_category['id']

    api_endpoint = f"{config}/{API_END_POINT}/GetById/{id_categoria}"

    headers = {
        "Authorization": f"Bearer {get_token_access(config)}"
    }

    response = requests.get(api_endpoint, headers=headers)
    response.raise_for_status()

    assert response.status_code == 200
    category = response.json()
    assert "id" in category
    assert category["id"] == created_category["id"]
    assert "descricao" in category
    assert category["descricao"] == created_category["descricao"]
    assert "idTipoCategoria" in category
    assert category["idTipoCategoria"] == created_category["idTipoCategoria"]


def test_get_category_by_tipo_categoria(config):
    """ Test E2E Backend API Categoria Endpoint - GET Categoria/GetByTipoCategoria/1 """
    api_endpoint = f"{config}/{API_END_POINT}/GetByTipoCategoria/1"

    headers = {
        "Authorization": f"Bearer {get_token_access(config)}"
    }

    response = requests.get(api_endpoint, headers=headers)
    response.raise_for_status()

    assert response.status_code == 200
    categories = response.json()
    assert isinstance(categories, list)
