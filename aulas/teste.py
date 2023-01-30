import cv2
import pytesseract

# Ler a imagem com o opencv


img = cv2.imread("ocstese.png")


# onde esta o executável do pytesseract

pytesseract.pytesseract.pytesseract_cmd = "C:\Program Files\Tesseract-OCR\Tesseract.exe"
resultado = pytesseract.image_to_string(img)

print(resultado)
