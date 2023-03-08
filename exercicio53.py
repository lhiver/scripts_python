frase = str(input('Digite um frase: ')).lower().strip()
inverso =''.join(frase[::-1])
print(frase)
print(inverso)
if frase == inverso:
    print('Formou um palindromo')
else:
    print('Não é um palindromo')