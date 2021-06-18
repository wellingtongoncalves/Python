
nome = str(input('Digite o nome completo: '))
print('Seu nome em completo em minúsculo é {}'.format(nome.upper()))
print('Seu nome em completo em minúsculo é {}'.format(nome.lower()))
print('Seu primeiro nome tem ao todo {} letras '.format(len(nome) - nome.count(' ')))
primeiro = nome.split()
print('Seu primeiro nome tem {} letras '.format(len(primeiro[0])))
## ou
print('Seu primeiro nome tem {} letras '.format(nome.find(' ')))




