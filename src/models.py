from pydantic import BaseModel
from typing import List
import server

class Receita(BaseModel):
    data_inicio: str = ''
    data_fim: str = ''
    fonte_consulta: str = 'Portal da Transparência - Fortaleza'
    fonte: str = ''
    descricao: str = ''
    receita_prevista_no_ano: float = 0.0
    receita_arrecadada_no_período: float = 0.0
    receita_recolhida_no_período: float = 0.0
    percentual_realizado: float = 0.0
    
class ResponseSite(BaseModel):
    receitas: List[Receita] = []

class ResponseDefault(BaseModel):
    code: int
    message: str
    datetime: str
    results: List[ResponseSite] = []

class ResponseError(BaseModel):
    code: int
    message: str