
import time
from pytesseract import pytesseract
import pyautogui

# Defina o caminho para o executável do Tesseract
caminho = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
pytesseract.tesseract_cmd = caminho

time.sleep(5) # tempo para executar o codigo e ir até o navegador abrir o jogo

# Coordenadas do retângulo que delimita a área da tela inicial do jogo

x = 500  # coordenada x do canto superior esquerdo
y = 70  # coordenada y do canto superior esquerdo
width = 800  # largura do retângulo
height = 1000  # altura do retângulo
while True:
    # Captura a tela
    screenshot = pyautogui.screenshot(region=(x, y, width, height))

    # Salva a captura de tela como "img.jpg"
    screenshot.save("img.jpg")
    

    # Realiza OCR na imagem da captura de tela
    texto = pytesseract.image_to_string("img.jpg")

    # a variavel texto recebe ela mesmo como tipo str esplitada para a melhor organização das palavras
    texto = str(texto).split()

    try:
        # LOOP para cada palavra dentro da lista "texto"
        for p in texto:
            pyautogui.write(p)  # digita a palavra inteira de uma vez
            pyautogui.typewrite(p, 0.0001)  # digita a palavra novamente porem letra por letra
            pyautogui.typewrite(p, 0.0001)  # digita a palavra novamente porem letra por letra

    except:
        pass

# O codigo só ira finalizar se for cancelado manualmente no seu IDE, seja rapido para cancelar!
