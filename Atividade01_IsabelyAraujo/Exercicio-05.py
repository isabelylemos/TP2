fabricacao = float(input("Digite o custo de fabricação do carro: "))

total = (fabricacao + ((28/100)*fabricacao) + ((45/100)*fabricacao))

print(f"O custo final para o consumidor é igual a: R$ {total}")