import pandas as pd
import os
from datetime import datetime

# 1. Configurações Iniciais
ARQUIVO_ENTRADA = "data/grocery_chain_data.csv"
PASTA_SAIDA = "output/"
ESTOQUE_ATUAL = 5 

print(f"[{datetime.now()}] Iniciando Robô...")

try:
    df = pd.read_csv(ARQUIVO_ENTRADA)
    
    analise = df.groupby(['store_name', 'product_name'])['quantity'].mean().round(2).reset_index()
    
    analise['estoque_seguranca'] = (analise['quantity'] * 3).round(2)
    
    compras = analise[analise['estoque_seguranca'] > ESTOQUE_ATUAL].copy()
    
    compras['qtd_a_comprar'] = (compras['estoque_seguranca'] - ESTOQUE_ATUAL).round(2)
    compras['status'] = "COMPRA NECESSÁRIA"

    if not os.path.exists(PASTA_SAIDA):
        os.makedirs(PASTA_SAIDA)

    timestamp = datetime.now().strftime('%Y%m%d_%H%M')
    caminho_final = f"{PASTA_SAIDA}Pedido_Compra_{timestamp}.csv"
    
    compras.to_csv(caminho_final, index=False)
    print(f"[{datetime.now()}] Sucesso! Relatório gerado com {len(compras)} itens em: {caminho_final}")

except Exception as e:
    print(f"[{datetime.now()}] ERRO NO PROCESSO: {e}")