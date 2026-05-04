from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt


class Grafico:

    def __init__(self, Ventana, modelo):
        self.ventana = Ventana
        self.modelo = modelo

        # Creamos la figura y el canvas
        self.figura = Figure(figsize=(5, 4), dpi=100)
        self.subgrafico = self.figura.add_subplot(111)

        self.canvas = FigureCanvasTkAgg(self.figura, master=self.ventana)
        self.canvas.get_tk_widget().grid(row=7, column=2, columnspan=5)

        # Dibujamos el estado inicial
        self.DibujarEjes()

    def DibujarEjes(self):
        self.subgrafico.clear()
        self.subgrafico.grid(True)

        self.subgrafico.set_title("Analista de Fútbol")
        self.subgrafico.text(
            0.5,
            0.6,
            "Modelo con 3 entradas:\n"
            "Goles a favor\n"
            "Goles en contra\n"
            "Ganados visitante",
            ha="center",
            va="center",
            transform=self.subgrafico.transAxes
        )
        self.subgrafico.text(
            0.5,
            0.35,
            "Salida:\n[Campeón, Media Tabla, Descenso]",
            ha="center",
            va="center",
            transform=self.subgrafico.transAxes
        )

        self.canvas.draw()

    def GraficarRecta(self, x1, x2, y1, y2, repeticion):
        self.DibujarEjes()