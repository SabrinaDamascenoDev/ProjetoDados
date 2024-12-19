import pandas as pd
import openpyxl as xl
from bd.connect import collection
from bd.connect import collection2
from bd.connect import collection3

# Importar base de dados
tabela_vendas = pd.read_excel("excel_files/Vendas.xlsx")
# Visualizar a base de dados
pd.set_option("display.max_columns", None)

faturamento = tabela_vendas[['ID Loja', 'Valor Final']].groupby('ID Loja').sum().reset_index() # Faturamento por loja

quantidade = tabela_vendas[['ID Loja', 'Quantidade']].groupby('ID Loja').sum().reset_index() # Quantidade de produtos vendidos pela loja
# Ticket medio por procura em cada loja

#Se o faturamento não tiver o mesmo indice que a qunatidade aparecer erro
if not faturamento.index.equals(quantidade.index):
    raise ValueError("Os índices de 'faturamento' e 'quantidade' não são iguais.")

quantidade.replace({'Quantidade': {0: pd.NA}}, inplace=True) #Susbstituir os valores igual a 0 por nulo na tabela

# Fazer a lógica do ticket médio e criar uma tabela para guardar essas informações com o nome Ticked Médio
ticket = (faturamento['Valor Final'] / quantidade['Quantidade']).to_frame(name='Ticket Médio')
# Add o valor ID Loja da tabela faturamendo e add o valor no atributo ID Loja do ticket
ticket['ID Loja'] = faturamento['ID Loja'].values

ticket.reset_index(inplace=True)

print(ticket)
#Converte para dicionário
faturamento_dict = faturamento.to_dict(orient='records')
quantidade_dict = quantidade.to_dict(orient='records')
ticket_dict = ticket[['ID Loja', 'Ticket Médio']].to_dict(orient='records')

#Envia para banco
try:
    collection.insert_many(faturamento_dict)
    collection2.insert_many(quantidade_dict)
    collection3.insert_many(ticket_dict)
    print("Tudo salvo no MongoDB!")
except:
    print("Erro ao salvar no MongoDB")








