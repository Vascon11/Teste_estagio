#entrada da string pelo usuário
texto = input("Digite a string que deseja inverter: ")

#string vazia para armazenar o texto invertido
texto_invertido = ""

#coloca a string de trás para frente
for i in range(len(texto) - 1, -1, -1):
    texto_invertido += texto[i]


#mostra a string invertida
print(f"String invertida: {texto_invertido}")