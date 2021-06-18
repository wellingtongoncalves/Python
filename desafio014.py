celsius = float(input ('informe a temperatura em C°: '))
##fare = (celsius * 1.8) + 32
fare = 9 * celsius / 5 + 32
print ('A temperatura de {:.0f}°C corresponde a {:.0f}.°F'.format(celsius,fare))