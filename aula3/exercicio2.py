indice = int(input("Digite o indice de poluição: "))

match indice:
    case 0 | 1 | 2:
        print("Considerar aceitável")
    case 3 | 4 | 5:
        print("Suspender Atividades Grupo I")
    case 6 | 7: 
        print("Suspender Atividades Grupo I e II")
    case indice if indice >=8:
        print("Suspender Atividades de todos os Grupos")