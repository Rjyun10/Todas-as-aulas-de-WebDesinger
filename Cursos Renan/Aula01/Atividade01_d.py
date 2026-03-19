Altura = float(input("Digite sua altura: ").replace(",","."))
Peso = float(input("Digite seu peso: ").replace(",","."))
Idade = int(input("Digite sua idade: "))

resultado = Peso/Altura**2

if Idade >= 20 and Idade <= 60:
    resultado < 18.5
    classificacao = "Baixo peso"
elif resultado >= 18.5 < 24.99:
    classificacao = "Normal"
elif resultado > 25 < 29.99:
    classificacao = "Sobrepeso"
else:
    classificacao = "Obesidade"

if Idade > 60:
    resultado < 22
    classificacao = "Baixo peso"
elif resultado >= 22 <= 27:
    classificacao = "Normal"
elif resultado > 27 < 29.99:
    classificacao = "Sobrepeso"
else:
    classificacao = "Obesidade"


print(resultado)