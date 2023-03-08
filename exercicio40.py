'''Calcular média de notas'''
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
print(f' A sua média foi {media:.1f}')
if media < 5:
    print('Infelizmente você foi reprovado')
elif media > 5 and media < 6.9:
    print('Você fará uma recuperação')
elif media > 10:
    print('Media invalida, digite as notas novamente')
else:
    print('Parabéns você foi aprovado')
