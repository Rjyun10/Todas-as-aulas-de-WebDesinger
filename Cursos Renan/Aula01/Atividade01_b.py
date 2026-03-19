import math
recebe_dados = True

while recebe_dados:
    try:
        raio = float(input("\nDigite o tamanho do Raio: ").replace(",", "."))
        recebe_dados = False
    except:
        print("\nValor inválido !")
else:
    resultado = 2*math.pi*raio
    print("\nA circunferência é igual a:", resultado)