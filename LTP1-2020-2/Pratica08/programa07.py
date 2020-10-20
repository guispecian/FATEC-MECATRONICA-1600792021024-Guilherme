preco = input("Informe um preco:")

posicao = 0
posicao_da_virgula = -1
while posicao < len(preco):
  if preco[posicao] == ',':
   posicao_da_virgula = posicao
  posicao = posicao + 1

if posicao_da_virgula == -1:
 print('O valor informado foi de', preco, 'reais')
else:
 print("O valor informado foi de", preco[:posicao_da_virgula], "reais")
 print("com", preco[posicao_da_virgula+1:] ,"centavos")
