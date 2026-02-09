'''Você está recebendo uma lista de valores representando os produtos de sua loja virtual e gostaria de calcular a soma total desses produtos para entender o desempenho financeiro semanal.
valores = [10, 20, 30, 40, 50]
Crie um programa para implementar a soma.'''
valores = [10, 20, 30, 40, 50]
soma = 0
for valor in valores:
    soma += valor
print(f'A soma total das receitas é: {soma}')

'''pode ser assim:'''
valores_1 = [10, 20, 30, 40, 50]
soma_1 = 0 
for i in range(len(valores_1)):
    soma_1 += valores_1[i]
print(f'A soma total das receitas é: {soma_1}')

'''ou assim:'''
valores_2 = [10, 20, 30, 40, 50]
print(f'A soma total das receitas é: {sum(valores_2)}')