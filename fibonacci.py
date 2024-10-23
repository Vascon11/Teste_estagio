#defini uma função que calcula se o numero pretence a fibonacci
def fibonacci_check(num):
    
    a, b = 0, 1 #vaalores inicias da sequencia de fibonacci
    
    #enquanto b for menor ou igual a numero escolhido
    while b <= num:
        
        if b == num:
            return f"{num} pertence à sequência de Fibonacci."
        #atualiza os valores de "a" e "b" para o proximo da sequencia
        
        a, b = b, a + b
    return f"{num} não pertence à sequência de Fibonacci."

#solicida um numero do usuario
numero = int(input("Digite um número: "))

#imprime se for verdade ou falso, calculado pela função anterior
print(fibonacci_check(numero))
