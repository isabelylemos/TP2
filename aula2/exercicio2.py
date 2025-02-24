numero = int(input("Digite um número inteiro positivo: "))

if numero%2 == 0:
    quadrado = pow(numero,2)
    print(f"O número digitado é par, este é o quadrado do número: {quadrado}")
else:
    cubo = pow(numero,3)
    print(f"O número digitado é impar, este é o cubo do número: {cubo}")
