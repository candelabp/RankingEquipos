import tkinter

from Vista import Vista
from Grafico import Grafico
from Controlador import Controlador
from PerceptronAnalistaFutbol import PerceptronAnalistaFutbol


if __name__ == "__main__":
    ventana = tkinter.Tk()

    modelo = PerceptronAnalistaFutbol()
    vista = Vista(ventana)
    grafico = Grafico(ventana, modelo)
    controlador = Controlador(vista, grafico, ventana, modelo)

    ventana.mainloop()