def contador(inicio, fim, passo):
    if passo == 0:
        print("O passo não pode ser zero.")
        return
    if inicio < fim:
        for i in range(inicio, fim + 1, passo):
            print(i, end=' ')
    else:
        for i in range(inicio, fim - 1, -passo):
            print(i, end=' ')
    print()

inicio = int(input("Digite o valor de início: "))
fim = int(input("Digite o valor de fim: "))
passo = int(input("Digite o valor do passo: "))

print(f"Contagem de {inicio} até {fim}, de {passo} em {passo}:")
contador(inicio, fim, passo)
