from endereco import Endereco
from funcionario import Funcionario

class Medico(Funcionario):
    def __init__(self, nome: str, telefone: str, email: str, crm, endereco: Endereco) -> None:
        super().__init__(nome, telefone, email, endereco)
        self.crm = crm

    def __str__(self) -> str:
        return super().__str__()
    
    def __str__(self) -> str:
        return (f"CRM: {self.crm}")