import pytest
from atividade.models.endereco import Endereco
from atividade.models.medico import Medico

@pytest.fixture
def validar_medico():
    medico = Medico("Nome", "Telefone", "Email", "CRM", Endereco("Logradouro", "Numero", "Complemento", "CEP", "Cidade"))
    return medico

def test_validar_atributo_nome(validar_medico):
    assert validar_medico.nome == "Nome"

def test_validar_atributo_telefone(validar_medico):
    assert validar_medico.telefone == "Telefone"

def test_validar_atributo_email(validar_medico):
    assert validar_medico.crm == "CRM"

def test_validar_endereco_atributo_logradouro(validar_medico):
    assert validar_medico.endereco.logradouro == "Logradouro"

def test_validar_endereco_atributo_numero(validar_medico):
    assert validar_medico.endereco.numero == "Numero"

def test_validar_endereco_atributo_complemento(validar_medico):
    assert validar_medico.endereco.complemento == "Complemento"

def test_validar_endereco_atributo_cep(validar_medico):
    assert validar_medico.endereco.cep == "CEP"

def test_validar_endereco_atributo_cidade(validar_medico):
    assert validar_medico.endereco.cidade == "Cidade"