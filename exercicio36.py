'''emprestimo bancario'''
casa = float(input('Digite o valor da casa: '))
salario = float(input('Digite o valor do seu salário: '))
anos = float(input('Em quantos anos você pretende pagar? '))
prestacao = casa / (anos * 12)
minimo = salario * 30 / 100
print(f'A prestação ficou em {prestacao:.2f} R$ por mês')
if prestacao <= minimo:
    print('Parabéns seu emprestimo foi aprovado')
else:
    print('Seu emprestimo foi reprovado')
