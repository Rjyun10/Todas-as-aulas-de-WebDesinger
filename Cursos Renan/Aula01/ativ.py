NOME ="admin"
SENHA =12345

Nome = str(input("\nDigite seu usuário: "))
Senha = int(input("\nDigite sua senha: "))

if NOME == Nome and Senha == SENHA:
    print("\nUsuário encontrado !")
else:
    print("\nA senha ou o usuário estão incorretos !")