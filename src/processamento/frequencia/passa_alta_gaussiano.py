import cv2
import numpy as np
from .utils import criar_mascara_gaussiana, aplicar_filtro_frequencia

def filtro_passa_alta_gaussiano(imagem, corte=30):
    """
    Aplica filtro passa-alta Gaussiano no domínio da frequência.
    Realça bordas removendo baixas frequências (variações suaves).
    
    Args:
        imagem: imagem de entrada
        corte: frequência de corte (quanto menor, mais bordas)
    
    Returns:
        imagem com bordas realçadas
    """
    # Criar máscara Gaussiana (passa-baixa)
    mascara_pb = criar_mascara_gaussiana(imagem.shape[:2], corte)
    
    # Passa-alta = 1 - Passa-baixa
    mascara_pa = 1 - mascara_pb
    
    # Aplicar o filtro
    return aplicar_filtro_frequencia(imagem, mascara_pa)
