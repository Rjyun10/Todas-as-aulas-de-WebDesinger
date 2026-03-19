recebe_dados = True
campo = 1

while recebe_dados:
    match campo:
        case 1:
            try:
                Nome = str(input("\nDigite seu nome: "))
                campo += 1
            except:
                print("\nValor inválido !")
        case 2:
            try:
                Idade = int(input("\nDigite sua idade anos: "))
                campo += 1
            except:
                print("\nValor inválido !")
        case 3:
            try:
                Peso = float(input("\nDigite seu peso em Kgs: ").replace(",","."))
                recebe_dados = False
            except:
                print("\nValor inválido !")
else:
    print("\nSeu nome é", Nome, "você tem", Idade, "anos e pesa", Peso, "Kgs")