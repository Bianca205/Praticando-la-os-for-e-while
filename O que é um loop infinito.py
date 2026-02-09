'''
André está testando um novo recurso no backend do Buscante que processa dados em um loop. Durante os testes, ele percebeu que o sistema parou de responder, e suspeita que o problema está em um loop infinito.
contador = 0
while contador < 10:
    print("Processando dados...")
Qual é o problema do código de André e como resolver?
Resposta: O problema do código de André é que o valor do contador nunca é incrementado dentro do loop, o que faz com que a condição `contador < 10` seja sempre verdadeira, resultando em um loop infinito.
Para resolver esse problema, é necessário adicionar uma linha de código para incrementar o contador dentro do loop. 
'''
contador = 0
while contador < 10:
    print("Processando dados...")
    contador += 1  # Incrementa o contador para evitar o loop infinito
