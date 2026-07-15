numero = int(input())

count = 0
for i in range(1, numero+1):
    if numero % i == 0:
        count += 1

if count == 3:
    print('sim')
else:
    print('nao')