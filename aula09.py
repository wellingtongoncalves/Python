frase = ('Curso em Vídeo Python')
print(frase[9::3]) ##VePh

frase = str('Aprendendo Python')
print(frase[3:]) ##noaeMio

frase = ('Digite um número:')
print(frase[15:]) ##o:

frase = ('1234')
print(frase.count('4',0,5)) ##1

frase = ('1234')
print(frase.find('3')) ## O número 3 está na posição 2.

frase = ('1234')
print(frase.find('1234')) ## O número 3 está na posição 2.

frase = ('Wellington Gonçalves Marinho')
print(frase.find('Gon')) ## Encontrado na posição 11.

frase = ('Wellington Gonçalves Marinho')
print(frase.find('NHO')) ## Quando a string pedida não existe é acrescentado o valor de -1.

'''frase = ('Wellington Gonçalves Marinho')
print('Curso' in 'frase') ## Não existe a palavra dentro da string - Irá resultar em True Ou False.

frase = ('Wellington Gonçalves Da Silva Calcanhoto')
print(frase.replace('Da Silva','Marinho')) ## Troca a string Wellington Gonçalves Marinho Calcanhoto

frase = ('Wellington Gonçalves Da Silva Calcanhoto')
print(frase.replace('Da Silva Calcanhoto', 'Marinho')) ## Troca a string Wellington Gonçalves Marinho.

frase = ('Wellington Gonçalves Marinho')
print(frase.upper()) ## Transforma os caracteres minúsculos para maiúsculos = WELLINGTON GONÇALVES MARINHO

frase = ('wELLINGTON gONÇALVES mARINHO')
print(frase.upper())## Transforma os caracteres minúsculos para maiúsculos = WELLINGTON GONÇALVES MARINHO

frase = ('wELLINGTON gONÇALVES mARINHO')
print(frase.lower())  ## Transforma os caracteres maiúsculos para minúsculos = De 'wELLINGTON gONÇALVES mARINHO' para 'wellington gonçalves marinho'.

frase = ('Wellington Gonçalves Marinho')
print(frase.capitalize()) ## Transforma as demais letras maiúsculas para minúsculas e deixa somente a primeira letra em maiúscula.
## = Wellington gonçalves marinho

frase = ('Wellington gonçalves marinho')
print(frase.title())
## Wellington Gonçalves Marinho
## Vai analisar quantas palavras a string tem no exemplo acima tem 3 palavras.
## Então pela posição dos espaços o title vai começar transformando as primeiras letras e as transformando
## de letras minúsculas para maiúsculas.

frase = ('   Aprenda Python  ') ## Essa string 'frase' tem 18 caracteres na memória incluindo espaços.
print(frase.strip())
##Aprenda Python
## O método strip irá remover os espaços do começo e fim , esquerda e direita
## E os caracteres que ficaram serão contados à partir do zero.

frase = ('   Aprenda Python  ')
print(frase.rstrip()) ## O método strip irá remover os espaços da direita.

frase = ('   Aprenda Python  ')
print(frase.lstrip()) ## O método strip irá remover os espaços da esquerda.

número = ('1234')
print(número.split())

frase = ('Curso em Vídeo Python')
print(frase.split())
## Resultado ['Curso', 'em', 'Vídeo', 'Python'] transforma em uma lista e cada palavra recebe indexação nova.
## ex: 'Curso' = 01234 , 'em' = 0,1 e etc.
## A string completa é transformada em indíces também ficando da seguinte forma 'Curso' 'em' 'Vídeo' 'Python'
                                                                                # 0      1     2      3 .
## Junção
frase = 'Curso em Vídeo Python'
print('-'.join(frase ))
print('## -------------------------------------------------- ##\n \n')

frase = 'Manipulando Textos'
print(frase[3:13]) ## ipulando T

frase = 'Manipulando Textos'
print(frase.count('A')) ## 0 Letras 'A' maiúsculas dentro da string.

frase = 'Manipulando Textos'
print(frase.upper().count('AN')) ## Significa que tem dois caracteres 'AN' maiúsculos dentro da string.

frase = 'Curso em Vídeo Python'
print(frase.find('Curso')) ## Procura a palavra e mostra o indíce posição daonde a mesma começa. no caso posição 0.

frase = 'Curso em Vídeo Python'
print('Curso' in frase) ## Vai mostrar com true ou false se existe aquela palavra dentro da string.No caso true.

frase = 'Curso em Vídeo Python'
print(frase.lower().find('vídeo')) ##vídeo achado na posição 9.

frase = 'Curso em Vídeo Python'
print(frase.split()) ##['Curso', 'em', 'Vídeo', 'Python']

frase = 'Curso em Vídeo Python'
print(frase.split().count('Python'))


frase = 'Curso em Vídeo Python'
dividido = frase.split()
print(dividido[0]) ## 'Curso' vai mostrar a posição dentro da lista no caso Curso representa a posição 0.

frase = 'Curso em Vídeo Python'
dividido = frase.split()
print(dividido[3][0])

frase = 'Curso em Vídeo Python'
dividido = frase.split()
print(dividido[0][0])

numero = ('1''2''3''4')
unidade = numero.split()
print(unidade[0][3])

dezena = numero.split()
print(dezena[0][2])

centena = numero.split()
print(centena[0][1])

milhar = numero.split()
print(milhar[0][0]) 


numero = str(input('Digite um número: '))
unidade = numero
print('A unidade é {}'.format(unidade[3]))


dezena = numero
print('A dezena é {}'.format(dezena[2]))

centena = numero
print('A centena é {}'.format(centena[1]))

milhar = numero
print('A milhar é {}'.format(milhar[0]))'''