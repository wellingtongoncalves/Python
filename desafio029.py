velocidade = int(input('Qual a velocidade do carro ? '))
print('A velocidade do carro é: {}km/h'.format(velocidade))
excedente = velocidade - 80
multa = excedente * 7  
if velocidade > 80:
    print('Você foi multado porque sua velocidade é de {}km/h e o valor da sua multa por excesso de velocidade é de R${} e a velocidade ultrapassada foi de {}km/h'.format(velocidade,multa,excedente))
else:
    print('Você não ultrapassou o limite de velocidade')    