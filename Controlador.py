from tkinter import messagebox
import matplotlib.pyplot as plt


class Controlador:
    def __init__(self, Vista, Grafico, Ventana, modelo):
        self.vista, self.grafico, self.ventana, self.modelo = Vista, Grafico, Ventana, modelo
        self.vista.btnEntrenamiento.config(command=self.EventEntrenamiento)
        self.vista.btnAprendizaje.config(command=self.EventAprendizaje)
        self.vista.btnPrueba.config(command=self.EventPrueba)
        self.grafico.canvas.mpl_connect('close_event', lambda e: plt.close())

    def EventEntrenamiento(self):
        self.modelo.Entrenamiento()

        errores = self.modelo.errors_history[-1] if self.modelo.errors_history else 0
        estado = "ENTRENAMIENTO COMPLETO" if self.modelo.training_complete else "ENTRENANDO"

        self.vista.lblTituloPrincipal.config(text=estado)
        self.vista.lblEpoca.config(text=f"Época: {self.modelo.epoch_count}")
        self.vista.lblErrores.config(text=f"Errores: {errores}")
        self.vista.lblEntrada1.config(text=f"Goles Favor: {self.modelo.getEntradas(1)}")
        self.vista.lblEntrada2.config(text=f"Goles Contra: {self.modelo.getEntradas(2)}")
        self.vista.lblEntrada3.config(text=f"Visitante: {self.modelo.getEntradas(3)}")
        self.vista.lblPeso1.config(text=f"Campeón: {self.modelo.pesos[0].tolist()}")
        self.vista.lblPeso2.config(text=f"Media Tabla: {self.modelo.pesos[1].tolist()}")
        self.vista.lblUmbral.config(text=f"Descenso: {self.modelo.pesos[2].tolist()}")
        self.vista.lblSalidaDeseada.config(text=f"Deseada: {self.modelo.salidas_deseadas[-1].tolist()}")
        self.vista.lblSalidaObtenida.config(text=f"Salida final: {self.modelo.y.tolist()}")

        # FIX: muestra el factor de aprendizaje real del modelo (antes estaba hardcodeado en Vista)
        self.vista.lblFactorAprendizaje.config(
            text=f"Factor Aprendizaje: {self.modelo.factor_aprendizaje}"
        )

        self.grafico.actualizar()

    def EventAprendizaje(self):
        errores = self.modelo.Aprendizaje()

        estado = "APRENDIZAJE COMPLETO" if self.modelo.training_complete else "APRENDIENDO"
        self.vista.lblTituloPrincipal.config(text=estado)
        self.vista.lblEpoca.config(text=f"Época: {self.modelo.epoch_count}")
        self.vista.lblErrores.config(text=f"Errores: {errores}")
        self.vista.lblPeso1.config(text=f"Campeón: {self.modelo.pesos[0].tolist()}")
        self.vista.lblPeso2.config(text=f"Media Tabla: {self.modelo.pesos[1].tolist()}")
        self.vista.lblUmbral.config(text=f"Descenso: {self.modelo.pesos[2].tolist()}")
        self.vista.lblSalidaObtenida.config(text=f"Salida actual: {self.modelo.y.tolist()}")

        # FIX: muestra el factor de aprendizaje real del modelo
        self.vista.lblFactorAprendizaje.config(
            text=f"Factor Aprendizaje: {self.modelo.factor_aprendizaje}"
        )

        self.grafico.actualizar()

        if self.modelo.training_complete:
            messagebox.showinfo("Aprendizaje", f"Modelo entrenado en {self.modelo.epoch_count} época(s).")
        else:
            messagebox.showinfo("Aprendizaje", f"Una época de aprendizaje completada. Errores: {errores}.")

    def EventPrueba(self):
        try:
            goles_favor = int(self.vista.jtfEntrada1.get())
            goles_contra = int(self.vista.jtfEntrada2.get())
            ganados_visitante = int(self.vista.jtfEntrada3.get())

            _, _, categoria = self.modelo.clasificar_equipo(
                goles_favor,
                goles_contra,
                ganados_visitante
            )

            self.vista.lblPruebaSalidaObtenida.config(text=categoria)

        except ValueError:
            messagebox.showerror("Error", "Ingrese: goles a favor, goles en contra y ganados visitante.")