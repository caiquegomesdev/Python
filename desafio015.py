#Escreva um programa que pergute a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preco a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por km rodado

km_percorridos = float(input("Digite a quantidade de Km percorridos: "))
dias_alugados = int(input("Digite a quantidade de dias de aluguel: "))

preco_por_dia = 60
preco_por_km = 0.1530

preco_total = (preco_por_dia * dias_alugados) + (preco_por_km * km_percorridos)

print(f"O preço a pagar é: R${preco_total:.2f}")
