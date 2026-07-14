import numpy as np

def ruido_sal_pimenta(imagem, densidade=0.05):
    """
    Adiciona ruído sal e pimenta
    densidade: proporção de pixels afetados (0 a 1)
    """
    # Verificar se a imagem é colorida
    if len(imagem.shape) == 3:
        h, w, c = imagem.shape
    else:
        h, w = imagem.shape
        c = 1
    
    # Criar cópia da imagem
    resultado = imagem.copy()
    
    # Número de pixels a serem modificados
    num_pixels = int(h * w * densidade)
    
    # Coordenadas aleatórias para sal (branco)
    coords_x = np.random.randint(0, w, num_pixels // 2)
    coords_y = np.random.randint(0, h, num_pixels // 2)
    
    # Coordenadas aleatórias para pimenta (preto)
    coords_x2 = np.random.randint(0, w, num_pixels // 2)
    coords_y2 = np.random.randint(0, h, num_pixels // 2)
    
    # Aplicar sal (branco = 255)
    if c == 1:
        resultado[coords_y, coords_x] = 255
        resultado[coords_y2, coords_x2] = 0
    else:
        resultado[coords_y, coords_x] = [255, 255, 255]
        resultado[coords_y2, coords_x2] = [0, 0, 0]
    
    return resultado
