def busca(entrada, alvo):
  encontro = False
  for nome in entrada.split(';'):
    if nome == nome_alvo:
      encontro = True
  return encontro

nomes = input('Informe nomes separados por ";":')
nome_alvo = input('Informe um nome para ser procurado:')

if busca(nomes, nome_alvo) == True:
  print('Alvo encontrado')
else:
  print('Alvo não encontraddo')
