import cv2
import numpy as np

def decompor_rgb(imagem):
    """
    Decompõe uma imagem RGB em seus 3 canais (R, G, B).
    Retorna as 3 imagens em escala de cinza lado a lado.
    
    Args:
        imagem: imagem colorida (BGR no OpenCV)
    
    Returns:
        imagem com os 3 canais lado a lado (R | G | B)
    """
    # Separar os canais BGR (OpenCV usa BGR)
    b, g, r = cv2.split(imagem)
    
    # Dimensões da imagem
    h, w = b.shape
    
    # Criar imagem resultante (3x mais larga)
    resultado = np.zeros((h, w*3), dtype=np.uint8)
    
    # Colocar os canais lado a lado: R | G | B
    resultado[:, 0:w] = r      # Canal Red (Vermelho)
    resultado[:, w:2*w] = g    # Canal Green (Verde)
    resultado[:, 2*w:3*w] = b  # Canal Blue (Azul)
    
    return resultado

