menor_preco = float('inf')
melhor_loja = ''

continuar = True

while continuar == True:
  preco = float(input('Informe o preço:'))
  loja = input('Informe a loja:')
  if preco < menor_preco:
    menor_preco = preco
    melhor_loja = loja

  continuar = input('Deseja continuar?').lower() == 's'

print('melhor loja: %s com o Preço de R$%.2f'%(melhor_loja, menor_preco))
