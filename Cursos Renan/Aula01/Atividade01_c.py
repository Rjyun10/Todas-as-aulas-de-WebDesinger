import time
campo = 1
recebe_campos = True
start_prog = True

while start_prog:
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
    #print("\nCalculando...")
    #time.sleep(1)
    print("\nO resultado da sua conta é:", resultado)

    fim_prog = True
    while fim_prog:
        print("\nDeseja finalizar o Programa?")
        try:
            confirma = str(input("\nDigite S (SIM) ou N (Calcular Novamente): "))
            if confirma == "s" or confirma == "S":
                fim_prog = False
                start_prog = False
            if confirma == "n" or confirma == "N":
                fim_prog = False
                recebe_campos = True
                campo = 1
        except:
            print("\nOpção inválida...")
else:
    print("\n---------- PROGRAMA FINALIZADO ----------")