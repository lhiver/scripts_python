'''pagamento de um produto'''
produto = float(input('Digite o valor do produto: '))
print('\033[35mComo deseja pagar?\033[m')
print('\033[32m1 - a vista')
print('2 - a vista no cartão')
print('3 - 2x no cartão')
print('4 - 3x ou mais no cartão\033[m')
escolha = int(input('\033[35mDigite a opção desejada: \033[m'))

if escolha == 1:
    print(produto - (produto * 10 / 100))
elif escolha == 2:
    print(produto - (produto * 5 / 100))
elif escolha == 3:
    produto = produto / 2
    print(f'O valor do produto ficou em {produto}R$')
elif escolha == 4:
    opc = int(input('Em quantas vezes deseja parcelar? '))
    juros = produto + (produto * 20 / 100)
    parcela = juros / opc
    print(
        f'Com juros vai custar {juros}R$ parcelado em {opc}x de {parcela}R$')
else:
    print('\033[31mOpção invalida\033[31m')
