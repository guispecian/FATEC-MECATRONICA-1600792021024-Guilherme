#Calculadora Personalizada
#1 - Soma
#2 - Subtração
#3 - Multiplicação
#4 - Divisão
#5 - Resistencia
#6 - Corrente
#7 - Tensão
#8 - Potencia
#9 - Resistencia em Serie
#10 - Resistencia em Paralelo

def exebir_menu():
  print('menu calculadora:')
  print('1 - Somar')
  print('2 - Subtrair')
  print('3 - Multiplicar')
  print('4 - Dividir')
  print('5 - Resistencia')
  print('6 - Corrente')
  print('7 - Tensão')
  print('8 - Potencia')
  print('9 - Serie')
  print('10 - paralelo')
  print('0 - Sair')

def somar(numero1,numero2):
  return numero1+numero2

def subtrair(numero1,numero2):
  return numero1-numero2

def multiplicar(numero1,numero2):
  return numero1*numero2

def dividir(numero1,numero2):
 if numero2 != 0:
   return numero1/numero2
 else:
   return 'Você tentou realizar uma divisão por zero!'

def resistencia(tensao,corrente):
  return dividir(tensao,corrente)

def corrente(tensao,resistencia):
  return dividir(tensao,resistencia)

def tensao(resistencia,corrente):
  return multiplicar(resistencia,corrente)

def potencia(tensao,corrente):
  return multiplicar(tensao,corrente)

def serie(resistencia1,resistencia2):
  return somar(resistencia1,resistencia2)

def paralelo(resistencia1,resistencia2):
  return multiplicar(resistencia1,resistencia2)/somar(resistencia1,resistencia2)

def ler_numeros():
  n1 = float(input('Numero 1:'))
  n2 = float(input('Numero 2:'))
  return n1,n2

#Programa Principal
import os
continuar = True
while continuar == True:
  os.system('clear')
  exebir_menu()
  opção = int(input('escolha sua opção:'))
  if opção == 1:
    n1,n2 = ler_numeros()
    print('Resultado:', somar(n1,n2))
  elif opção == 2:
    n1,n2 = ler_numeros()
    print('Resultado:', subtrair(n1,n2))
  elif opção == 3:
    n1,n2 = ler_numeros()
    print('Resultado:', multiplicar(n1,n2))
  elif opção == 4:
    n1,n2 = ler_numeros()
    print('Resultado:', dividir(n1,n2))
  elif opção == 5:
    n1,n2 = ler_numeros()
    print('Resultado:', resistencia(n1,n2))
  elif opção == 6:
    n1,n2 = ler_numeros()
    print('Resultado:', corrente(n1,n2))
  elif opção == 7:
    n1,n2 = ler_numeros()
    print('Resultado:', tensao(n1,n2))
  elif opção == 8:
    n1,n2 = ler_numeros()
    print('Resultado:', potencia(n1,n2))
  elif opção == 9:
    n1,n2 = ler_numeros()
    print('Resultado:', serie(n1,n2))
  elif opção == 10:
    n1,n2 = ler_numeros()
    print('Resultado:', paralelo(n1,n2))
  elif opção == 0:
    continuar = False
  else:
    print('Opção invalida!')
  input('Pressione enter para continuar')
