from datetime import datetime
from typing import Tuple
from pydantic import BaseModel, EmailStr, validate_call, PositiveFloat, PositiveInt
from enum import Enum

class ProdutoEnum(str, Enum):
    ChabotGPT = 'ChabotGPT'
    ChatbotGemini = 'ChatbotGemini'
    ChatbotLlhama = 'ChatbotLlhama'

class Vendas(BaseModel):
    email: EmailStr
    data: datetime
    valor: PositiveFloat
    quantidade: PositiveInt
    categoria: str
    produto: ProdutoEnum
    
    @validate_call('produto')
    def categoria_deve_estar_no_enum(cls, v):
            return v