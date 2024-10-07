from abc import ABC, abstractmethod

from atividade.models.endereco import Endereco

class Funcionario(ABC, Endereco):
    
    def __init__(self, nome: str, telefone: str, email: str, salario: float, endereco: Endereco) -> None:
        self.nome = self._verificar_nome(nome)
        self.telefone = self._verificar_telefone(telefone)
        self.email = self._verificar_email(email)
        self.salario = self._verificar_salario(salario)
        self.endereco = endereco

    @abstractmethod
    def salarioFinal() -> float:
        pass

    def _verificar_salario(self, salario):
         if not isinstance(salario,float):
              raise TypeError("Salario deve ser numero")
         return salario

    def _verificar_nome(self, nome):
            if not isinstance(nome, str) or not nome.strip():
                raise ValueError("O nome não pode estar em branco")
            return nome
    
    def _verificar_telefone(self, telefone):
        if not isinstance (telefone, str):
            raise TypeError("Digite apenas números.")
        return telefone
    
    def _verificar_email(self, email):
            if not isinstance(email, str) or not email.strip():
                raise TypeError("Email não pode estar vazio.")
            return email

    def __str__(self) -> str:
        return(
            f"\nNome: {self.nome}"
            f"\nTelefone: {self.telefone}"
            f"\nEmail: {self.email}"
            f"\nSalário: {self.salario}"
            f"\nEndereco: {self.endereco}"
        )    