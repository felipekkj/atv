def verificar_idade(nome, idade):
    if idade >= 18:
        print(f"{nome} é maior de idade.")
    else:
        print(f"{nome} é menor de idade.")

nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))
verificar_idade(nome, idade)
