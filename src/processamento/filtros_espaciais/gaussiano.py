import cv2

def filtro_gaussiano(imagem, sigma=1.0, tamanho=5):
    """
    Aplica filtro Gaussiano (suavização com distribuição Gaussiana).
    
    Args:
        imagem: imagem de entrada
        sigma: desvio padrão da distribuição Gaussiana
        tamanho: tamanho da janela (deve ser ímpar)
    
    Returns:
        imagem suavizada
    """
    # Garantir que o tamanho seja ímpar
    if tamanho % 2 == 0:
        tamanho += 1
    
    # Aplicar filtro Gaussiano
    return cv2.GaussianBlur(imagem, (tamanho, tamanho), sigma)
