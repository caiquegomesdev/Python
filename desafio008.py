# escreva um programa que leia um valor em metros e exiba convertido em centimetros e milimetros
m = float(input("Digite um valor em metros"))
cm = m * 100
mm = m * 1000

print(f"{m} metros equivale a {cm:.2f} cm")
print(f"{m} metros equivale a {mm:.2f} mm")
