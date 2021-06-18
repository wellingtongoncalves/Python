frase = str(input('Digite uma frase: ').strip())
print('A letra "A" aparece nesta frase {} vezes'.format(frase.upper().count('A')))
print('A letra "A" aparece a primeira vez na posição {}'.format(frase.upper().find('A')+1))
print('A letra "A" aparece a ultima vez na posição {}'.format(frase.upper().rfind('A')+1))