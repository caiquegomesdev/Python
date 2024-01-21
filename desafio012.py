#faca um algoritimo que leia o preco de um produto e mostre seu novo preco com 5% de desconto
preco_produto = float(input("Digite o preco do produto: "))
desconto = 0.05 #desconto de 5%
preco_com_desconto = preco_produto * (1 - desconto)

print(f"O preco com desconto ficou R${preco_com_desconto:.2f}")