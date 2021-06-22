reta1 =float(input('Digite o valor da primeira reta: '))
reta2 =float(input('Digite o valor da segunda reta: '))
reta3 =float(input('Digite o valor da terceira reta: '))
if reta3 < reta2 + reta1 and reta2 < reta3 + reta1 and reta1 < reta3 + reta2:
  print('Com a somas das retas é possivel criar um triangulo')   
else:
   print('Com a somas das retas não é possivel criar um triangulo') 


