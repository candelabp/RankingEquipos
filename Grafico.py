from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class Grafico:

    def __init__(self, frame, modelo):
        self.frame = frame
        self.modelo = modelo

        self.figura = Figure(figsize=(6, 5), dpi=100)
        self.ax_error, self.ax_weights = self.figura.subplots(2, 1, sharex=False)

        self.canvas = FigureCanvasTkAgg(self.figura, master=self.frame)
        self.canvas.get_tk_widget().pack(fill="both", expand=True)

        self.DibujarEjes()

    def DibujarEjes(self):
        self.ax_error.clear()
        self.ax_weights.clear()

        self.ax_error.axis('off')
        self.ax_error.text(
            0.5,
            0.7,
            "Analista de Fútbol",
            ha="center",
            va="center",
            fontsize=12,
            fontweight='bold'
        )
        self.ax_error.text(
            0.5,
            0.45,
            "Modelo con 3 entradas:\nGoles a favor\nGoles en contra\nGanados visitante",
            ha="center",
            va="center",
            fontsize=10
        )
        self.ax_error.text(
            0.5,
            0.2,
            "Salida esperada:\n[Campeón, Media Tabla, Descenso]",
            ha="center",
            va="center",
            fontsize=10
        )

        self.ax_weights.axis('off')
        self.canvas.draw()

    def actualizar(self):
        self.ax_error.clear()
        self.ax_weights.clear()

        if self.modelo.errors_history:
            epocas = list(range(1, len(self.modelo.errors_history) + 1))
            self.ax_error.plot(epocas, self.modelo.errors_history, marker='o', color='#3f51b5')
            self.ax_error.set_title('Errores por época')
            self.ax_error.set_xlabel('Época')
            self.ax_error.set_ylabel('Errores')
            self.ax_error.set_ylim(bottom=0)
            self.ax_error.grid(True, linestyle='--', alpha=0.4)

            pesos_norma = [sum(abs(w) for w in self.modelo.pesos[i]) for i in range(3)]
            self.ax_weights.bar(self.modelo.nombres_neuronas, pesos_norma, color=['#4caf50', '#2196f3', '#ff9800'])
            self.ax_weights.set_title('Magnitud de pesos por categoría')
            self.ax_weights.set_ylabel('Magnitud')
        else:
            self.ax_error.axis('off')
            self.ax_error.text(
                0.5,
                0.6,
                "Presiona 'Entrenamiento' para ajustar el perceptrón.",
                ha='center',
                va='center',
                fontsize=11
            )
            self.ax_weights.axis('off')
            self.ax_weights.text(
                0.5,
                0.5,
                "El gráfico mostrará la evolución de errores y los pesos finales.",
                ha='center',
                va='center',
                fontsize=10
            )

        self.canvas.draw()
