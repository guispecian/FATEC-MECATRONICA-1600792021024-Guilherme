def LerNumeroPositivo():
  continuar = True
  while continuar == True:
    numero = int(input('Informe um valor:'))
    continuar = numero < 0
  return numero

def somar_dois_numeros(numero1,numero2):
  return numero1+numero2

primeiro_valor = LerNumeroPositivo()
segundo_valor =  LerNumeroPositivo()
resposta = somar_dois_numeros(primeiro_valor, segundo_valor)
print('A soma de', primeiro_valor, 'com', segundo_valor, 'é igual a',resposta)
