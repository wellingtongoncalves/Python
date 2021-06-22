'''salário_atual = float(input('Qual é o salário do funcionário: '))
print('O salário atual do funcionário sem aumento é {:.2f}'.format(salário_atual))
aumento = (salário_atual * 10) / 100
novo_salário1 = aumento + salário_atual
aumento = (salário_atual * 15) / 100
novo_salário2 = aumento + salário_atual
if salário_atual > 1250:
  print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora'.format(salário_atual,novo_salário1))
if salário_atual <= 1250:
  print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora'.format(salário_atual,novo_salário2))'''  

salário = float(input('Qual é o salário do funcionário? R$ '))
if salário <= 1250:
    novo = salário + (salário * 15/100)
else:
    novo = salário + (salário * 10/100)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salário,novo))   