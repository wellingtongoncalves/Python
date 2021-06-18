'''cidade = input('Em que cidade você nasceu ? ')
print('Analisando a palavra {}'.format(cidade))
procure = cidade.split()
print('Santo' in procure[0].capitalize())'''

'''frase = ('Wellington Gonçalves Marinho')
print('Gonçalves' in frase) ## Não existe a palavra dentro da string - Irá resultar em True Ou False.'''

'''nome = input('Digite um nome: ')
print('Silva' in nome)'''

'''name = input('Digite um nome: ')
print('Silva'in name.title().strip())
print(name)'''
##print(name.title().strip())

'''name = input('Digite um nome: ')
name = print('Silva'in name.title().strip())'''

nome = str(input('Informe seu nome completo: ')).strip()
divisao = nome.upper().split()
print(divisao)
print('SILVA' in divisao)