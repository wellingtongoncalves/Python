
'''from math import sqrt
oposto = float(input('Digite o valor do cateto oposto: '))
adjacente = float(input('Digite o valor do cateto adjacente: '))
hipotenusa = oposto**2 + adjacente**2
hipotenusa = sqrt (hipotenusa)
print('A hipotenusa vai medir {:.2f}'.format(hipotenusa,sqrt(hipotenusa)))'''


from math import hypot
oposto = float(input('Digite o valor do cateto oposto: '))
adjacente = float(input('Digite o valor do cateto adjacente: '))
hipotenusa = hypot (oposto,adjacente)
print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))


'''oposto = float(input('Digite o valor do cateto oposto: '))
adjacente = float(input('Digite o valor do cateto adjacente: '))
hipotenusa = (oposto**2 + adjacente**2) ** (1/2)
print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))

import math
oposto = float(input('Digite o valor do cateto oposto: '))
adjacente = float(input('Digite o valor do cateto adjacente: '))
hipotenusa= math.hypot(oposto,adjacente)
print('A hipotenusa vai medir {:.2f}'.format(hipotenusa))'''


