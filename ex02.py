def reajustar_salario(salario):
    if salario > 5000:
        reajuste = salario * 0.10
    else:
        reajuste = salario * 0.15
    salario_reajustado = salario + reajuste
    return salario_reajustado

salario_atual = float(input("Digite o salário atual: R$"))
novo_salario = reajustar_salario(salario_atual)
print(f"O novo salário é: R${novo_salario:.2f}")
