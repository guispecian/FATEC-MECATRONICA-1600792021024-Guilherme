#Estrura de repetição
numero_secreto = 42

acertou = False

while acertou == False:
  chute = int(input('informe seu chute:'))
  if chute > numero_secreto:
    print('errou pro alto!')
  elif chute < numero_secreto:
    print('errou pra baixo')
  else:
    acertou = True 
    print('acertou!!')

print('Obrigado por jogar!!')
