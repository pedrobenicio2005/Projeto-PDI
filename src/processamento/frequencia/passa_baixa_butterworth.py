import cv2
import numpy as np
from .utils import criar_mascara_butterworth, aplicar_filtro_frequencia

def filtro_passa_baixa_butterworth(imagem, corte=30, ordem=2):
    """
    Aplica filtro passa-baixa Butterworth no domínio da frequência.
    Suaviza a imagem com transição mais suave que o Gaussiano.
    
    Args:
        imagem: imagem de entrada
        corte: frequência de corte
        ordem: ordem do filtro (quanto maior, mais abrupta a transição)
    
    Returns:
        imagem suavizada
    """
    # Criar máscara Butterworth
    mascara = criar_mascara_butterworth(imagem.shape[:2], corte, ordem)
    
    # Aplicar o filtro
    return aplicar_filtro_frequencia(imagem, mascara)
