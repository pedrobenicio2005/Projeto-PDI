import numpy as np

def transformacao_potencia(imagem, c=1.0, gama=0.5):
    """
    Aplica transformação de potência: s = c * (r ^ gama)
    Usada para correção gama (ajuste de brilho/contraste).
    
    Args:
        imagem: imagem de entrada (colorida ou cinza)
        c: ganho (padrão: 1.0)
        gama: expoente (padrão: 0.5)
              - gama < 1: clareia a imagem
              - gama > 1: escurece a imagem
              - gama = 1: não altera
    
    Returns:
        imagem transformada
    """
    # Converter para float e normalizar para [0, 1]
    img_float = np.float32(imagem) / 255.0
    
    # Aplicar potência: c * (img ^ gama)
    resultado = c * (img_float ** gama)
    
    # Voltar para [0, 255]
    resultado = np.uint8(np.clip(resultado * 255, 0, 255))
    
    return resultado

