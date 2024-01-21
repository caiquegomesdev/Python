# Crie um algoritmo que leia um numero e mostre seu dobro seu triplo e sua raiz quadrada
import math

n1=float(input('Digite um numero: '))
d = n1 * 2
t = n1 * 3
r = math.sqrt(n1)

print(f"O dobro de {n1} é {d}")
print(f"O triplo de {n1} é {t}")
print(f"A raiz quadrada de {n1} é {r:.2f}")