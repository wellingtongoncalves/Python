try:
	numero1 = float(input("Informe um numero: "))
	numero2 = float(input("Informe um numero: "))
	
	soma = numero1 + numero2
	print ("{0} + {1} = {2}".format(numero1, numero2, soma))
	
except ValueError:
	print("Somente numeros sao aceitos. Tente novamente.")
