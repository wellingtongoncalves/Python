import math
ang = float(input('Digite o ângulo que você deseja: '))
seno  = math.sin(math.radians(ang))
print('O ângulo de {:.2f} tem o COSSENO de {:.2f}'.format(ang,seno))
cosseno = math.cos(math.radians(ang))
print('O ângulo de {:.2f} tem o COSSENO de {:.2f}'.format(ang,cosseno))
tang = math.tan(math.radians(ang))
print('O ângulo de {:.2f} tem o SENO de {:.2f}'.format(ang,tang))