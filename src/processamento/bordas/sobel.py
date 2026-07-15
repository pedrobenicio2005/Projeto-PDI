import cv2
import numpy as np

def gradiente_sobel(imagem):
    """
    Calcula o gradiente de Sobel da imagem.
    Detecta bordas usando as derivadas nas direções X e Y.
    
    Args:
        imagem: imagem de entrada (colorida ou cinza)
    
    Returns:
        imagem com o gradiente de Sobel (magnitude)
    """
    # Converter para cinza se for colorida
    if len(imagem.shape) == 3:
        img = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    else:
        img = imagem.copy()
    
    # Calcular gradiente em X (horizontal)
    sobel_x = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize=3)
    
    # Calcular gradiente em Y (vertical)
    sobel_y = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize=3)
    
    # Calcular a magnitude do gradiente
    magnitude = np.sqrt(sobel_x**2 + sobel_y**2)
    
    # Normalizar para [0, 255]
    return np.uint8(np.clip(magnitude, 0, 255))
