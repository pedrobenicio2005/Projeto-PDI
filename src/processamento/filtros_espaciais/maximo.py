import cv2
import numpy as np

def filtro_maximo(imagem, tamanho=3):
    """
    Aplica filtro de máximo (dilatação).
    Útil para remover ruído pimenta (pixels pretos).
    
    Args:
        imagem: imagem de entrada
        tamanho: tamanho da janela (deve ser ímpar)
    
    Returns:
        imagem filtrada
    """
    # Garantir que o tamanho seja ímpar
    if tamanho % 2 == 0:
        tamanho += 1
    
    # Criar kernel (matriz de 1s)
    kernel = np.ones((tamanho, tamanho), np.uint8)
    
    # Aplicar dilatação (máximo)
    return cv2.dilate(imagem, kernel)
