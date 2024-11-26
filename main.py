import math
import threading
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from mpl_toolkits.mplot3d import Axes3D
import customtkinter as ctk

# Função para calcular trajetória com resistência aerodinâmica
def calcular_trajetoria_com_resistencia(velocidade_inicial, angulo_tiro, coeficiente_balistico, massa_projetil, densidade_ar, area_transversal, altura_inicial, altura_alvo, distancia_alvo, gravidade=9.81, dt=0.01):
    massa = massa_projetil / 1000  # Convertendo gramas para kg
    angulo_rad = math.radians(angulo_tiro)
    v_x = velocidade_inicial * math.cos(angulo_rad)
    v_y = velocidade_inicial * math.sin(angulo_rad)
    x, y = 0, altura_inicial
    trajetoria_x, trajetoria_y = [x], [y]

    # Enquanto o projétil estiver acima do solo
    while y >= 0:
        velocidade = math.sqrt(v_x**2 + v_y**2)
        resistencia = 0.5 * densidade_ar * coeficiente_balistico * area_transversal * velocidade**2
        a_x = -(resistencia / massa) * (v_x / velocidade)  # Aceleração horizontal
        a_y = -(resistencia / massa) * (v_y / velocidade) - gravidade  # Aceleração vertical

        # Atualiza velocidades e posições
        v_x += a_x * dt
        v_y += a_y * dt
        x += v_x * dt
        y += v_y * dt

        # Registrar posições
        trajetoria_x.append(x)
        trajetoria_y.append(max(0, y))  # Garantir que não haja valores negativos para altura

        # Para se passar da posição do alvo
        if x >= distancia_alvo and y <= altura_alvo:
            break

    return {
        "tempo_voo": len(trajetoria_x) * dt,
        "trajetoria_x": trajetoria_x,
        "trajetoria_y": trajetoria_y,
        "alcance_maximo": max(trajetoria_x),
        "altura_maxima": max(trajetoria_y)
    }

# Função para realizar o cálculo em uma thread separada
# essa função vai realizar o cálculo e atualizar os dados 
# que serão exibidos na IHM (Interface Humano Máquina)
def calcular_e_atualizar():
    try:
        velocidade_inicial = float(entry_velocidade.get())
        angulo_tiro = float(entry_angulo.get())
        coeficiente_balistico = float(entry_bc.get())
        peso_projetil = float(entry_peso.get())
        densidade_ar = float(entry_densidade.get())
        area_transversal = float(entry_area.get())
        altura_inicial = float(entry_altura_inicial.get())
        altura_alvo = float(entry_altura_alvo.get())
        alcance_alvo = float(entry_alcance_alvo.get())

        # Calcular a trajetória
        resultado = calcular_trajetoria_com_resistencia(
            velocidade_inicial, angulo_tiro, coeficiente_balistico, peso_projetil,
            densidade_ar, area_transversal, altura_inicial, altura_alvo, alcance_alvo
        )

        # Atualizar informações na IHM
        label_resultados.configure(
            text=f"Tempo de voo: {resultado['tempo_voo']:.2f} s\n"
                 f"Alcance máximo: {resultado['alcance_maximo']:.2f} m\n"
                 f"Altura máxima: {resultado['altura_maxima']:.2f} m"
        )

        # Plotar os gráficos
        plot_2d(resultado['trajetoria_x'], resultado['trajetoria_y'], altura_inicial, alcance_alvo, altura_alvo)
        plot_3d(resultado['trajetoria_x'], resultado['trajetoria_y'], altura_inicial, alcance_alvo, altura_alvo)

    except ValueError:
        label_resultados.configure(text="Por favor, insira valores válidos!")

# Função para plotar o gráfico 2D
def plot_2d(x, y, altura_inicial, alcance_alvo, altura_alvo):
    fig_2d.clear()
    ax = fig_2d.add_subplot(111)
    
    # Desenha a trajetória
    ax.plot(x, y, label="Trajetória", color="blue")
    
    # Posição do atirador
    ax.scatter([0], [altura_inicial], color="green", label="Atirador")
    
    # Posição do alvo
    ax.scatter([alcance_alvo], [altura_alvo], color="red", label="Alvo")
    
    ax.set_title("Trajetória Balística 2D")
    ax.set_xlabel("Distância (m)")
    ax.set_ylabel("Altura (m)")
    ax.legend()
    canvas_2d.draw()

