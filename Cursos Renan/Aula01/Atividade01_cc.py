import time
campo = 1
recebe_campos = True


while recebe_campos:
    match campo:
        case 1:
            try:
                valor1 = float(input("\nDigite seu primeiro número: ").replace(",","."))
                campo += 1
            except:
                print("\nValor inválido !")
        case 2:
            try:
                print("\n========== OPERAÇÕES ==========")
                print("\nSoma = +")
                print("Subtração = -")
                print("Multiplicação = x")
                print("Divisão = /")
                oper = str(input("\nDigite sua operação: "))
                if oper == "+" or oper == "-" or oper == "x" or oper == "X" or oper == "/":
                    campo += 1
                else:
                    print("\nOperador inválido !")
            except:
                print("\nValor inválido !")
        case 3:
            try:
                valor2 = float(input("\nDigite seu segundo número: ").replace(",","."))
                recebe_campos = False
            except:
                print("\nValor inválido !")
else:
    if oper == "+":
        resultado = valor1 + valor2
    elif oper == "-":
        resultado = valor1 - valor2
    elif oper == "X" or oper == "x":
        resultado = valor1 * valor2
    else:
        oper == "/"
        resultado = valor1/valor2
print("\n=============== RESULTADO ===============")
print("\nCalculando...")
#time.sleep(1)
print("\nO resultado da sua conta é:", resultado)
