import cv2
import numpy as np

imagem = cv2.imread("pentagono3.png")
altura, largura, bypixel = np.shape(imagem)

print ("altura: ", altura)
print ("largura: ", largura)

imagem_copia = np.copy(imagem)


for py in range(0,altura):
        for px in range(0,largura):
  
            if (255,255,255) in imagem[py][px]:
                imagem_copia[py][px][0] =0
                imagem_copia[py][px][1] =0
                imagem_copia[py][px][2] =0
            else:
                imagem_copia[py][px][0] =255
                imagem_copia[py][px][1] =255
                imagem_copia[py][px][2] =255
  
cv2.imshow("imagem copiada", imagem_copia)

x0 = largura
y0 = altura
x1 = 0
y1 = 0

for py in range (0,altura):
  for px in range (0,largura):
    if (255,255,255) in imagem_copia[py][px]:
      if(px<x0):
        x0=px
      if(px>x1):
        x1=px
      if(py<y0):
        y0=py
      if(py>y1):
        y1=py
        
print("pto 0:", x0, "", y0)
print("pto 1:", x1, "", y1)
imagem_largura = x1-x0
imagem_comprimento = y1-y0
print("larg:", imagem_largura)
print("comp:", imagem_comprimento)
