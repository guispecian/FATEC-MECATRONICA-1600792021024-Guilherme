#Conversão de temperatura
def conversaof (numero1):
  return (numero1 / 5) * 9 + 32

def conversaok (numero1):
  return (numero1 / 5) * 5 + 273

#Programa Principal
#Informar Celsius
ValorC = float(input('infrome o valor de C em Celsius:'))

#Conversão de C para F
print('o valor de', ValorC, 'Celsius em Fahrenheit é:', conversaof(ValorC))

#Conversão de C para K
print('o valor de', ValorC, 'Celsius em Kelvin é:', conversaok(ValorC))
