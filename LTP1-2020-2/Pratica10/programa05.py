#Calculadora Personalizada
#1 - Soma
#2 - Subtração
#3 - Multiplicação
#4 - Divisão

def exebir_menu():
  print('menu calculadora:')
  print('1 - Somar')
  print('2 - Subtrair')
  print('3 - Multiplicar')
  print('4 - Dividir')
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


#Programa Principal
import os
continuar = True
while continuar == True:
  os.system('clear')
  exebir_menu()
  opção = int(input('escolha sua opção:'))
  if opção == 1:
    n1 = float(input('numero 1:'))
    n2 = float(input('numero 2:'))
    print('Resultado:', somar(n1,n2))
  elif opção == 2:
    n1 = float(input('numero 1:'))
    n2 = float(input('numero 2:'))
    print('Resultado:', subtrair(n1,n2))
  elif opção == 3:
    n1 = float(input('numero 1:'))
    n2 = float(input('numero 2:'))
    print('Resultado:', multiplicar(n1,n2))
  elif opção == 4:
    n1 = float(input('numero 1:'))
    n2 = float(input('numero 2:'))
    print('Resultado:', dividir(n1,n2))
  elif opção == 0:
    continuar = False
  else:
    print('Opção invalida!')
  input('Pressione enter para continuar')
