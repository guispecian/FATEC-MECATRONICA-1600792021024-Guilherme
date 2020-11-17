nomes = input('Informe os nomes separados por ";":' )

#Estrutura for
for nome in nomes.split(';'):
  print(nome.upper())