# Função para plotar o gráfico 3D
def plot_3d(x, y, altura_inicial, alcance_alvo, altura_alvo):
    fig_3d.clear()
    ax = fig_3d.add_subplot(111, projection='3d')
    z = [0] * len(x)  # Para simular um gráfico em linha reta no eixo Z
    ax.plot(x, z, y, label="Trajetória", color="blue")

    # Adicionando a posição do atirador
    ax.scatter([0], [0], [altura_inicial], color="green", s=50, label="Atirador")  # Posição do atirador
    
    # Adicionando o alvo
    ax.scatter([alcance_alvo], [0], [altura_alvo], color="red", s=50, label="Alvo")  # Posição do alvo
    
    # Configurações do gráfico
    ax.set_title("Trajetória Balística 3D")
    ax.set_xlabel("Distância (m)")
    # OBS: Não possui variação lateral, mas este eixo é necessário
    ax.set_ylabel("Lateral (m)")  
    ax.set_zlabel("Altura (m)")
    # ax.legend()
    canvas_3d.draw()

# Interface gráfica
# set_appearence_mode define a aparência do sistema ("System", "Dark", "Light")
ctk.set_appearance_mode("System")
ctk.set_default_color_theme("dark-blue")

app = ctk.CTk()
app.title("Calculadora Balística")
app.geometry("1200x850")

frame_inputs = ctk.CTkFrame(app)
frame_inputs.pack(pady=10, padx=10, fill="x")

# Entradas IHM
labels_entries = [
    ("Velocidade inicial (m/s):", "entry_velocidade"),
    ("Ângulo do tiro (graus):", "entry_angulo"),
    ("Coeficiente balístico (Cd):", "entry_bc"),
    ("Massa do projétil (g):", "entry_peso"),
    ("Densidade do ar (kg/m³):", "entry_densidade"),
    ("Área transversal do projétil (m²):", "entry_area"),
    ("Altura do atirador (m):", "entry_altura_inicial"),
    ("Altura do alvo (m):", "entry_altura_alvo"),
    ("Distância até o alvo (m):", "entry_alcance_alvo"),
]

entries = {}
for label_text, entry_var in labels_entries:
    frame = ctk.CTkFrame(frame_inputs)
    frame.pack(pady=5, padx=5, fill="x")
    label = ctk.CTkLabel(frame, text=label_text, width=300, anchor="w")
    label.pack(side="left", padx=10)
    entry = ctk.CTkEntry(frame, width=500)
    entry.pack(side="right", padx=10)
    entries[entry_var] = entry

entry_velocidade = entries["entry_velocidade"]
entry_angulo = entries["entry_angulo"]
entry_bc = entries["entry_bc"]
entry_peso = entries["entry_peso"]
entry_densidade = entries["entry_densidade"]
entry_area = entries["entry_area"]
entry_altura_inicial = entries["entry_altura_inicial"]
entry_altura_alvo = entries["entry_altura_alvo"]
entry_alcance_alvo = entries["entry_alcance_alvo"]

# Botão para calcular
btn_calcular = ctk.CTkButton(app, text="Calcular", command=lambda: threading.Thread(target=calcular_e_atualizar).start())
btn_calcular.pack(pady=10)

# Resultados
label_resultados = ctk.CTkLabel(app, text="", justify="left")
label_resultados.pack(pady=10)

# Gráficos
frame_graphs = ctk.CTkFrame(app)
frame_graphs.pack(pady=10, padx=10, fill="both", expand=True)

# Gráfico 2D
fig_2d = plt.Figure(figsize=(6, 4))
canvas_2d = FigureCanvasTkAgg(fig_2d, master=frame_graphs)
canvas_2d.get_tk_widget().pack(side="left", fill="both", expand=True)

# Gráfico 3D
fig_3d = plt.Figure(figsize=(6, 4))
canvas_3d = FigureCanvasTkAgg(fig_3d, master=frame_graphs)
canvas_3d.get_tk_widget().pack(side="right", fill="both", expand=True)

app.mainloop()
