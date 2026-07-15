import numpy as np

def ruido_gaussiano(imagem, media=0, variancia=25):
    """
    Adiciona ruído gaussiano à imagem
    
    Args:
        imagem: imagem de entrada
        media: média da distribuição (padrão: 0)
        variancia: variância da distribuição (padrão: 25)
    
    Returns:
        imagem com ruído gaussiano
    """
    # Converter para float para evitar overflow
    img_float = np.float32(imagem)
    
    # Gerar ruído gaussiano
    desvio_padrao = np.sqrt(variancia)
    ruido = np.random.normal(media, desvio_padrao, img_float.shape)
    
    # Adicionar ruído à imagem
    resultado = img_float + ruido
    
    # Voltar para [0, 255]
    return np.uint8(np.clip(resultado, 0, 255))
