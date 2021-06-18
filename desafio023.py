'''num = (input('Digite um número: '))
print('O número digitado foi: {}' .format(num))
unidade = (num)
dezena = (num)
centena = (num)
milhar = (num)
print('A unidade do número é {} e sua unidade é {}'.format(num,unidade[3]))
print('A unidade do número é {} e sua dezena é {}'.format(num,dezena[2]))
print('A unidade do número é {} e sua centena é {}'.format(num,centena[1]))
print('A unidade do número é {} e sua milhar é {}'.format(num,milhar[0]))'''

num = int(input('Digite um número: '))
print('Analisando o número: {}'.format(num))

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('A unidade é {}'.format(u))
print('A dezena é {}'.format(d))
print('A centena é {}'.format(c))
print('A milhar é {}'.format(m))
