#Repetição Infinita (Cuidado, pois se a variavel somatorio for = 1; o programa nunca acaba)

somatoria = 0

while True:
  print(somatoria)
  somatoria = somatoria + 10
  if somatoria == 100:
    break
print("Fim")
