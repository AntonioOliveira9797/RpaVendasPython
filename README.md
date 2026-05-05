# RpaVendasPython
RPA-Inventory-Bot: Automação de Reposição de Estoque

Problema: O processo manual de análise de estoque de 500+ itens levava X horas e era suscetível a erros humanos.

Solução: Um bot que processa dados de transações, calcula a demanda e gera ordens de compra automaticamente.

Tecnologias: Python, Pandas, Datetime.

Fluxograma do Processo: 

1. Trigger
Robô recebe um arquivo csv

2. Input
   
Leitura do arquivo grocery_chain_data.csv na pasta /data

3. Processamento e Decisões

Cálculo: "Calcular média de vendas e Estoque de Segurança ($Estoque = \mu \times 3$)".

Decisão: "O estoque atual é menor que o de segurança?".

Ação: "Sim: Adicionar item à lista de compras" ou "Não: Ignorar item".

4. Output

Finalização: "Gerar arquivo Pedido_Compra.csv com codificação UTF-8".

Sustentação: "Gravar status da operação no arquivo execucao.log".

<img width="794" height="37" alt="image" src="https://github.com/user-attachments/assets/c56989d2-c18b-44c7-9fbc-9b41a20cdd56" />

<img width="758" height="408" alt="image" src="https://github.com/user-attachments/assets/53fc5ef1-5f79-4180-a938-4faf58919d19" />
