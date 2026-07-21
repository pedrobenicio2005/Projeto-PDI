import numpy as np

def criar_mascara_gaussiana(shape, corte):
    """
    Cria uma máscara Gaussiana no domínio da frequência.
    
    Args:
        shape: (altura, largura) da imagem
        corte: frequência de corte (quanto maior, mais passa)
    
    Returns:
        Máscara Gaussiana (valores entre 0 e 1)
    """
    h, w = shape
    centro_h, centro_w = h // 2, w // 2
    
    # Criar coordenadas
    y, x = np.ogrid[:h, :w]
    
    # Calcular distância ao centro
    distancia = np.sqrt((x - centro_w)**2 + (y - centro_h)**2)
    
    # Máscara Gaussiana: exp(-D^2 / (2 * corte^2))
    mascara = np.exp(-(distancia**2) / (2 * (corte**2)))
    
    return mascara

def criar_mascara_butterworth(shape, corte, ordem):
    """
    Cria uma máscara Butterworth no domínio da frequência.
    
    Args:
        shape: (altura, largura) da imagem
        corte: frequência de corte
        ordem: ordem do filtro (quanto maior, mais abrupta a transição)
    
    Returns:
        Máscara Butterworth (valores entre 0 e 1)
    """
    h, w = shape
    centro_h, centro_w = h // 2, w // 2
    
    # Criar coordenadas
    y, x = np.ogrid[:h, :w]
    
    # Calcular distância ao centro
    distancia = np.sqrt((x - centro_w)**2 + (y - centro_h)**2)
    
    # Máscara Butterworth: 1 / (1 + (D/corte)^(2*ordem))
    # Evitar divisão por zero
    with np.errstate(divide='ignore', invalid='ignore'):
        mascara = 1 / (1 + (distancia / (corte + 1e-10))**(2 * ordem))
        mascara[distancia == 0] = 1  # Centro (frequência zero) sempre passa
    
    return mascara

def aplicar_filtro_frequencia(imagem, mascara):
    """
    Aplica um filtro no domínio da frequência.
    
    Args:
        imagem: imagem de entrada
        mascara: máscara no domínio da frequência
    
    Returns:
        imagem filtrada
    """
    # Converter para cinza se for colorida
    if len(imagem.shape) == 3:
        img = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    else:
        img = imagem.copy()
    
    # Transformada de Fourier
    f = np.fft.fft2(img)
    f_shift = np.fft.fftshift(f)
    
    # Aplicar a máscara
    f_filtrado = f_shift * mascara
    
    # Transformada inversa
    f_ishift = np.fft.ifftshift(f_filtrado)
    img_filtrada = np.fft.ifft2(f_ishift)
    img_filtrada = np.abs(img_filtrada)
    
    return np.uint8(np.clip(img_filtrada, 0, 255))
