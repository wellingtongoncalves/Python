import random 
from time import sleep
print('Vou pensar em um número entre 0 e 5. Tente adivinhar ... ')
num = random.randint(0,5)
num1 = int(input('Em que número eu pensei?  '))
print('PROCESSANDO...')
sleep(4)
if num1 != num:
    print('GANHEI O número que eu escolhi foi {} e não {}'.format(num,num1))
else:
    print('PARABÉNS Você ganhou , o número que eu escolhi foi {}'.format(num))    