import cv2
import numpy as np

def filtro_minimo(imagem, tamanho=3):
    """
    Aplica filtro de mínimo (erosão).
    Útil para remover ruído sal (pixels brancos).
    
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
    
    # Aplicar erosão (mínimo)
    return cv2.erode(imagem, kernel)
