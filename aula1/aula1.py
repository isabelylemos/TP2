#numero1 = int(input("Digite o primeiro valor: "))
#numero2 = int(input("Digite o segundo valor: "))

#resultado = numero1 + numero2

#print(resultado)

valorProduto = float(input("Digite o valor do produto: "))
valorDesconto = float(input("Digite o desconto em %: "))

valorDesconto = valorProduto * valorDesconto/100
valorVenda = valorProduto - valorDesconto

print(f"O valor final da venda é: {valorVenda}")


