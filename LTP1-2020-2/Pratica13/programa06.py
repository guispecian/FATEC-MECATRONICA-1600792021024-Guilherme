def contar_palavras (frase,palavra):
  total = 0
  for palavra_na_frase in frase.split():
    if palavra_na_frase == palavra:
      total = total + 1
  return total 

frase = input('informe uma frase:')
alvo = input('Informe uma palavra para contar:')
print(contar_palavras(frase,alvo))
