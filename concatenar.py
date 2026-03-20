import pandas as pd

# --- CONFIGURAÇÕES ---
# Nome do arquivo que TEM a informação (onde está a coluna PA_SIGLA)
arquivo_origem = 'conta_corrente.xlsx'

# Nome do arquivo que RECEBERÁ a informação
arquivo_destino = 'Cooperados_Leads_CC1.xlsx'

# Nome do arquivo final que será salvo
arquivo_saida = 'Cooperados_Leads_CC1.xlsx'

# Nomes das colunas
coluna_chave = 'CPF'  # A coluna em comum nos dois arquivos
coluna_valor = 'pa'     # A informação que você quer copiar
# ---------------------

print("1. Carregando arquivos Excel...")
# Carrega os dados
df_origem = pd.read_excel(arquivo_origem)
df_destino = pd.read_excel(arquivo_destino)

print("2. Cruzando informações (Correspondência Exata)...")

# Selecionamos apenas as colunas necessárias do arquivo de origem
# para não sujar o arquivo final com colunas extras que você não quer.
dados_para_copiar = df_origem[[coluna_chave, coluna_valor]]

# Fazemos o MERGE (o cruzamento)
# how='left' significa: Mantenha TODAS as linhas do meu arquivo de destino
# e apenas traga as informações da origem quando encontrar correspondência.
df_final = pd.merge(
    df_destino, 
    dados_para_copiar, 
    on=coluna_chave, 
    how='left'
)

# Dica: Se quiser preencher quem não foi encontrado com algum texto, descomente a linha abaixo:
# df_final[coluna_valor] = df_final[coluna_valor].fillna('Não Encontrado')

print(f"3. Salvando resultado em {arquivo_saida}...")
df_final.to_excel(arquivo_saida, index=False)

print("Pronto! Verifique o arquivo gerado.")
