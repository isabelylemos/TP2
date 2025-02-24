numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

op = input("Digite: 1 - Média, 2 - Quadrado da soma dos 2 números, 3 - Cubo do menor número: ")
if op == "1":
    media = (numero1*2)+(numero2*3)/2
    print(f"Esta é a média ponderada dos números com pesos 2 e 3 respectivamente: {media}")
elif op == "2":
    soma = numero1 + numero2
    quadrado = pow(soma, 2)
    print(f"Este é o quadrado da soma dos dois números: {quadrado}")
elif op == "3":
    if numero1 < numero2:
        cubo = pow(numero1, 3)
        print(f"Este é o cubo do menor número: {cubo}")
    elif numero2 < numero1:
        cubo = pow(numero2, 3)
        print(f"Este é o cubo do menor número: {cubo}")
    else:
        print("Os dois números são iguais.")


    
    