entrada = input()
entrada = entrada.split()

valor_carrinho = int(entrada[0])
quantidade = int(entrada[1])

if valor_carrinho < 30 or valor_carrinho > 200:
    exit()
elif quantidade < 3 or quantidade > 10**5:
    exit()

lista = []

for i in range(quantidade):
    sla = int(input())

    if sla < 30 or sla > 200:
        exit()
    lista.append()

lista = sorted(lista)
soma = 0
soma += lista[-1]
soma += lista[-2]
soma += lista[-3]
soma += valor_carrinho


if soma >= 200:
    print('fretegratis')
else:
    print('fretepago')