import cv2
import numpy as np

# Carregar a imagem
image = cv2.imread('pentagono3.png')

# Converter para escala de cinza
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Binarizar a imagem
_, threshold = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# Aplicar algoritmo de detecção de contornos
contours, _ = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

# Filtrar contornos para identificar pentágonos
pentagon_contours = []
for contour in contours:
    area = cv2.contourArea(contour)
    if area > 500:  # Ajuste esse valor de acordo com o tamanho do seu pentágono
        approx = cv2.approxPolyDP(contour, 0.05 * cv2.arcLength(contour, True), True)
        if len(approx) == 5:
            pentagon_contours.append(approx)

# Verificar se um pentágono foi encontrado
if len(pentagon_contours) > 0:
    # Encontrar os pontos de mínimo e máximo
    min_x = min_y = float('inf')
    max_x = max_y = float('-inf')
    for contour in pentagon_contours:
        for point in contour[:, 0, :]:
            x, y = point[0], point[1]
            min_x = min(min_x, x)
            min_y = min(min_y, y)
            max_x = max(max_x, x)
            max_y = max(max_y, y)

    # Exibir os pontos de mínimo e máximo
    print("Ponto mínimo: ({}, {})".format(min_x, min_y))
    print("Ponto máximo: ({}, {})".format(max_x, max_y))

    # Recortar o pentágono da imagem original
    cropped_image = image[int(min_y):int(max_y), int(min_x):int(max_x)]

    # Exibir o recorte do pentágono
    cv2.imshow('Recorte do Pentágono', cropped_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
else:
    print("Nenhum pentágono encontrado na imagem.")
