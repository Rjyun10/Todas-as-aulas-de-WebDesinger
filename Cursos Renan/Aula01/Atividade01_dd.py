recebe_campos = True
campo = 1

while recebe_campos:
    match campo:
        case 1:
            try:
                Nome = str(input("\nDigite seu nome: "))
                campo += 1
            except:
                print("\nValor inválido !")
        case 2:
            try:
                Idade = int(input("\nDigite sua idade: "))
                if Idade < 20:
                    print("\nAbaixo da Idade !")
                else:
                    campo += 1
            except:
                print("\nValor inválido !")
        case 3:
            try:
                Altura = float(input("\nDigite sua altura: ").replace(",","."))
                campo += 1
            except:
                print("\nValor inválido !")
        case 4:
            try:
                Peso = float(input("\nDigite seu peso: ").replace(",","."))
                recebe_campos = False
            except:
                print("\nValor inválido !")
else:
    resultado = Peso/Altura**2

    if Idade >= 20 and Idade <= 60:
        if resultado < 18.5:
            classificacao = "Abaixo do peso"
        elif resultado >= 18.5 < 24.99:
            classificacao = "Normal"
        elif resultado > 25 < 29.99:
            classificacao = "Sobrepeso"
        else:
            classificacao = "Obesidade"
    elif Idade > 60:
        if resultado < 22:
            classificacao = "Abaixo do peso"
        elif resultado >= 22 <= 27:
            classificacao = "Normal"
        elif resultado > 27 < 29.99:
            classificacao = "Sobrepeso"
        else:
            classificacao = "Obesidade"

print("\nSeu nome é", Nome, "você tem", Idade, "anos, pesa", Peso, "Kgs, tem", Altura, "metros de altura e sua classificação de IMC é", classificacao)