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

#Programa Principal

continuar = True
while continuar == True:
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
  elif opção == 0:
    continuar = False
