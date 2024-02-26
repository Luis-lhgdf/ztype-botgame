# ztype_Botgame

Bot utilizando reconhecimento de img e texto para auxiliar nas fases do ztype

---

link do game = https://zty.pe/

recomendado deixar o browser em tela cheia pressionando F11 (caso estiver no windows,Chrome)
![alt text](app_img.png)

---

---

Para o codigo Funcionar perfeitamento é necessario instalar algumas bibliotecas:
--->import time
--->from pytesseract import pytesseract
--->import pyautogui

a biblioteca pytesseract tera que instalar um executavel alem de usar o pip install
que se encontra neste link:https://github.com/UB-Mannheim/tesseract/wiki

duvidas na instalaçao do exe este video ira te ajudar: https://www.youtube.com/watch?v=jailqGRNAgw

---

---

As variaveis Abaixo São cordenadas apenas para o print da tela sair recortado no local onde esta o tela inicial do game.
Caso nao delimitar essas posições o print vai sair da tela inteira e o codigo pode puxar textos
que estão no seu navegador. Dica: utilize a biblioteca "MouseInfo" para saber as posições x y
da tela inicial do game.

x = 658 # coordenada x do canto superior esquerdo
y = 80 # coordenada y do canto superior esquerdo
width = 800 # largura do retângulo
height = 1000 # altura do retângulo

---
