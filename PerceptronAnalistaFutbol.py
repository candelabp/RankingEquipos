class PerceptronAnalistaFutbol:

    def __init__(self):
        self.factor_aprendizaje = 0.01

        # Entradas:
        # [sesgo, goles a favor, goles en contra, ganados visitante]
        self.entradas = [
            [1.0, 80.0, 25.0, 10.0],  # Campeón
            [1.0, 70.0, 30.0, 8.0],   # Campeón
            [1.0, 55.0, 45.0, 5.0],   # Media tabla
            [1.0, 45.0, 50.0, 4.0],   # Media tabla
            [1.0, 30.0, 70.0, 1.0],   # Descenso
            [1.0, 25.0, 75.0, 0.0]    # Descenso
        ]

        # Salidas deseadas:
        # [Campeón, Media Tabla, Descenso]
        self.salidas = [
            [1.0, -1.0, -1.0],
            [1.0, -1.0, -1.0],
            [-1.0, 1.0, -1.0],
            [-1.0, 1.0, -1.0],
            [-1.0, -1.0, 1.0],
            [-1.0, -1.0, 1.0]
        ]

        # Pesos iniciales de cada neurona:
        # [w0, w1, w2, w3]
        self.pesos_campeon = [-30.0, 0.8, -0.6, 1.5]
        self.pesos_media = [-5.0, 0.3, -0.2, 0.5]
        self.pesos_descenso = [-10.0, -0.4, 0.7, -1.0]

        self.pesos = [
            self.pesos_campeon,
            self.pesos_media,
            self.pesos_descenso
        ]

        self.nombres_neuronas = ["Campeón", "Media Tabla", "Descenso"]

        self.fila = 0
        self.repeticion = 1
        self.bandera = True
        self.error = 0.0
        self.y = [0.0, 0.0, 0.0]

    def Activacion(self, valor):
        if valor > 0:
            return 1.0
        else:
            return -1.0

    def CalcularSalidaNeurona(self, pesos, entrada):
        suma = 0.0

        for i in range(len(pesos)):
            suma += pesos[i] * entrada[i]

        return self.Activacion(suma), suma

    def Entrenamiento(self):
        if self.bandera == True:
            print("PERCEPTRON ANALISTA DE FÚTBOL")
            print(f"Factor de Aprendizaje: {self.factor_aprendizaje}")
            print(f"ITERACIÓN: {self.repeticion}")
            print("-----------------------------------------------------------")

            while self.fila < len(self.entradas):
                entrada_actual = self.entradas[self.fila]
                salida_deseada = self.salidas[self.fila]

                print(f"Equipo de entrenamiento #{self.fila + 1}")
                print(f"Goles a favor: {entrada_actual[1]}")
                print(f"Goles en contra: {entrada_actual[2]}")
                print(f"Ganados visitante: {entrada_actual[3]}")

                self.error = 0.0

                for indice_neurona in range(3):
                    pesos_neurona = self.pesos[indice_neurona]
                    salida_obtenida, suma = self.CalcularSalidaNeurona(pesos_neurona, entrada_actual)

                    self.y[indice_neurona] = salida_obtenida

                    error_neurona = salida_deseada[indice_neurona] - salida_obtenida
                    self.error += abs(error_neurona)

                    print(f"Neurona {self.nombres_neuronas[indice_neurona]}")
                    print(f"Suma: {suma}")
                    print(f"Salida obtenida: {salida_obtenida}")
                    print(f"Salida deseada: {salida_deseada[indice_neurona]}")
                    print(f"Error: {error_neurona}")

                    if error_neurona != 0.0:
                        for i in range(len(pesos_neurona)):
                            pesos_neurona[i] = pesos_neurona[i] + (
                                self.factor_aprendizaje * error_neurona * entrada_actual[i]
                            )

                print("-----------------------------------------------------------")

                if self.error == 0.0:
                    self.fila += 1
                else:
                    self.fila = 0
                    self.repeticion += 1
                    break

            if self.fila == len(self.entradas):
                print("ENTRENAMIENTO COMPLETADO")
                print("Pesos finales:")

                for i in range(3):
                    print(f"{self.nombres_neuronas[i]}: {self.pesos[i]}")

                self.bandera = False

    def Aprendizaje(self):
        # En este modelo el ajuste de pesos se hace dentro de Entrenamiento()
        print("El aprendizaje del Analista de Fútbol se realiza durante el entrenamiento.")

    def PruebaFuncionamiento(self, goles_favor, goles_contra, ganados_visitante):
        entrada = [1.0, float(goles_favor), float(goles_contra), float(ganados_visitante)]

        resultado = []
        sumas = []

        for pesos_neurona in self.pesos:
            salida, suma = self.CalcularSalidaNeurona(pesos_neurona, entrada)
            resultado.append(salida)
            sumas.append(round(suma, 4))

        categoria = self.InterpretarResultado(resultado)

        return resultado, sumas, categoria

    def InterpretarResultado(self, resultado):
        if resultado == [1.0, -1.0, -1.0]:
            return "Campeón / Puestos 1-4"

        if resultado == [-1.0, 1.0, -1.0]:
            return "Media Tabla / Puestos 5-15"

        if resultado == [-1.0, -1.0, 1.0]:
            return "Descenso / Puestos 16-20"

        # Si más de una neurona se activa, se elige la de mayor prioridad lógica.
        if resultado[0] == 1.0:
            return "Campeón / Puestos 1-4"

        if resultado[1] == 1.0:
            return "Media Tabla / Puestos 5-15"

        if resultado[2] == 1.0:
            return "Descenso / Puestos 16-20"

        return "Sin clasificación clara"

    def getEntradas(self, X):
        if self.fila >= len(self.entradas):
            return self.entradas[-1][X]
        else:
            return self.entradas[self.fila][X]

    def getSalidas(self, X):
        if self.fila >= len(self.salidas):
            return self.salidas[-1]
        else:
            return self.salidas[self.fila]