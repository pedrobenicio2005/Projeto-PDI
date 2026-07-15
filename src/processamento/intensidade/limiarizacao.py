import cv2
import numpy as np

def limiarizar(imagem, k=127):
    """
    Aplica limiarização à imagem.
    
    Args:
        imagem: imagem de entrada (colorida ou cinza)
        k: valor do limiar (0 a 255)
    
    Returns:
        imagem binarizada (preto e branco)
    """
    # Converter para cinza se for colorida
    if len(imagem.shape) == 3:
        img = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    else:
        img = imagem.copy()
    
    # Aplicar limiarização
    _, resultado = cv2.threshold(img, k, 255, cv2.THRESH_BINARY)
    
    return resultado
