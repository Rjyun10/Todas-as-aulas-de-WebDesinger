Nome = "Renan"
Auto = True
tenta_n = True

while tenta_n:
    while Auto:
        login = input("Digite seu nome: ")
        if login == Nome:
            print("Acesso confirmado")
            Auto = True
    else:
        Auto = False
        tenta_n = False
    print("Acesso negado")
else:
    Repetir = input("Tentar de novo? (S):")
    if Repetir == "s" or Repetir == "S":
        tenta_n = False
    else:
        tenta_n = True
