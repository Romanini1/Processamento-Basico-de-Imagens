
# Projeto de Processamento de Imagens com Filtros

Este projeto contém a aplicação de seis filtros de processamento de imagens utilizando a linguagem Python e a biblioteca OpenCV. A imagem utilizada foi aplicada a cada filtro individualmente.

## 1. Realce e Ajuste de Intensidade
**Filtro:** Ajuste de contraste e brilho  
**Técnica:** `cv2.convertScaleAbs()` com `alpha=1.5` e `beta=30`  
**Objetivo:** Destacar áreas claras e escuras, intensificando as cores e a iluminação da imagem.

## 2. Redução de Ruído e Suavização
**Filtro:** Suavização com desfoque gaussiano  
**Técnica:** `cv2.GaussianBlur()` com kernel 5x5  
**Objetivo:** Suavizar imperfeições e ruídos visuais mantendo os detalhes relevantes.

## 3. Detecção de Bordas
**Filtro:** Detector de bordas de Canny  
**Técnica:** `cv2.Canny()` com limiares 100 e 200  
**Objetivo:** Realçar contornos nítidos e transições fortes na imagem.

## 4. Detecção de Formas e Texturas
**Filtro:** Detecção de contornos  
**Técnica:** `cv2.findContours()` e `cv2.drawContours()`  
**Objetivo:** Identificar formas geométricas e padrões visuais presentes na imagem.

## 5. Transformações Geométricas
**Filtro:** Redimensionamento  
**Técnica:** `cv2.resize()` para 300x300 pixels  
**Objetivo:** Demonstrar transformação geométrica simples para ajuste de tamanho.

## 6. Filtros Morfológicos
**Filtro:** Fechamento morfológico  
**Técnica:** `cv2.morphologyEx()` com operação `MORPH_CLOSE`  
**Objetivo:** Preencher pequenos buracos em regiões segmentadas da imagem, útil em pré-processamento de segmentações binárias.

---

### Como Executar
Cada pasta contém:
- `original.jpg` ou `original_segmentada.jpg`: imagem de entrada.
- `resultado.jpg`: imagem após aplicação do filtro.

Para aplicar os filtros novamente, basta utilizar os scripts Python correspondentes com a biblioteca OpenCV instalada.

---
