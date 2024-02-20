import pandas as pd
import openpyxl

#instanciando workbook
wb =  openpyxl.Workbook()
#convertendo dataframe
df = pd.read_html('https://www.infomoney.com.br/ferramentas/cambio/')[0]
#Removendo coluna com as bandeiras
tabela_cotacao =  df.drop("Unnamed: 1", axis=1)
#Exportando para o Excel
tabela_cotacao.to_excel('Cotação.xlsx', index=False)


