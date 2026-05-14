import tkinter
from tkinter import ttk

class Vista:

    def __init__(self, ventana):

        self.ventana = ventana

        ventana.geometry("1000x800")
        ventana.title("PERCEPTRON - ANALISTA DE FÚTBOL")
        ventana.configure(bg="#f0f0f0")  # Fondo gris claro

        fuenteTitulos = ("Helvetica", 12, "bold")
        fuenteLabels = ("Helvetica", 10)
        estilo = ttk.Style()
        estilo.configure('EstiloBoton.TButton', borderwidth=2, relief="raised", font=("Helvetica", 10, "bold"), background="#4CAF50", foreground="white")
        estilo.map('EstiloBoton.TButton', background=[('active', '#45a049')])

        # Frame principal
        main_frame = tkinter.Frame(ventana, bg="#f0f0f0")
        main_frame.pack(fill="both", expand=True, padx=10, pady=10)

        # Frame de título
        title_frame = tkinter.Frame(main_frame, bg="#f0f0f0")
        title_frame.pack(fill="x", pady=(0, 10))
        self.lblTituloPrincipal = tkinter.Label(title_frame, text="HAGA CLICK EN 'Entrenamiento' PARA COMENZAR", font=fuenteTitulos, bg="#f0f0f0", fg="#333")
        self.lblTituloPrincipal.pack()

        # Frame de entrenamiento
        train_frame = tkinter.LabelFrame(main_frame, text="Entrenamiento", font=fuenteLabels, bg="#ffffff", padx=10, pady=10)
        train_frame.pack(fill="x", pady=(0, 10))

        self.lblEntrada1 = tkinter.Label(train_frame, text="Goles a favor:", font=fuenteLabels, bg="#ffffff")
        self.lblEntrada2 = tkinter.Label(train_frame, text="Goles en contra:", font=fuenteLabels, bg="#ffffff")
        self.lblEntrada3 = tkinter.Label(train_frame, text="Ganados visitante:", font=fuenteLabels, bg="#ffffff")
        lblEntrada0 = tkinter.Label(train_frame, text="Entrada 0: 1", font=fuenteLabels, bg="#ffffff")
        self.lblPeso1 = tkinter.Label(train_frame, text="Campeón:", font=fuenteLabels, bg="#ffffff")
        self.lblPeso2 = tkinter.Label(train_frame, text="Media Tabla:", font=fuenteLabels, bg="#ffffff")
        self.lblUmbral = tkinter.Label(train_frame, text="Descenso:", font=fuenteLabels, bg="#ffffff")
        self.lblSalidaDeseada = tkinter.Label(train_frame, text="Salida Deseada:", font=fuenteLabels, bg="#ffffff")
        self.lblSalidaObtenida = tkinter.Label(train_frame, text="Salida Obtenida:", font=fuenteLabels, bg="#ffffff")
        self.lblFactorAprendizaje = tkinter.Label(train_frame, text="Factor Aprendizaje: 0.01", font=fuenteLabels, bg="#ffffff")
        self.lblEpoca = tkinter.Label(train_frame, text="Época: 0", font=fuenteLabels, bg="#ffffff")
        self.lblErrores = tkinter.Label(train_frame, text="Errores: 0", font=fuenteLabels, bg="#ffffff")

        self.btnEntrenamiento = ttk.Button(train_frame, text="Entrenamiento", style='EstiloBoton.TButton')

        # Grid para entrenamiento
        self.lblEntrada1.grid(row=0, column=1, padx=5, pady=5, sticky="w")
        self.lblEntrada2.grid(row=0, column=2, padx=5, pady=5, sticky="w")
        self.lblEntrada3.grid(row=0, column=3, padx=5, pady=5, sticky="w")
        lblEntrada0.grid(row=0, column=4, padx=5, pady=5, sticky="w")
        self.lblPeso1.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        self.lblPeso2.grid(row=1, column=2, padx=5, pady=5, sticky="w")
        self.lblUmbral.grid(row=1, column=3, padx=5, pady=5, sticky="w")
        self.lblSalidaDeseada.grid(row=2, column=1, padx=5, pady=5, sticky="w")
        self.lblSalidaObtenida.grid(row=2, column=2, padx=5, pady=5, sticky="w")
        self.lblFactorAprendizaje.grid(row=2, column=3, padx=5, pady=5, sticky="w")
        self.lblEpoca.grid(row=3, column=1, padx=5, pady=5, sticky="w")
        self.lblErrores.grid(row=3, column=2, padx=5, pady=5, sticky="w")
        self.btnEntrenamiento.grid(row=0, column=0, rowspan=4, padx=10, pady=5, sticky="ns")

        # Frame de aprendizaje
        learn_frame = tkinter.LabelFrame(main_frame, text="Aprendizaje", font=fuenteLabels, bg="#ffffff", padx=10, pady=10)
        learn_frame.pack(fill="x", pady=(0, 10))

        self.btnAprendizaje = ttk.Button(learn_frame, text="Aprendizaje", style='EstiloBoton.TButton')
        self.btnAprendizaje.grid(row=0, column=0, padx=10, pady=5)

        # Frame de prueba
        test_frame = tkinter.LabelFrame(main_frame, text="Prueba del Perceptrón", font=fuenteLabels, bg="#ffffff", padx=10, pady=10)
        test_frame.pack(fill="x", pady=(0, 10))

        lblTituloPrueba = tkinter.Label(test_frame, text="EJERCICIO PARA PROBAR EL PERCEPTRON:", font=fuenteTitulos, bg="#ffffff")
        self.lblPruebaEntrada1 = tkinter.Label(test_frame, text="Goles a favor:", font=fuenteLabels, bg="#ffffff")
        self.lblPruebaEntrada2 = tkinter.Label(test_frame, text="Goles en contra:", font=fuenteLabels, bg="#ffffff")
        self.lblPruebaEntrada3 = tkinter.Label(test_frame, text="Ganados visitante:", font=fuenteLabels, bg="#ffffff")
        self.lblPruebaSalidaObtenida = tkinter.Label(test_frame, text="Salida Obtenida:", font=fuenteLabels, bg="#ffffff")

        self.btnPrueba = ttk.Button(test_frame, text="Prueba", style='EstiloBoton.TButton')
        self.jtfEntrada1 = tkinter.Entry(test_frame, font=fuenteLabels)
        self.jtfEntrada2 = tkinter.Entry(test_frame, font=fuenteLabels)
        self.jtfEntrada3 = tkinter.Entry(test_frame, font=fuenteLabels)

        lblTituloPrueba.grid(row=0, column=1, columnspan=3, pady=10)
        self.lblPruebaEntrada1.grid(row=1, column=1, padx=5, pady=5, sticky="w")
        self.lblPruebaEntrada2.grid(row=1, column=2, padx=5, pady=5, sticky="w")
        self.lblPruebaEntrada3.grid(row=1, column=3, padx=5, pady=5, sticky="w")
        self.lblPruebaSalidaObtenida.grid(row=2, column=4, padx=5, pady=5, sticky="w")
        self.btnPrueba.grid(row=1, column=0, rowspan=2, padx=10, pady=5, sticky="ns")
        self.jtfEntrada1.grid(row=2, column=1, padx=5, pady=5)
        self.jtfEntrada2.grid(row=2, column=2, padx=5, pady=5)
        self.jtfEntrada3.grid(row=2, column=3, padx=5, pady=5)

        # Frame para gráfico (dejamos espacio para que Grafico.py lo coloque)
        self.graph_frame = tkinter.LabelFrame(main_frame, text="Gráfico", font=fuenteLabels, bg="#ffffff", padx=10, pady=10)
        self.graph_frame.pack(fill="both", expand=True)