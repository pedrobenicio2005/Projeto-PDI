import cv2
import numpy as np
from .utils import criar_mascara_gaussiana, aplicar_filtro_frequencia

def filtro_passa_baixa_gaussiano(imagem, corte=30):
    """
    Aplica filtro passa-baixa Gaussiano no domínio da frequência.
    Suaviza a imagem removendo altas frequências (ruídos e detalhes finos).
    
    Args:
        imagem: imagem de entrada
        corte: frequência de corte (quanto menor, mais suaviza)
    
    Returns:
        imagem suavizada
    """
    # Criar máscara Gaussiana
    mascara = criar_mascara_gaussiana(imagem.shape[:2], corte)
    
    # Aplicar o filtro
    return aplicar_filtro_frequencia(imagem, mascara)
