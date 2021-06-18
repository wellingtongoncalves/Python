import math
an = int(input('Qual é o ângulo: '))
sen = math.sin(math.radians(an))
cos = math.cos(math.radians(an))
tg = math.tan(math.radians(an))
print('O seno de {:.2f} é {:.2f}'.format(an,sen))
print('O cosseno de {:.2f} é {:.2f}'.format(an,cos))
print('A tangente de {:.2f} é {:.2f}'.format(an,tg))