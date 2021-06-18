preço = float(input('Qual o preço do produto ? : '))
#desconto = preço * (5 / 100)
novo_pre = preço - (preço * 5 / 100)
print('O preço normal do produto sem desconto é {} , R$ vai custar {:.2f}'.format(preço,novo_pre))