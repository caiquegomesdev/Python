#Crie um programa que leia quantos dinheiro a pessoa tem na carteira e  mostre quantos dolares ela pode comprar
# considere US1.0 = R$3.27

taxa_cambio = 3.27  # Taxa de câmbio de reais para dólares

dinheiro_reais = float(input("Digite a quantidade de dinheiro em reais: "))
dolares = dinheiro_reais / taxa_cambio

print(f"Com {dinheiro_reais:.2f} reais, você pode comprar aproximadamente {dolares:.2f} dólares.")
