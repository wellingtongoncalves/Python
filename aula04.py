Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print("Hello Mundo ")
Hello Mundo 
>>> print('Olá,Mundo)
      
SyntaxError: EOL while scanning string literal
>>> print ('Olá,Mundo')
Olá,Mundo
>>> print(7+4)
11
>>> print('7'+'4')
74
>>> print('7+4')
7+4
>>> 7+4
11
>>> '7'+'4'
'74'
>>> print('Olá' + 5)
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    print('Olá' + 5)
TypeError: can only concatenate str (not "int") to str
>>> print ('Olá',5)
Olá 5
>>> print('Olá' + 6)
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    print('Olá' + 6)
TypeError: can only concatenate str (not "int") to str
>>> nome = 'Guanabara'
>>> idade = 25
>>> peso = 74.8
>>> print 9nome,idade,peso)
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(9nome,idade,peso))?
>>> print(nome,idade,peso)
Guanabara 25 74.8
>>> nome = input('Qual é o seu nome ? ')
Qual é o seu nome ? juvenal
>>> idade = input('Qual sua idade ? ')
Qual sua idade ? 77
>>> peso = input('Qual seu peso ? ')
Qual seu peso ? 88
>>> print (nome,idade,peso)
juvenal 77 88
>>> 