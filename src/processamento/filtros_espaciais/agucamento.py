import cv2
import numpy as np

def mascara_agucamento(imagem, ganho=1.0, tamanho=5):
    """
    Máscara de aguçamento: realça bordas
    Fórmula: original + ganho * (original - borrada)
    """
    # Borrar a imagem com filtro Gaussiano
    if tamanho % 2 == 0:
        tamanho += 1
    borrada = cv2.GaussianBlur(imagem, (tamanho, tamanho), 0)
    
    # Calcular a máscara (original - borrada)
    mascara = cv2.subtract(imagem, borrada)
    
    # Aplicar o ganho e somar com a original
    resultado = cv2.addWeighted(imagem, 1.0, mascara, ganho, 0)
    
    return resultado
