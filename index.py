import re

print("===================")
print("Validação de senha")
print("===================")

print("Vamos criar uma senha segura?")
print("""A mesam deve conter os seguintes criterios:
Minimo de 8 digitos;
1 letramaiuscula;
1 letra minuscula;
1 caractere especial.""")

def senha_segura(senha):
    if len(senha) < 8:
        return False, "A sua senha deve conter mais 8 digiost"
    
    if not re.search(r'[a-z]', senha):
        return False, "Sua senha precisa ter no mínimo 1 letra minúscula."
    
    if not re.search(r'[A-Z]', senha)
    return False, "Sua senha precisa ter no minimo 1 letra miuscula"

    if not re.search

    return True, "Senha validad"


def solicitar_senha():
    while True:
        senha = input("Digite sua senha: ")
        valida, mensagem = senha_segura(senha)
        print(mensagem)
        if valida:
            break

solicitar_senha()

