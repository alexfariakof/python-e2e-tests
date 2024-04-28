"""Test E2E Backend API Categoria Endpoint"""
from faker import Faker
import requests
from conftest import get_token_access

fake = Faker()
API_END_POINT = "Categoria"


def test_create_category(config: str):
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
    assert result is not None
    created_category = result
    assert "id" in created_category
    assert "descricao" in created_category
    assert created_category["descricao"] == new_category["descricao"]
    assert "idTipoCategoria" in created_category
    assert created_category["idTipoCategoria"] == 1


def test_update_category(config: str):
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
    assert created_category is not None
    result = response.json()
    created_category = result

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
    assert updated_category is not None
    updated_category = result
    assert "id" in updated_category
    assert "descricao" in updated_category
    assert updated_category["descricao"] == new_category["descricao"]
    assert "idTipoCategoria" in updated_category
    assert updated_category["idTipoCategoria"] == 1


def test_delete_category(config: str):
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
    assert result is not None
    created_category = result

    # Deleting the category
    response = requests.delete(f"{api_endpoint}/{created_category['id']}", headers=headers)
    response.raise_for_status()

    assert response.status_code == 200
    deleted_category = response.json()
    assert deleted_category is True


def test_get_categories(config: str):
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


def test_get_category_by_id(config: str):
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
    assert result is not None
    created_category = result
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


def test_get_category_by_tipo_categoria(config: str):
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
