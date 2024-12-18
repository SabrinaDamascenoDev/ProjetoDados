import pandas as pd
import openpyxl as xl

tabela_vendas = pd.read_excel("excel_files/Vendas.xlsx")

# Importar base de dados
pd.set_option("display.max_columns", None)
print(tabela_vendas)
# Visualizar a base de dados

# Faturamento por loja

# Quantidade de produtos vendidos pela loja

# Ticket medio por procura em cada loja

# Enviar um email com o relatório gerado