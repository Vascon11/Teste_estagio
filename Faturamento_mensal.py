import pandas as pd

#os dados de faturamento mensal por estado
dados = {
    'Estado': ['SP', 'RJ', 'MG', 'ES', 'Outros'],
    'Faturamento': [
        67836.43, 
        36678.66, 
        29229.88, 
        27165.48, 
        19849.53
    ]
}

#criando o DataFrame
df = pd.DataFrame(dados)

#calculo do total de faturamento
total_faturamento = df['Faturamento'].sum()

#calculo do percentual de representação por estado (com arredondamento)
df['Percentual_Representacao'] = (
    (df['Faturamento'] / total_faturamento) * 100
).round(2)

#formatando o faturamento
def formatar_moeda(valor):
    return f"R$ {valor:,.2f}".replace(',', 'X').replace('.', ',').replace('X', '.')

df['Faturamento_Formatado'] = df['Faturamento'].apply(formatar_moeda)

print("-=-"*20)# uma separação de texto

#mostrandoo o DataFrame completo
print("Percentual de Representação por Estado:\n")
print(df[['Estado', 'Faturamento_Formatado', 'Percentual_Representacao']])

print("-=-"*20)#uma separação de texto

#mostra um resumo formatado
print("\nResumo:")
for _, row in df.iterrows():
    print(
        f"{row['Estado']}: {row['Faturamento_Formatado']} - "
        f"{row['Percentual_Representacao']}%"
    )
print("-=-"*20)# uma separação de texto