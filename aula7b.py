##nome = input('Qual é seu nome? ')
## print ('Prazer em te conhecer {:<20}!'.format(nome))
##print ('Prazer em te conhecer {:=^20}!'.format(nome))

n1 = int (input('Um valor: '))
n2 = int (input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
res = n1 % n2
print('A soma é {}, o produto é {} , a divisão é {:.3f} , \n a divisão inteira é {} , e o resultado da potência é {}'.format(s,m,d,di,e,res))
# {:.3f} expressão para se colocar o ponto depois de 3 casas decimais.
#('A soma é {}, o produto é {} , a divisão é {:.3f} , \n a divisão inteira é {} , e o resultado da potência é {}'.format(s,m,d,di,e,res),end='') operador end mantem a linha caso haja dois prints.
#\n quebra a linha