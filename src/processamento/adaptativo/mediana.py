import cv2
import numpy as np

def filtro_adaptativo_mediana(imagem, tamanho_maximo=7):
    """
    Filtro Adaptativo de Mediana para remoção de ruído sal e pimenta.
    
    Funcionamento:
    1. Começa com janela 3x3
    2. Calcula mínimo, máximo e mediana da janela
    3. Se a mediana está entre mínimo e máximo, verifica o pixel central
    4. Se o pixel central é ruído, substitui pela mediana
    5. Se não, mantém o pixel original
    6. Se a mediana é igual ao mínimo ou máximo, aumenta a janela
    7. Repete até encontrar um bom valor ou atingir o tamanho máximo
    
    Args:
        imagem: imagem de entrada (colorida ou cinza)
        tamanho_maximo: tamanho máximo da janela (deve ser ímpar)
    
    Returns:
        imagem filtrada
    """
    # Garantir que o tamanho máximo seja ímpar
    if tamanho_maximo % 2 == 0:
        tamanho_maximo += 1
    
    # Converter para cinza se for colorida
    if len(imagem.shape) == 3:
        img = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    else:
        img = imagem.copy()
    
    h, w = img.shape
    resultado = np.zeros_like(img)
    
    # Para cada pixel da imagem
    for i in range(h):
        for j in range(w):
            # Começa com janela 3x3
            tamanho = 3
            
            # Loop para aumentar a janela até o tamanho máximo
            while tamanho <= tamanho_maximo:
                # Calcular a metade da janela
                metade = tamanho // 2
                
                # Definir limites da janela (cuidado com bordas)
                i_min = max(0, i - metade)
                i_max = min(h, i + metade + 1)
                j_min = max(0, j - metade)
                j_max = min(w, j + metade + 1)
                
                # Extrair a janela
                janela = img[i_min:i_max, j_min:j_max]
                
                # Calcular estatísticas da janela
                minimo = np.min(janela)
                maximo = np.max(janela)
                mediana = np.median(janela)
                pixel_central = img[i, j]
                
                # Verificar se a mediana é um valor "válido"
                # (não é igual ao mínimo ou máximo)
                if minimo < mediana < maximo:
                    # A mediana é válida
                    # Verificar se o pixel central é ruído
                    if minimo < pixel_central < maximo:
                        # Pixel central NÃO é ruído, manter original
                        resultado[i, j] = pixel_central
                    else:
                        # Pixel central É ruído, substituir pela mediana
                        resultado[i, j] = int(mediana)
                    # Sair do loop (encontrou uma solução)
                    break
                else:
                    # A mediana não é válida (é igual ao mínimo ou máximo)
                    # Aumentar a janela e tentar novamente
                    tamanho += 2
            else:
                # Se saiu do loop sem break (atingiu o tamanho máximo)
                # Usar a mediana da janela máxima
                metade = tamanho_maximo // 2
                i_min = max(0, i - metade)
                i_max = min(h, i + metade + 1)
                j_min = max(0, j - metade)
                j_max = min(w, j + metade + 1)
                janela = img[i_min:i_max, j_min:j_max]
                resultado[i, j] = int(np.median(janela))
    
    return resultado
