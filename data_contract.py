from datetime import datetime
from typing import Tuple
from pydantic import BaseModel, EmailStr, PositiveFloat, PositiveInt
from enum import Enum

class SetorEnum(str, Enum):
    Varejo = 'Varejo'
    Atacado = 'Atacado'

class Vendas(BaseModel):
    """
    Modelo de dados para vendas.
    
    args:
        email (EmailStr): Email do vendedor
        data (datetime): Data da venda
        valor (PositiveFloat): Valor da venda
        quantidade (PositiveInt): Quantidade de produtos
        setor (SetorEnum): Setor da venda
    """
    email: EmailStr
    data: datetime
    valor: PositiveFloat
    quantidade: PositiveInt
    setor: SetorEnum
    
    