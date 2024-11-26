# Calculadora Balística

Uma calculadora simples que exibe a trajetória de um projétil considerando alguns fatores como: Velocidade inicial do projétil, ângulo do tiro, coeficiente balístico, massa do projétil, densidade do ar, área transversal do projétil, altura do atirador, altura do alvo e distância entre o atirador e o alvo, fornecendo tanto gráficos 2D quanto 3D interativos.

Este projeto foi desenvolvido em Python, utilizando a biblioteca **CustomTkinter** para a interface gráfica e **Matplotlib** para a visualização de gráficos. 

---

## Funcionalidades

- **Entrada de parâmetros balísticos:**
  - Velocidade inicial do projétil.
  - Ângulo de disparo.
  - Coeficiente balístico (Cd).
  - Massa do projétil.
  - Densidade do ar.
  - Área transversal do projétil.
  - Altura do atirador.
  - Altura do alvo
  - Distância entre o atirador e o alvo.

- **Cálculos :**
  - Trajetória com resistência aerodinâmica.
  - Tempo de voo.
  - Alcance máximo.
  - Altura máxima.

- **Visualização gráfica:**
  - **Gráfico 2D** com a trajetória e marcadores para o atirador e o alvo.
  - **Gráfico 3D** interativo, mostrando a trajetória em perspectiva e as posições do atirador e do alvo.

---
#### Dicionário
theta = angulo theta
D_ar = densidade do ar
## Explicação Física

A calculadora utiliza conceitos fundamentais de física e balística, incluindo:

### 1. **Movimento Parabólico**
A trajetória de um projétil é dada pelas equações do movimento sob a influência da gravidade e da resistência do ar.

#### Sem resistência do ar:
A trajetória seria uma parábola, e as equações são:
- **Alcance horizontal:**  
  x(t) = v_0 * cos(theta) * t
- **Altura vertical:**  
  y(t) = y_0 + v_0 * sin(theta) * t - 1/2 * g * t^2

- **Legenda:**
  - theta: ângulo theta

#### Com resistência do ar:
O movimento é influenciado por uma força oposta à direção do projétil, dada por:
F_d = 1/2 * D_ar * C_d * A * v^2
Onde:
- D_ar: densidade do ar.
- C_d: coeficiente de arrasto.
- A: área transversal do projétil.
- v: velocidade instantânea do projétil.

As equações de movimento se tornam diferenciais e são resolvidas numericamente.

---

### 2. **Força de Arrasto**
A força de resistência reduz a velocidade do projétil e é dada por:  F_d = 1/2 * D_ar * C_d * A * v^2
Esta força é integrada para calcular a posição e velocidade a cada instante.

---

### 3. **Gravidade**
A gravidade atua verticalmente com aceleração constante: g = 9.81 m/s^2

---

### 4. **Cálculo do Alcance e Altura**
- **Altura máxima:**  
  y_max = y_0 + ((v_0 * sin(theta))^2) / 2 * g 
- **Tempo total de voo:**  
  Resolvemos y(t) = 0 numericamente, considerando a resistência do ar.
- **Alcance horizontal:**  
  Integramos x(t) ao longo do tempo de voo.

---

## Como Usar

1. Clone este repositório:
   ```bash
   git clone https://github.com/PedroMagno11/Calculadora-de-trajetoria-balistica.git calculadora-balistica
   cd calculadora-balistica
   ```

2. Execute o seguinte comando para instalar todas as dependências necessárias:
    ```bash
    pip install -r dependencias.txt
    ```

3. Execute o script principal:
   ```bash
   python main.py
   ```

4. Preencha os parâmetros na interface gráfica.

5. Clique em **Calcular** para obter:
   - Resultados numéricos: tempo de voo, alcance e altura máxima.
   - Visualizações gráficas (2D e 3D).

---

## Estrutura do Código

- **`calcular_trajetoria_com_resistencia`:** Realiza os cálculos da trajetória considerando resistência aerodinâmica.
- **Gráficos:**
  - `plot_2d`: Gera o gráfico 2D.
  - `plot_3d`: Gera o gráfico 3D interativo.
- **Interface gráfica:** Criada com **CustomTkinter**.

---

## Visualizações

### Gráfico 2D
- Linha azul: trajetória do projétil.
- Ponto verde: posição do atirador.
- Ponto vermelho: posição do alvo.

### Gráfico 3D
- Trajetória do projétil em perspectiva tridimensional.
- Posição do atirador e do alvo identificadas por marcadores.

---

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests com melhorias.

---

## Autor
- [Pedro Magno](https://github.com/PedroMagno11)