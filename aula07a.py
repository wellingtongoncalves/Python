#nome = input('Qual é seu nome?') print('Prazer em te conhecer {:=^20}!'.format(nome))

n1 = int(input('Um valor:'))
n2 = int(input('Outro valor:'))
a = n1 + n2
s = n1 - n2
m = n1 * n2
d = n1 / n2
po = n1 ** n2
div_in = n1 // n2
mod = n1 % n2
#print('A soma vale {} '.format(a))
#print('A subtração vale {} '.format(s))
#print('A multiplicação vale {} '.format(m))
#print('A divisão vale {} '.format(d))
#print('A potência vale {} '.format(po))
#print('A divisão inteira vale {} '.format(div_in))
#print('O resto vale {} '.format(mod))
print('A soma é {},\n o produto é {} e a divisão é {:.3f}'.format(a,m,d), end=' ')
print('Divisão inteira {} e potência {}'.format(div_in,po))

