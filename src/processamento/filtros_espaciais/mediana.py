import cv2

def filtro_mediana(imagem, tamanho=3):
    """
    Aplica filtro de mediana (substitui cada pixel pela mediana da vizinhança).
    Ótimo para remover ruído sal e pimenta.
    
    Args:
        imagem: imagem de entrada
        tamanho: tamanho da janela (deve ser ímpar)
    
    Returns:
        imagem filtrada
    """
    # Garantir que o tamanho seja ímpar
    if tamanho % 2 == 0:
        tamanho += 1
    
    # Aplicar filtro de mediana
    return cv2.medianBlur(imagem, tamanho)
