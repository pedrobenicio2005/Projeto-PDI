import cv2
import numpy as np
from .utils import criar_mascara_butterworth, aplicar_filtro_frequencia

def filtro_passa_alta_butterworth(imagem, corte=30, ordem=2):
    """
    Aplica filtro passa-alta Butterworth no domínio da frequência.
    Realça bordas com transição mais suave que o Gaussiano.
    
    Args:
        imagem: imagem de entrada
        corte: frequência de corte
        ordem: ordem do filtro (quanto maior, mais abrupta a transição)
    
    Returns:
        imagem com bordas realçadas
    """
    # Criar máscara Butterworth (passa-baixa)
    mascara_pb = criar_mascara_butterworth(imagem.shape[:2], corte, ordem)
    
    # Passa-alta = 1 - Passa-baixa
    mascara_pa = 1 - mascara_pb
    
    # Aplicar o filtro
    return aplicar_filtro_frequencia(imagem, mascara_pa)
