prestacao = float(input("Digite o valor da prestação: "))
taxa = float(input("Digite o valor da taxa de juros: "))
tempo = int(input("Digite a quantidade de meses em atraso: "))

valor = prestacao+(prestacao*(taxa/100)*tempo)

print(f"Este é o total da sua prestação em atraso: R$ {valor}")