import re
def verificador(senha):
    verifica = "áéíóúâêîôûàèìòùãõüç.,!? : "
    
    if len(senha) < 6 or len(senha) > 15:
        return False
   
    is_up = False
    is_low = False
    is_digit = False

    for char in senha:
        if char in verifica:
            return False
        if char.isupper():
            is_up = True
        if char.islower():
            is_low = True
        if char.isdigit():
            is_digit = True
    
    if not (is_up and is_low and is_digit):
        return False
    
    for i in range(len(senha) -1 ):
        if senha[i].lower().isalpha() and senha[i + 1].lower().isalpha():
            if ord(senha[i]) + 1 == ord(senha[i + 1]):
                return False
            
        if senha[i].isdigit() and senha[i + 1].isdigit():
            if int(senha[i]) + 1 == int(senha[i + 1]):
                return False    
    

    return True


senha = input("Digite a senha: ")
if verificador(senha):
    print("Senha válida")
else:
    print("Senha inválida")
