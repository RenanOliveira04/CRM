from datetime import datetime
from typing import Tuple
from pydantic import BaseModel, EmailStr, PositiveFloat, PositiveInt
from enum import Enum

class SetorEnum(str, Enum):
    Varejo = 'Varejo'
    Atacado = 'Atacado'

class Vendas(BaseModel):
    email: EmailStr
    data: datetime
    valor: PositiveFloat
    quantidade: PositiveInt
    setor: SetorEnum
    
    