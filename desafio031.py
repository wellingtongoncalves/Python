'''distancia = float(input('Qual é a distância da sua viagem? ? '))
print('Você está prestes a começar uma viagem de {}'.format(distancia))
passagem_curta = distancia * 0.50
passagem_longa = distancia * 0.45 
if distancia <= 200:
    print('E o preço da sua passagem será de {:.2f}'.format(passagem_curta))
else:
    print('E o preço da sua passagem será de {:.2f}'.format(passagem_longa))

distância = float(input('Qual é a distância da sua viagem ? '))    
print('Você está prestes a começar uma viagem de {}KM.'.format(distância))
if distância <= 200:
    preço = distância * 0.50
else:
    preço = distância * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preço))'''

distância = float(input('Qual é a distância da sua viagem ? '))    
print('Você está prestes a começar uma viagem de {}KM.'.format(distância))
preço = distância * 0.50 if distância <= 200 else distância * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preço))





