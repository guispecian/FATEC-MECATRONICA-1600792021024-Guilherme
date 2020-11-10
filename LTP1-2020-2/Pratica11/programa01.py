#Calculo da area do triangulo

#Função para calculo do semiperimetro
def semiperimetro(a,b,c):
  return (a+b+c)/2

#Função para calculo da area
def area(a,b,c):
  s = semiperimetro(a,b,c)
  return (s*(s-a)*(s-b)*(s-c)) ** 0.5

#Programação Principal
#Informe os lados A, B e c
a = int(input('Informe o valor do lado A:'))
b = int(input('Informe o valor do lado B:'))
c = int(input('Informe o valor do lado C:'))

#Calculo da area
print('O valor da area é:', area(a,b,c))
