'''calculo de distancia e preço da viagem'''
distancia = float(input('Qual a distancia em KM? '))
if distancia <= 200:
    print(distancia * 0.50)
else:
    print(distancia * 0.45)
