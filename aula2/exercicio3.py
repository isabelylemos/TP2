estatura1 = float(input("Digite a estatura da primeira pessoa: "))
estatura2 = float(input("Digite a estatura da segunda pessoa: "))
estatura3 = float(input("Digite a estatura da terceira pessoa: "))

print("Estaturas em ordem decrescente:")
if estatura1 >= estatura2 and estatura1 >= estatura3:
    print(estatura1)
    if estatura2 >= estatura3:
        print(estatura2)
        print(estatura3)
    else:
        print(estatura3)
        print(estatura2)
elif estatura2 >= estatura1 and estatura2 >= estatura3:
    print(estatura2)
    if estatura1 >= estatura3:
        print(estatura1)
        print(estatura3)
    else:
        print(estatura3)
        print(estatura1)
else:
    print(estatura3)
    if estatura1 >= estatura2:
        print(estatura1)
        print(estatura2)
    else:
        print(estatura2)
        print(estatura1)
