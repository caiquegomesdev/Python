# faca um program aque leia a largura e a altura de uma parede em metros, calcule a sua area e a quantidade de tinta necessaria para pintala, sabendo que cada litro de tinta, pinta uma area de  2mqudrados
largura = float(input("Digite a largura da parede em metros: "))
altura = float(input("Digite a altura da parede em metros: "))

area = largura * altura
quantidade_tinta = area / 2

print(f"A área da parede é de {area:.2f} metros quadrados.")
print(f"Você vai precisar de {quantidade_tinta:.2f} litros de tinta para pintar a parede.")
