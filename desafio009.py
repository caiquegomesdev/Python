# faca um programa que leia um numero inteiro qualquer e mostre na tela a sua tabuada
numint = int(input("Digite o numero: "))

print(f"Tabuada do {numint}")
for i in range (1, 11):
    r = numint * i
    print(f"{numint} x {i} = {r}")