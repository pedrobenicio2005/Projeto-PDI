import numpy as np

def ruido_sal(imagem, densidade=0.05):
    """
    Adiciona ruído sal (pixels brancos) à imagem
    
    Args:
        imagem: imagem de entrada
        densidade: proporção de pixels afetados (0 a 1)
    
    Returns:
        imagem com ruído sal
    """
    # Verificar dimensões
    if len(imagem.shape) == 3:
        h, w, c = imagem.shape
    else:
        h, w = imagem.shape
        c = 1
    
    # Criar cópia
    resultado = imagem.copy()
    
    # Número de pixels a serem modificados
    num_pixels = int(h * w * densidade)
    
    # Coordenadas aleatórias
    coords_x = np.random.randint(0, w, num_pixels)
    coords_y = np.random.randint(0, h, num_pixels)
    
    # Aplicar sal (branco = 255)
    if c == 1:
        resultado[coords_y, coords_x] = 255
    else:
        resultado[coords_y, coords_x] = [255, 255, 255]
    
    return resultado
