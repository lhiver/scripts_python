'''numero maior e menor'''
n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite mais um número: '))
lista = [n1, n2, n3]
ordem = sorted(lista)
print(ordem)
print(f'O menor número é {ordem[0]}')
print(f'O maior número é {ordem[2]}')
