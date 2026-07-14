import tkinter as tk
from tkinter import filedialog, ttk
import cv2
import numpy as np
from PIL import Image, ImageTk
import os

class PDIApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Projeto PDI - Processamento de Imagens")
        self.root.geometry("1200x700")
        
        # Variáveis
        self.imagem_original = None
        self.imagem_processada = None
        self.is_color = False
        
        # ===== FRAME SUPERIOR (Botões) =====
        frame_superior = tk.Frame(root)
        frame_superior.pack(pady=10)
        
        btn_abrir = tk.Button(frame_superior, text="Abrir Imagem", 
                              command=self.abrir_imagem, width=15)
        btn_abrir.pack(side=tk.LEFT, padx=5)
        
        btn_salvar = tk.Button(frame_superior, text="Salvar Resultado", 
                               command=self.salvar_imagem, width=15)
        btn_salvar.pack(side=tk.LEFT, padx=5)
        
        # Dropdown de processos
        self.processo_var = tk.StringVar(value="Selecione um processo")
        processos = [
            "Selecione um processo",
            "Decomposição RGB",
            "Decomposição HSV",
            "Limiarização",
            "Equalização de Histograma",
            "Filtro Gaussiano"
        ]
        self.dropdown = ttk.Combobox(frame_superior, textvariable=self.processo_var, 
                                     values=processos, width=25)
        self.dropdown.pack(side=tk.LEFT, padx=10)
        
        btn_aplicar = tk.Button(frame_superior, text="Aplicar", 
                                command=self.aplicar_processo, width=10)
        btn_aplicar.pack(side=tk.LEFT, padx=5)
        
        # ===== FRAME DE PARÂMETROS =====
        self.frame_parametros = tk.Frame(root)
        self.frame_parametros.pack(pady=5)
        
        # Label para mostrar info da imagem
        self.info_label = tk.Label(root, text="Nenhuma imagem carregada", font=("Arial", 10))
        self.info_label.pack()
        
        # ===== FRAME DE IMAGENS =====
        frame_imagens = tk.Frame(root)
        frame_imagens.pack(pady=10, expand=True, fill=tk.BOTH)
        
        # Original
        frame_original = tk.Frame(frame_imagens)
        frame_original.pack(side=tk.LEFT, padx=10, expand=True, fill=tk.BOTH)
        
        tk.Label(frame_original, text="Imagem Original", font=("Arial", 12, "bold")).pack()
        self.label_original = tk.Label(frame_original, bg="lightgray")
        self.label_original.pack(expand=True, fill=tk.BOTH)
        
        # Processada
        frame_processada = tk.Frame(frame_imagens)
        frame_processada.pack(side=tk.RIGHT, padx=10, expand=True, fill=tk.BOTH)
        
        tk.Label(frame_processada, text="Imagem Processada", font=("Arial", 12, "bold")).pack()
        self.label_processada = tk.Label(frame_processada, bg="lightgray")
        self.label_processada.pack(expand=True, fill=tk.BOTH)
    
    def abrir_imagem(self):
        caminho = filedialog.askopenfilename(
            filetypes=[("PNG files", "*.png"), ("Todos os arquivos", "*.*")]
        )
        if caminho:
            # Carregar imagem
            self.imagem_original = cv2.imread(caminho)
            
            # Verificar se é colorida
            if len(self.imagem_original.shape) == 3:
                self.is_color = True
                info = f"Colorida (RGB) - {self.imagem_original.shape[1]}x{self.imagem_original.shape[0]}"
            else:
                self.is_color = False
                info = f"Escala de Cinza - {self.imagem_original.shape[1]}x{self.imagem_original.shape[0]}"
            
            self.info_label.config(text=info)
            
            # Exibir imagem original
            self.mostrar_imagem(self.imagem_original, self.label_original)
            
            # Limpar processada
            self.label_processada.config(image="", text="")
    
    def mostrar_imagem(self, imagem, label, tamanho_max=500):
        """Exibe uma imagem no label (redimensionando se necessário)"""
        # Converter BGR (OpenCV) para RGB
        if len(imagem.shape) == 3:
            imagem_rgb = cv2.cvtColor(imagem, cv2.COLOR_BGR2RGB)
        else:
            imagem_rgb = imagem
        
        # Redimensionar
        h, w = imagem_rgb.shape[:2]
        escala = min(tamanho_max/w, tamanho_max/h, 1.0)
        novo_w, novo_h = int(w*escala), int(h*escala)
        
        if escala < 1.0:
            imagem_rgb = cv2.resize(imagem_rgb, (novo_w, novo_h))
        
        # Converter para PIL
        imagem_pil = Image.fromarray(imagem_rgb)
        imagem_tk = ImageTk.PhotoImage(imagem_pil)
        
        label.config(image=imagem_tk)
        label.image = imagem_tk
    
    def aplicar_processo(self):
        if self.imagem_original is None:
            return
        
        processo = self.processo_var.get()
        
        if processo == "Decomposição RGB":
            self.decompor_rgb()
        elif processo == "Decomposição HSV":
            self.decompor_hsv()
        elif processo == "Limiarização":
            self.limiarizar()
        elif processo == "Equalização de Histograma":
            self.equalizar_histograma()
        elif processo == "Filtro Gaussiano":
            self.filtro_gaussiano()
        else:
            return
    
    def decompor_rgb(self):
        if not self.is_color:
            self.info_label.config(text="ERRO: Imagem precisa ser colorida!")
            return
        
        # Separar canais
        b, g, r = cv2.split(self.imagem_original)
        
        # Criar imagem com os 3 canais lado a lado
        h, w = b.shape
        resultado = np.zeros((h, w*3), dtype=np.uint8)
        resultado[:, 0:w] = r
        resultado[:, w:2*w] = g
        resultado[:, 2*w:3*w] = b
        
        self.imagem_processada = resultado
        self.mostrar_imagem(resultado, self.label_processada)
        self.info_label.config(text="RGB: R | G | B")
    
    def decompor_hsv(self):
        if not self.is_color:
            self.info_label.config(text="ERRO: Imagem precisa ser colorida!")
            return
        
        # Converter para HSV
        hsv = cv2.cvtColor(self.imagem_original, cv2.COLOR_BGR2HSV)
        h, s, v = cv2.split(hsv)
        
        # Criar imagem com os 3 canais lado a lado
        h, w = h.shape
        resultado = np.zeros((h, w*3), dtype=np.uint8)
        resultado[:, 0:w] = h
        resultado[:, w:2*w] = s
        resultado[:, 2*w:3*w] = v
        
        self.imagem_processada = resultado
        self.mostrar_imagem(resultado, self.label_processada)
        self.info_label.config(text="HSV: H | S | V")
    
    def limiarizar(self):
        # Converter para cinza se for colorida
        if self.is_color:
            img = cv2.cvtColor(self.imagem_original, cv2.COLOR_BGR2GRAY)
        else:
            img = self.imagem_original
        
        # Limiar simples (k=127 fixo por enquanto)
        _, resultado = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
        
        self.imagem_processada = resultado
        self.mostrar_imagem(resultado, self.label_processada)
        self.info_label.config(text="Limiarização (k=127)")
    
    def equalizar_histograma(self):
        if self.is_color:
            self.info_label.config(text="ERRO: Equalização só para imagens em cinza!")
            return
        
        resultado = cv2.equalizeHist(self.imagem_original)
        self.imagem_processada = resultado
        self.mostrar_imagem(resultado, self.label_processada)
        self.info_label.config(text="Histograma Equalizado")
    
    def filtro_gaussiano(self):
        resultado = cv2.GaussianBlur(self.imagem_original, (5, 5), 1.0)
        self.imagem_processada = resultado
        self.mostrar_imagem(resultado, self.label_processada)
        self.info_label.config(text="Filtro Gaussiano (σ=1.0)")
    
    def salvar_imagem(self):
        if self.imagem_processada is None:
            return
        
        caminho = filedialog.asksaveasfilename(
            defaultextension=".png",
            filetypes=[("PNG files", "*.png")]
        )
        if caminho:
            cv2.imwrite(caminho, self.imagem_processada)
            self.info_label.config(text=f"Imagem salva em: {os.path.basename(caminho)}")

# ===== MAIN =====
if __name__ == "__main__":
    root = tk.Tk()
    app = PDIApp(root)
    root.mainloop()

