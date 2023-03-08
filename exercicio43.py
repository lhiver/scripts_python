'''imc'''
print('FAÇA O CALCULO DO SEU IMC')
peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))
imc = peso / (altura * altura)
print(f'O seu IMC é {imc:.1f}')
if imc < 18.5:
    print('Você está abaixo do peso')
elif imc == 18.5 or imc < 25:
    print('Você está no seu peso ideal')
elif imc == 25 or imc < 30:
    print('Você está um pouco acima do seu peso ideal')
elif imc == 30 or imc < 40:
    print('Você está obeso')
else:
    print('Você está com obesidade mórbida')
