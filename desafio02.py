Python 3.9.5 (tags/v3.9.5:0a7dcbd, May  3 2021, 17:27:52) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> print('===== DESAFIO 02 ===== ')
===== DESAFIO 02 ===== 
>>> dia = input('DIA = ' )
DIA = 
>>> mes = input('MES = ')
MES = 11
>>> print('Você nasceu no dia',dia,' de ' , mes , 'de ' , ano ,'. Correto ? ')
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    print('Você nasceu no dia',dia,' de ' , mes , 'de ' , ano ,'. Correto ? ')
NameError: name 'ano' is not defined
>>> ano = input('ANO = ')
ANO = 1992
>>> print('Você nasceu no dia',dia,' de ' , mes , 'de ' , ano ,'. Correto ? ')
Você nasceu no dia   de  11 de  1992 . Correto ? 
>>> 