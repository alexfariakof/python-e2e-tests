"""Test e2e Create Account Angular."""
from playwright.sync_api import Page, expect
from faker import Faker

fake = Faker()


def test_angular_create_account_success(page: Page, config):
    """ Teste da funcionalidade de criação de uma conta com sucesso """
    # Arrange
    page.goto(f"{config}/createAccount")

    # Preencher os campos do formulário
    page.fill('input[name=nome]', fake.first_name())
    page.fill('input[name=sobreNome]', fake.last_name())
    page.fill('input[name=telefone]', fake.phone_number())
    page.fill('input[name=email]', fake.email())
    password = fake.password()
    page.fill('input[name=senha]', password)
    page.fill('input[name=confirmaSenha]', password)

    # Act
    page.click('button[type=submit]')
    
    # Assert
    page.wait_for_selector("app-alert-component")
    expect(page.locator("app-alert-component")).to_be_visible()
    success_alert = page.locator(".alert .alert-success")
    expect(success_alert).to_be_visible()
    assert success_alert.inner_text().strip() == 'Cadastro realizado com sucesso!'


def test_angular_create_account_with_password_mismatch(page: Page, config):
    """ Teste da funcionalidade de criação de uma conta com senhas diferentes  """
    # Arrange (Preparação)
    page.goto(f"{config}/createAccount")

    # Preencher os campos do formulário
    page.fill('input[name=nome]', fake.first_name())
    page.fill('input[name=sobreNome]', fake.last_name())
    page.fill('input[name=telefone]', fake.phone_number())
    page.fill('input[name=email]', fake.email())
    page.fill('input[name=senha]', fake.password())
    page.fill('input[name=confirmaSenha]', fake.password())

    # Act
    """ page.click('button[type=submit]')

    # Assert
    page.wait_for_selector("app-alert-component")
    expect(page.locator("app-alert-component")).to_be_visible()
    text_alert_component = page.locator(".alert .alert-danger")
    assert text_alert_component.inner_text().strip() == 'Senha e Confirma Senha são diferentes!'    
    """
    # Assert
    submit_button = page.locator('button[type=submit]')
    assert submit_button.is_disabled()


def test_angular_create_account_user_exists(page: Page, config):
    """ Teste da funcionalidade de criação de uma conta com usuário existente """
    # Arrange
    page.goto(f"{config}/createAccount")

    # Preencher os campos do formulário
    page.fill('input[name=nome]', fake.first_name())
    page.fill('input[name=sobreNome]', fake.last_name())
    page.fill('input[name=telefone]', fake.phone_number())
    page.fill('input[name=email]', "teste@teste.com")
    password = fake.password()
    page.fill('input[name=senha]', password)
    page.fill('input[name=confirmaSenha]', password)

    # Act
    page.click('button[type=submit]')

    # Assert
    page.wait_for_selector("app-alert-component")
    expect(page.locator("app-alert-component")).to_be_visible()
    text_alert_component = page.locator(".alert .alert-danger")
    print(text_alert_component.inner_text())
    assert text_alert_component.inner_text().strip() == 'Usuário já cadastrado!'
