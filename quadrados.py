numero = int(input())
if numero < 1 or numero > 2**30:
    exit()
else:
    count = 1
    soma = 0

    for i in range(1, numero):
        if i % 2 == 0:
            continue
        else:
            soma += i
            if soma == numero:
                break
            count += 1
print(count)
