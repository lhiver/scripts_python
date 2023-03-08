'''mostrar primeiro e ultimo nome'''
nome = input('Digite um nome completo: ')
primeiro = nome.split()[0]
ultimo = nome.split()[-1]
print(f'O seu primeiro nome é {primeiro}')
print(f'O seu ultimo nome é {ultimo}')
