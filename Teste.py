quantidade_pessoas = int(input())
pessoas = []
score = [0,0]

if quantidade_pessoas < 2 or quantidade_pessoas > 6:
    exit()

for i in range(quantidade_pessoas):
    pessoas.append(input())

rodadas = int(input())

for i in range(rodadas):
    mao_jogador = input()
    mao_jogador = mao_jogador.split()

    palpite = input()
    palpite = palpite.split()

    for x in range(quantidade_pessoas):
        if mao_jogador[x] == palpite[x]:
            score[x] += 1

ordenada = sorted(score)
ordenada = score[-1]

count = 0
for x in range(len(score)):
    if score[x] == ordenada:
        count += 1

if count > 1:
    print('EMPATE')

for x in range(len(score)):
    if score[x] == ordenada:
        print(pessoas[x].upper(), 'GANHOU')

