'''Conversão de base'''
n = int(input('Digite um número: '))
print('\033[32mOpções de conversão \033[m ')
print('1 - binário')
print('2 - octal')
print('3 - hexadecimal')
opc = int(input('Digite o numero da opção desejada: '))
if opc == 1:
    print(bin(opc))
elif opc == 2:
    print(oct(opc))
elif opc == 3:
    print(hex(opc))
else:
    print('\033[31mopção invalida\033[m')
