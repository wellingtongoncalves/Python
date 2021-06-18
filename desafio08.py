metros = float(input('Valor em metros: '))
quilometro = metros/1000
hectometro = metros/100
decametro = metros/10
decimetro = metros/10
centimetro =  metros*100
milimetro =  metros*1000


print('O valor de metros é {}m \n o valor de quilometros é {:.1f}km \n  o valor de hectometro é {:.1f}hec \n o valor em decametros é {:.1f}dam \n em decimetro {:.1f}dm \n em centimetro  {:.1f}cem \n e em milimetro é {:.1f}mm'.format(metros,quilometro,hectometro,decametro,decimetro,centimetro,milimetro))

