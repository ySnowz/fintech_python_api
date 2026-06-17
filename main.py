from fastapi import FastAPI
from pydantic import BaseModel, Field
from decimal import Decimal, ROUND_HALF_UP
from typing import List

app = FastAPI(title='API fintech')

# Classe que herda basemodel
class RequisicaoContrato(BaseModel):
    client_id: int
    # Decimal e, usando o 'Field', garantimos que seja maior que zero (gt=0)
    valor_total: Decimal = Field(..., gt=0)
    # Um inteiro entre 1 e 12 (ge=maior ou igual, le=menor ou igual)
    quantidade_parcelas: int=Field(...,ge=1, le=12)

# Função que recebe valor total e as quantidades de parcelas e calcula o valor de cada parcela
def calcular_parcelas_fintech(valor_total: Decimal, qtd_parcelas: int) -> List[Decimal]:
    valor_base_parcela = (valor_total / qtd_parcelas).quantize(Decimal('0.01'), rounding=ROUND_HALF_UP)
    lista_parcelas = [valor_base_parcela] * qtd_parcelas
    soma_atual_das_parcelas = sum(lista_parcelas)
    diferenca_centavos = valor_total - soma_atual_das_parcelas
    
    if diferenca_centavos != 0:
        lista_parcelas[-1] += diferenca_centavos
        
    return lista_parcelas

# Configuração dos endpoints
# O decorador '@app.post' diz ao FastAPI: "Quando alguém enviar um POST para a URL '/gerar-parcelas', execute isso"
@app.post("/gerar_parcelas")

# Função que irá gerar as parcelas baseada no contrato e retornar a resposta formatada
def gerar_parcelas(dados_entrada: RequisicaoContrato):
    resultado_calculo = calcular_parcelas_fintech(
        valor_total=dados_entrada.valor_total,
        qtd_parcelas=dados_entrada.quantidade_parcelas
    )

    resposta_formatada = {
        "mensagem": "Contrato Processado Com Sucesso!",
        "cliente_id": dados_entrada.client_id,
        "valor_total_contrato": dados_entrada.valor_total,
        "quantidade_parcelas": dados_entrada.quantidade_parcelas,
        "valores_das_parcelas": resultado_calculo
    }

    return resposta_formatada