import cv2
import numpy as np

def fatiamento_intensidade(imagem, A=100, B=200, preservar_fundo=True):
    """
    Fatia a imagem na faixa [A, B]
    preservar_fundo=True: fundo mantém valor original
    preservar_fundo=False: fundo fica 0 (preto)
    """
    # Converter para cinza se for colorida
    if len(imagem.shape) == 3:
        img = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    else:
        img = imagem.copy()
    
    # Criar máscara com a faixa de interesse
    mascara = np.zeros_like(img)
    mascara[(img >= A) & (img <= B)] = 255
    
    if preservar_fundo:
        # Aplicar a máscara preservando o fundo
        resultado = cv2.bitwise_and(img, mascara)
    else:
        # Fundo fica preto (0)
        resultado = np.zeros_like(img)
        resultado[(img >= A) & (img <= B)] = img[(img >= A) & (img <= B)]
    
    return resultado

