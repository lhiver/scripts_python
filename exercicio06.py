#crie um algoritmo que leia um numero inteiro e mostre o dobro o triplo e a raiz quadrada.
number = int (input('Digite um número: '))
dobro = number * 2
triplo = number * 3
raiz = number ** (1/2)
print ('O dobro do número {} é {} enquanto seu triplo é {} e sua raiz é {:.1f} '.format(number,dobro,triplo,raiz))