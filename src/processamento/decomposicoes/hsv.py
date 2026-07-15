import cv2
import numpy as np

def decompor_hsv(imagem):
    """
    Decompõe uma imagem RGB em seus 3 canais HSV (H, S, V).
    Retorna as 3 imagens em escala de cinza lado a lado.
    
    Args:
        imagem: imagem colorida (BGR no OpenCV)
    
    Returns:
        imagem com os 3 canais lado a lado (H | S | V)
    """
    # Converter BGR para HSV
    hsv = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)
    
    # Separar os canais
    h, s, v = cv2.split(hsv)
    
    # Dimensões da imagem
    h, w = h.shape
    
    # Criar imagem resultante (3x mais larga)
    resultado = np.zeros((h, w*3), dtype=np.uint8)
    
    # Colocar os canais lado a lado: H | S | V
    resultado[:, 0:w] = h      # Canal Hue (Matiz)
    resultado[:, w:2*w] = s    # Canal Saturation (Saturação)
    resultado[:, 2*w:3*w] = v  # Canal Value (Valor/Intensidade)
    
    return resultado
