# Automação de Cruzamento de Dados (Merge/VLOOKUP) com Pandas

## 📌 Sobre o Projeto
Este é um script Python focado em automação de tarefas de backoffice e manipulação de planilhas. Ele resolve o problema clássico de cruzamento de bases de dados (similar à função PROCV/VLOOKUP do Excel), mas com a velocidade e capacidade de processamento da biblioteca Pandas.

O objetivo do script é buscar uma informação específica em um arquivo de origem e inseri-la em um arquivo de destino, utilizando uma chave única (como um CPF ou ID) que exista em ambos.

## ⚙️ Como Funciona
O pipeline de dados executa os seguintes passos:
1. **Extração:** Lê as planilhas de origem e destino nos formatos `.xlsx`.
2. **Transformação (Filtro):** Isola apenas as colunas estritamente necessárias do arquivo de origem para otimizar a memória e evitar poluição de dados no arquivo final.
3. **Cruzamento (Left Join):** Realiza um `pd.merge` preservando todas as linhas do arquivo de destino (Leads) e trazendo os dados do arquivo de origem (Conta Corrente) apenas quando há correspondência exata.
4. **Carga:** Exporta o resultado final para uma nova planilha Excel consolidada.

## 🚀 Como Configurar e Rodar

### Pré-requisitos
Certifique-se de ter o Python instalado junto com as bibliotecas de manipulação de dados e leitura de Excel:
```bash
pip install pandas openpyxl
