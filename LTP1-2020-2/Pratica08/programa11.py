#Métodos das strings
texto = "a vinGAnça nunca é pLEna, MatA a aLma e envenena (Madruga, 1981)"


print(texto.capitalize())
print(texto.casefold())
print(texto.count("Madruga"))
texto_minusculo = texto.lower()
print(texto_minusculo)
print(texto_minusculo.count("madruga"))
texto_maisculo = texto.upper()
print(texto_maisculo)
print(texto_minusculo.find(','))
print(texto_minusculo[:texto_minusculo.find(',')])
