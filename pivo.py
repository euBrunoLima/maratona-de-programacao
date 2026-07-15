numeros = input()
numeros = numeros.split()

num1 = int(numeros[0])
num2 = int(numeros[1])
num3 = int(numeros[2])

numeros = [num1,num2,num3]
numeros = sorted(numeros)

if num1 < -2000000000 or num1 > 2000000000:
    exit()
elif num2 < -2000000000 or num2 > 2000000000:
    exit()
elif num3 < -2000000000 or num3 > 2000000000:
    exit()

print(numeros[1])