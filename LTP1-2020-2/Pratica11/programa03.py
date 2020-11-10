#Leitura e Visualização de um usuario

#visualização dos dados de um usuario
def visualização(nome,idade,cpf):
  print('Usuario')
  print('Nome:', nome)
  print('Idade:', idade)
  print('CPF:', cpf)

#Leitura de um usuario
def leitura():
  Nome = input('Informe seu nome:')
  Idade = input('Informe sua idade:')
  CPF = input('Informe seu CPF:')
  return Nome, Idade, CPF

N, I, C = leitura()
visualização(N,I,C)
