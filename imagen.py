import cv2
import easyocr

# Cargar la imagen
image = cv2.imread("image.jpg")

# Inicializar el lector OCR
reader = easyocr.Reader(["en"])

# Detectar el texto en la imagen
result = reader.readtext(image)

# Iterar sobre cada resultado de texto detectado
for res in result:
    # Obtener las coordenadas del rectángulo que encierra el texto
    top_left = tuple(res[0][0])
    bottom_right = tuple(res[0][2])

    # Dibujar el rectángulo alrededor del texto
    cv2.rectangle(image, top_left, bottom_right, (0, 255, 255), 2)

    # Obtener la posición para colocar el texto encima del rectángulo
    text_position = (top_left[0], top_left[1] - 10)

    # Escribir el texto encima del rectángulo
    cv2.putText(image, res[1], text_position, cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2)

print(text_position)
# Mostrar la imagen con el texto detectado y los rectángulos
cv2.imshow("Texto detectado", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

