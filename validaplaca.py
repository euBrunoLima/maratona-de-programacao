placa = input()
numeros = '0123456789'
try:
    if len(placa) < 1 or len(placa) > 50:
        exit()
    else:
        if placa.isalnum():
            for i in placa:
                if i.isalpha():
                    if not i.isupper():
                        exit()
        else:
            exit()

    for i in range(len(placa)):

        if placa[i] == 'A' or placa[i] == 'P':
            if len(placa) <= 6:
                if len(placa) < 2:
                    exit()
                if placa[i+1] in numeros:
                    print('Placa muito antiga')
                    break

        if placa.isnumeric() and len(placa) <= 7 and len(placa):
            print('Placa numerica')
            break

        if placa[i].isalpha() and placa[i+1].isalpha():
            if len(placa) < 3:
                exit()
            if placa[2:].isdigit():
                if len(placa) == 6:
                    print('Placa AA-9999')
                    break

        if placa[i].isalpha() and placa[i+1].isalpha() and placa[i+2].isalpha():
            if len(placa) < 4:
                exit()
            if placa[3:].isdigit():
                if len(placa) == 7:
                    print('Placa AAA-9999')
                    break

        if placa[i].isalpha() and placa[i+1].isalpha() and placa[i+2].isalpha() and placa[i+3].isdigit()\
            and placa[i+4].isalpha() and placa[i+5].isdigit() and placa[i+6].isdigit():
            if len(placa) == 7:
                print('Placa Mercosul')
                break
        else:
            print('Placa invalida')
            break
except:
    exit()
