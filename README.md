# API Financeira (Fintech)

Esta é uma API mínima desenvolvida com FastAPI para processamento de contratos financeiros e geração de parcelas. O sistema realiza o cálculo de divisões de valores garantindo que a soma das parcelas seja exatamente igual ao valor total do contrato, tratando divergências de centavos na última parcela.

## 🚀 Funcionalidades Atuais

- **Geração de Parcelas**: Endpoint para calcular o parcelamento de um valor total em até 12 vezes.
- **Correção de Centavos**: Ajuste automático na última parcela para evitar perdas ou excessos por arredondamento.
- **Validação de Dados**: Uso de Pydantic para garantir que valores sejam positivos e quantidades de parcelas estejam no intervalo permitido.

## 🛠️ Tecnologias Utilizadas

- **Python 3.10+**
- **FastAPI**: Framework web moderno e de alta performance.
- **Pydantic**: Validação de dados e gestão de configurações.
- **Decimal (Standard Library)**: Para cálculos financeiros precisos.

## ⚙️ Como Executar

1. **Instalar dependências**:
   ```bash
   pip install fastapi uvicorn
   ```

2. **Rodar o servidor**:
   ```bash
   uvicorn main:app --reload
   ```

3. **Acessar a documentação interativa**:
   Abra o navegador em [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## 📡 Endpoints

### `POST /gerar_parcelas`
Gera a lista de parcelas para um contrato.

**Exemplo de Payload:**
```json
{
  "client_id": 1,
  "valor_total": 1000.00,
  "quantidade_parcelas": 3
}
```

**Exemplo de Resposta:**
```json
{
  "mensagem": "Contrato Processado Com Sucesso!",
  "cliente_id": 1,
  "valor_total_contrato": 1000.00,
  "quantidade_parcelas": 3,
  "valores_das_parcelas": [333.33, 333.33, 333.34]
}
```

## 🔮 Futuras Atualizações (Roadmap)

- [ ] **Persistência de Dados**: Integração com banco de dados (PostgreSQL) usando SQLAlchemy para salvar contratos.
- [ ] **Autenticação**: Implementação de segurança via OAuth2 e JWT.
- [ ] **Cálculo de Juros**: Opção para parcelamento com juros simples ou compostos.
- [ ] **Histórico de Clientes**: Endpoint para consultar todos os contratos gerados por um cliente específico.
- [ ] **Testes Automatizados**: Implementação de testes unitários e de integração com `pytest`.
- [ ] **Dockerização**: Criação de `Dockerfile` e `docker-compose.yml` para facilitar o deploy.
- [ ] **Logs e Monitoramento**: Integração com ferramentas de observabilidade.
