import time
from pytesseract import pytesseract
import pyautogui
from PIL import Image
import os
import threading
import customtkinter as ctk

class Bot:
    def __init__(self, executable_file_location, x, y, w, h):
        """Inicializa um objeto bot para interagir com o jogo.

        Args:
            executable_file_location (str): O caminho para o executável do Tesseract OCR.
            x (int): A coordenada x do canto superior esquerdo do retângulo que delimita a área da tela inicial do jogo.
            y (int): A coordenada y do canto superior esquerdo do retângulo que delimita a área da tela inicial do jogo.
            w (int): A largura do retângulo que delimita a área da tela inicial do jogo.
            h (int): A altura do retângulo que delimita a área da tela inicial do jogo.
        """
        # Defina o caminho para o executável do Tesseract
        self.executable_file_location = executable_file_location
        pytesseract.tesseract_cmd = self.executable_file_location

        self.x = x  # coordenada x do canto superior esquerdo
        self.y = y  # coordenada y do canto superior esquerdo
        self.width = w  # largura do retângulo
        self.height = h  # altura do retângulo
        self.stop = bool

        image_path = os.path.join(os.path.dirname(os.path.realpath(__file__)))

        self.spacecraft_icon = ctk.CTkImage(light_image=Image.open(os.path.join(image_path, "spacecraft.png")),
                        dark_image=Image.open(os.path.join(image_path, "spacecraft.png")), size=(20, 20))

    def view(self):
        print("iniciando")
        self.root = ctk.CTk()
        self.root.geometry("400x300")
        self.root.configure(fg_color="#1D053B")
        ctk.set_appearance_mode("light")
        self.root.grid_columnconfigure((0, 1), weight=1)
        self.root.rowconfigure((1,2), weight=0)
        self.root.resizable(False, False)

        self.title = ctk.CTkLabel(self.root, text="ZTYPE", font=("open sans", 40, "bold"), text_color="white")
        self.title.grid(row=0,  column=0, padx=(60,0), pady=(20,0), columnspan=2, sticky="w")

        self.title2 = ctk.CTkLabel(self.root, text="BOT",font=("open sans", 40, "bold"), text_color="#D56A02")
        self.title2.grid(row=0, column=1, columnspan=2,pady=(20,0))

        self.start_bt = ctk.CTkButton(self.root, text="   INICIAR", height=40, image=self.spacecraft_icon, anchor="w", command=self.start_thread, font=("open sans", 15, "bold"), fg_color="white", text_color="#D56A02", hover_color="#540074")
        self.start_bt.grid(row=1, column=0, pady=(60,40), columnspan=2)

        self.stop_bt = ctk.CTkButton(self.root, text="PAUSAR", height=40,command=self.stop_bot, font=("open sans", 15, "bold"), fg_color="white", text_color="#D56A02", hover_color="#540074")
        self.stop_bt.grid(row=2, column=0, pady=(30,10), columnspan=2)

        self.root.mainloop()

    def start_thread(self):
        thread = threading.Thread(target=self.play)
        thread.start()

    def play(self):
        self.start_bt.configure(fg_color="#540074")
        self.stop_bt.configure(fg_color="white")

        self.start_timer(5)
        self.stop = False

        while not self.stop:
            screenshot = pyautogui.screenshot(region=(self.x, self.y, self.width, self.height))
            screenshot.save("img.jpg")
            text = pytesseract.image_to_string("img.jpg")
            text = str(text).split()
            try:
                for word in text:
                    pyautogui.write(word, 0.00001)
                    pyautogui.typewrite(word, 0.00001)
            except:
                pass

    def start_timer(self, timer):
        time.sleep(timer)

    def stop_bot(self):
        self.start_bt.configure(fg_color="white")
        self.stop_bt.configure(fg_color="#540074")

        self.stop = True

local = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
application = Bot(executable_file_location=local, x=500, y=70, w=800, h=1000)
application.view()
