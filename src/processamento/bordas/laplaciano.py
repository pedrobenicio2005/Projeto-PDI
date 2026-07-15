import cv2
import numpy as np

def realce_laplaciano(imagem):
    """
    Aplica realce por Laplaciano.
    Retorna a imagem realçada e o Laplaciano ajustado.
    
    Args:
        imagem: imagem de entrada (colorida ou cinza)
    
    Returns:
        (imagem_realcada, laplaciano_ajustado)
    """
    # Converter para cinza se for colorida
    if len(imagem.shape) == 3:
        img = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    else:
        img = imagem.copy()
    
    # Calcular o Laplaciano (segunda derivada)
    laplaciano = cv2.Laplacian(img, cv2.CV_64F)
    
    # Ajustar o Laplaciano para visualização (valor absoluto)
    laplaciano_ajustado = np.uint8(np.clip(np.abs(laplaciano), 0, 255))
    
    # Realçar a imagem: original + Laplaciano
    realcada = cv2.addWeighted(img, 1.0, laplaciano_ajustado, 1.0, 0)
    
    return realcada, laplaciano_ajustado
