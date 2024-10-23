import pandas as pd

def calcular_faturamento(arquivo_json):
    try:
        #le o arquivo.json e expandir as colunas corretamente
        df = pd.read_json(arquivo_json)
        print("Arquivo JSON carregado com sucesso:")#mostra se o arquivo foi chamado com sucesso
        print(df.head())  #mostrar as primeiras linhas para verificar a estrutura
    except ValueError as e:
        print(f"Erro ao ler o arquivo JSON: {e}")#mostra se o arquivo foi chamado com sucesso
        return

    # coloc os dicionários aninhados para colunas separadas
    try:
        df = pd.json_normalize(df['dias'])
        print("Estrutura normalizada:")
        print(df.head())
    except KeyError as e:
        print(f"Erro: A estrutura do JSON está diferente. Detalhes: {e}")
        return

    #filtrar apenas os dias com faturamento > 0
    df_validos = df[df['valor'] > 0]

    #calcula o menor e o maior valor de faturamento
    menor_faturamento = df_validos['valor'].min()
    maior_faturamento = df_validos['valor'].max()

    #calcula a média mensal ignorando os dias sem faturamento
    media_mensal = df_validos['valor'].mean()

    #contar os dias com faturamento superior à média
    dias_acima_media = df_validos[df_validos['valor'] > media_mensal].shape[0]

    #mostra os resultados
    print(f"Menor valor de faturamento: {menor_faturamento}")
    print(f"Maior valor de faturamento: {maior_faturamento}")
    print(f"Dias com faturamento acima da média: {dias_acima_media}")

# Chamada da função
calcular_faturamento('faturamento.json')
