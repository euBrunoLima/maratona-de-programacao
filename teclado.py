teclado = [' ',' ','ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
palavras = []
quantidade = int(input())

if quantidade < 1 or quantidade > 100:
    exit()

for i in range(quantidade):
    palavra = input()
    palavras.append(palavra)

for i in range(quantidade):

    for letra in palavras[i]:
        for z in range(len(teclado)):
            if letra in teclado[z]:
                print(z, end='')
    print('\n', end='')
