nome = input('Informe seu nome:')
valor = float(input('Informe um valor:'))
numero_conta = input('Informe o numero da conta:')

validacao = input('String de validação:')

nome_validacao, conta_validacao = validacao.split(';')

if nome_validacao == nome and conta_validacao == numero_conta:
  print('Dados validados')
else:
  print('Dados invalidos')
