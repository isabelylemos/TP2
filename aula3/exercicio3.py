tensao = int(input("Digite o valor da tensão: "))
resistencia = int(input("Digite o valor da resistencia: "))
corrente = int(input("Digite o valor da corrente: "))
menu = int(input("Digite: 1 - Tensão, 2 - Resistência, 3 - Corrente"))

match menu:
    case 1:
        tensao = resistencia*corrente
        print(f"Este é o valor da Tensão: {tensao}")
    case 2:
        resistencia = tensao/corrente
        print(f"Este é o valor da Resistência: {resistencia}")
    case 3:
        corrente = tensao/resistencia
        print(f"Este é o valor da Corrente: {corrente}")