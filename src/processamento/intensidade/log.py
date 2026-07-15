import numpy as np

def transformacao_log(imagem, c=1.0):
    """
    Aplica transformação logarítmica: s = c * log(1 + r)
    Usada para expandir regiões escuras e comprimir regiões claras.
    
    Args:
        imagem: imagem de entrada (colorida ou cinza)
        c: ganho da transformação (padrão: 1.0)
    
    Returns:
        imagem transformada
    """
    # Converter para float para evitar overflow
    img_float = np.float32(imagem)
    
    # Aplicar log: c * log(1 + img)
    resultado = c * np.log1p(img_float)
    
    # Normalizar para [0, 255]
    resultado = np.uint8(np.clip(resultado, 0, 255))
    
    return resultado
