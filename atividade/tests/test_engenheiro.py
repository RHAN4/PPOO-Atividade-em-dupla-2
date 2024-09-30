import pytest
from atividade.models.endereco import Endereco
from atividade.models.engenheiro import Engenheiro

@pytest.fixture
def pessoa_valida():
    engenheiro = Engenheiro("Marcos", "7199999-9999", "marcos@gmail.com", "6666", 
                            Endereco("Avenida J", "55", "Caminho K", "43806-200", "Salvador"))
    return engenheiro

def test_validar_nome(pessoa_valida):
    assert pessoa_valida.nome == "Marcos"

def test_validar_telefone(pessoa_valida):
    assert pessoa_valida.telefone == "7199999-9999"

def test_validar_email(pessoa_valida):
    assert pessoa_valida.email == "marcos@gmail.com"

def test_validar_crea(pessoa_valida):
    assert pessoa_valida.crea == "6666"

def test_validar_logradouro(pessoa_valida):
    assert pessoa_valida.logradouro == "Avenida J"

def test_validar_numero(pessoa_valida):
    assert pessoa_valida.numero == "55"

def test_validar_complemento(pessoa_valida):
    assert pessoa_valida.complemento == "Caminho K"

def test_validar_cep(pessoa_valida):
    assert pessoa_valida.cep == "43806-200"

def test_validar_cidade(pessoa_valida):
    assert pessoa_valida.cidade == "Salvador"