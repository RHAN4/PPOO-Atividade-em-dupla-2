from abc import ABC, abstractmethod

from endereco import Endereco

class Funcionario(ABC, Endereco):
    
    def __init__(self, nome: str, telefone: str, email: str, endereco: Endereco) -> None:
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.endereco = Endereco

    def __str__(self) -> str:
        return(
            f"\nNome: {self.nome}"
            f"Telefone: {self.telefone}"
            f"Eamil: {self.email}"
            f"Endereco: {self.endereco}"
        )    