import pytest
from atividade.models.endereco import Endereco
from atividade.models.medico import Medico

@pytest.fixture
def validar_medico():
    medico = Medico("Nome", "Telefone", "Email", "CRM", 10.000, Endereco("Logradouro", "Numero", "Complemento", "CEP", "Cidade"))
    return medico

def test_validar_atributo_nome(validar_medico):
    assert validar_medico.nome == "Nome"

def test_validar_atributo_telefone(validar_medico):
    assert validar_medico.telefone == "Telefone"

def test_validar_atributo_email(validar_medico):
    assert validar_medico.email == "Email"

def test_validar_atributo_crm(validar_medico):
    assert validar_medico.crm == "CRM"

def test_validar_atributo_salario(validar_medico):
    assert validar_medico.salario == 10.000

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

def test_nome_vazio(validar_medico):
    with pytest.raises(ValueError, match = "O nome não pode estar em branco"):
        Medico("", "Telefone", "Email", "CRM", 10.000, Endereco("Logradouro", "Numero", "Complemento", "CEP", "Cidade"))

def test_telefone_invalido(validar_medico):
   with pytest.raises(TypeError, match= "Digite apenas números."):
        Medico("Nome", 0000, "Email", "CRM", 10.000, Endereco("Logradouro", "Numero", "Complemento", "CEP", "Cidade"))
        
def test_email_invalido(validar_medico):
   with pytest.raises(TypeError, match= "Email não pode estar vazio."):
        Medico("Nome", "Telefone", "", "CRM", 10.000, Endereco("Logradouro", "Numero", "Complemento", "CEP", "Cidade"))

def test_logradouro_invalidos(validar_medico):
    with pytest.raises(ValueError, match= "Logradouro não pode estar vazio"):
        Medico("Nome", "Telefone", "Email", "CRM", 10.000, Endereco("", "Numero", "Complemento", "CEP", "Cidade"))

def test_numero_invalido(validar_medico):
   with pytest.raises(ValueError, match= "Numero não pode estar vazio"):
        Medico("Nome", "Telefone", "Email", "CRM", 10.000, Endereco("Logradouro", "", "Complemento", "CEP", "Cidade"))

def test_complemento_invalido(validar_medico):
   with pytest.raises(ValueError, match= "Complemento não pode estar vazio"):
        Medico("Nome", "Telefone", "Email", "CRM", 10.000, Endereco("Logradouro", "Numero", "", "CEP", "Cidade"))

def test_cep_invalido(validar_medico):
   with pytest.raises(ValueError, match= "CEP não pode estar vazio"):
        Medico("Nome", "Telefone", "Eamil", "CRM", 10.000, Endereco("Logradouro", "Numero", "Complemento", "", "Cidade"))

def test_cidade_invalido(validar_medico):
   with pytest.raises(ValueError, match= "Cidade não pode estar vazio"):
        Medico("Nome", "Telefone", "Email", "CRM", 10.000, Endereco("Logradouro", "Numero", "Complemento", "CEP", ""))