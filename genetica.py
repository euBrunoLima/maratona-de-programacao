numero = int(input())
string = input()

for i in range(len(string)):
    aux = i+numero
    invertido = string[i:aux]
    invertido = invertido[::-1]

    if len(invertido) < numero:
        print('N')
        break

    if string[i:aux] == invertido:
        print('S')
        break
