'''pesquisar se a cidade tem santo no nome'''
cidade = input('Digite o nome de uma cidade: ').strip().lower()
PALAVRA = 'santo'
print(PALAVRA in cidade)
