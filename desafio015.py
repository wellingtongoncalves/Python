quan_dias = int(input('Qual a quantidade de dias que ficou alugado ?: '))
km_rodado = float(input('Quantos Km rodados ?: '))
preço_pagar = (km_rodado * 0.15) + (quan_dias * 60)
print(' O total a pagar é de R${:.2f}'.format(preço_pagar))