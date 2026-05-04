from tkinter import messagebox
import matplotlib.pyplot as plt
from PerceptronAnalistaFutbol import PerceptronAnalistaFutbol



class Controlador:
    def __init__(self, Vista, Grafico, Ventana, modelo):
        self.vista, self.grafico, self.ventana, self.modelo = Vista, Grafico, Ventana, modelo

        self.vista.btnEntrenamiento.config(command=self.EventEntrenamiento)
        self.vista.btnAprendizaje.config(command=self.EventAprendizaje)
        self.vista.btnPrueba.config(command=self.EventPrueba)
        self.grafico.canvas.mpl_connect('close_event', lambda e: plt.close())

    def EventEntrenamiento(self):
        self.modelo.Entrenamiento()

        self.vista.lblTituloPrincipal.config(text="COMPLETADO" if not self.modelo.bandera else "ENTRENANDO")
        self.vista.lblEntrada1.config(text=f"Goles Favor: {self.modelo.getEntradas(1)}")
        self.vista.lblEntrada2.config(text=f"Goles Contra: {self.modelo.getEntradas(2)}")
        self.vista.lblEntrada3.config(text=f"Visitante: {self.modelo.getEntradas(3)}")
        self.vista.lblPeso1.config(text=f"Campeón: {self.modelo.y[0]}")
        self.vista.lblPeso2.config(text=f"Media Tabla: {self.modelo.y[1]}")
        self.vista.lblUmbral.config(text=f"Descenso: {self.modelo.y[2]}")
        self.vista.lblSalidaDeseada.config(text=f"Deseada: {self.modelo.getSalidas(self.modelo.fila)}")
        self.vista.lblSalidaObtenida.config(text=f"Obtenida: {self.modelo.y}")

    def EventAprendizaje(self):
        self.modelo.Aprendizaje()
        messagebox.showinfo("Aprendizaje", "En fútbol los pesos se ajustan durante el entrenamiento.")

    def EventPrueba(self):
        try:
            goles_favor = int(self.vista.jtfEntrada1.get())
            goles_contra = int(self.vista.jtfEntrada2.get())
            ganados_visitante = int(self.vista.jtfEntrada3.get())

            resultado, sumas, categoria = self.modelo.PruebaFuncionamiento(
                goles_favor,
                goles_contra,
                ganados_visitante
            )

            self.vista.lblPruebaSalidaObtenida.config(
                text=f"Salida: {resultado} | {categoria}"
            )

        except:
            messagebox.showerror("Error", "Ingrese: goles a favor, goles en contra y ganados visitante.")