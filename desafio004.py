#Faca um programa qu leia algo pelo teclado e mostre na tela  o seu tipo primitivo e todas as informacoes possiveis sobre ele.

valor = input('Digite algo: ')
print(f'O tipo primitivo desse valor é {type(valor)}') #f=format
print(f'Esse valor só tem espaços? {valor.isspace()}')
print(f'Esse valor é um número? {valor.isnumeric()}')
print(f'Esse valor é alfabético? {valor.isalpha()}')
print(f'Esse valor é alfanumérico? {valor.isalnum()}')
print(f'Esse valor está em maiúsculas? {valor.isupper()}')
print(f'Esse valor está em minúsculas? {valor.islower()}')
print(f'Esse valor está capitalizado? {valor.istitle()}')
