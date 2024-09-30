import pytest

from atividade.models.endereco import Endereco
from atividade.models.medico import Medico

@pytest.fixture
def validar_medico():
    Medico("Nome", "Telefone", "Email", "CRM", Endereco("Logradouro", "Numero", "Complemento", "CEP", "Cidade"))

def validar_atributo_nome(validar_medico):
    assert validar_medico.nome == "Nome"

def validar_atributo_telefone(validar_medico):
    assert validar_medico.telefone == "Telefone"

def validar_atributo_email(validar_medico):
    assert validar_medico.crm == "CRM"

def validar_endereco_atributo_logradouro(validar_medico):
    assert validar_medico.logradouro == "Logradouro"

def validar_endereco_atributo_numero(validar_medico):
    assert validar_medico.numero == "Numero"

def validar_endereco_atributo_complemento(validar_medico):
    assert validar_medico.complemento == "Complemento"

def validar_endereco_atributo_cep(validar_medico):
    assert validar_medico.cep == "CEP"

def validar_endereco_atributo_cidade(validar_medico):
    assert validar_medico.cidade == "Cidade"