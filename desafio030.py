inteiro = int(input('Digite um número: '))
print('O número digitado foi: {}'.format(inteiro))
res = inteiro % 2
if res == 0:
    print('O número é par')
else:
    print('O número é impar')    
