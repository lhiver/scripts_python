'''aumento de salario'''
salario = float(input('Digite o valor do sálario: '))
if salario > 1.250:
    novo = (salario + (salario * 10 / 100))
if salario <= 1.250:
    novo = (salario + (salario * 15 / 100))
print(f'{novo:.2f}')
