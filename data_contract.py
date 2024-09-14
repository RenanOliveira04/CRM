from datetime import datetime
from typing import Tuple
from pydantic import BaseModel, EmailStr, PositiveFloat, PositiveInt
from enum import Enum

class ProdutoEnum(str, Enum):
    Varejo = 'Varejo'
    SetorFinanceiro = 'Setor Financeiro'
    Saúde = 'Saúde'

class Vendas(BaseModel):
    email: EmailStr
    data: datetime
    valor: PositiveFloat
    quantidade: PositiveInt
    categoria: str
    produto: ProdutoEnum
    
    