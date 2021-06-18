salario = float (input('Qual é o salário do funcionário: '))
novo_sal = salario + (salario * 15/100)
print('O salário antes do aumento era de {} e depois do aumento de 15% é de {:.2f}'.format(salario,novo_sal))