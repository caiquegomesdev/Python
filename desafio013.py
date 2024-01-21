#faca um algoritimo que leia o salario de um funcionario e mostre seu novo salario com 15% de aumento.
salario_atual = float(input("Digite o salário do funcionário: "))
aumento = 0.15  # 15% de aumento

novo_salario = salario_atual * (1 + aumento)

print(f"O novo salário do funcionário com o aumento é: R${novo_salario:.2f}")
