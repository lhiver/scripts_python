# escreva um progama que leia a velocidade de um carro
# se o carro ultrapassar 80km/h. mostre uma msg dizendo que ele foi multado
# a multa vai custar r$7.00 por cada km acima do limite
velocidade = float(input('Digite a velocidade do carro: '))
multa = (velocidade-80)*7
if velocidade <= 80:
    print('Parabéns vc está digirindo com segurança')
else:
    print(f'Você foi multado em {multa}')
