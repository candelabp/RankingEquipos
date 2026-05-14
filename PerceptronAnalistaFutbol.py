import numpy as np


class PerceptronAnalistaFutbol:
    def __init__(self, factor_aprendizaje=0.001):  # FIX 1: factor reducido de 0.01 a 0.001
        self.factor_aprendizaje = factor_aprendizaje

        # FIX 2: Datos NORMALIZADOS (todos en escala 0.0 a 1.0)
        # Escala usada: GF y GC divididos por 100, GV dividido por 10
        # [Sesgo, Goles+ /100, Goles- /100, Ganados Visitante /10]
        self.entradas = np.array([
            [1.0, 0.80, 0.25, 1.0],  # Campeón
            [1.0, 0.70, 0.30, 0.8],  # Campeón
            [1.0, 0.55, 0.45, 0.5],  # Media tabla
            [1.0, 0.45, 0.50, 0.4],  # Media tabla
            [1.0, 0.30, 0.70, 0.1],  # Descenso
            [1.0, 0.25, 0.75, 0.0]   # Descenso
        ])

        # Salidas deseadas (One-Hot Encoding con 1 y -1)
        self.salidas_deseadas = np.array([
            [1.0, -1.0, -1.0], [1.0, -1.0, -1.0],   # Campeón
            [-1.0, 1.0, -1.0], [-1.0, 1.0, -1.0],   # Media
            [-1.0, -1.0, 1.0], [-1.0, -1.0, 1.0]    # Descenso
        ])

        # Matriz de pesos inicializada aleatoriamente (3 neuronas x 4 entradas)
        self.pesos = np.random.uniform(-0.5, 0.5, (3, 4))

        self.nombres_neuronas = ["Campeón", "Media Tabla", "Descenso"]
        self.iteracion = 0
        self.bandera = True
        self.training_complete = False
        self.fila = 0
        self.y = np.array([-1.0, -1.0, -1.0])
        self.errors_history = []
        self.epoch_count = 0

    def activacion(self, valor):
        return 1.0 if valor > 0 else -1.0

    def predecir(self, entrada):
        """Calcula la salida de las 3 neuronas simultáneamente."""
        sumas = np.dot(self.pesos, entrada)
        predicciones = [self.activacion(s) for s in sumas]
        return np.array(predicciones), sumas

    def _normalizar_entrada(self, gf, gc, gv):
        """
        FIX 2: Normaliza los valores ingresados por el usuario
        para que coincidan con la escala de los datos de entrenamiento.
        GF y GC se dividen por 100, GV se divide por 10.
        """
        return np.array([1.0, float(gf) / 100.0, float(gc) / 100.0, float(gv) / 10.0])

    def entrenamiento_completo(self, max_epocas=5000):  # FIX 3: más épocas (1000 -> 5000)
        self.errors_history = []
        self.training_complete = False
        print(f"Iniciando entrenamiento - Factor: {self.factor_aprendizaje} | Máx. épocas: {max_epocas}")

        for epoca in range(1, max_epocas + 1):
            errores_totales = 0

            for entrada_actual, deseado in zip(self.entradas, self.salidas_deseadas):
                prediccion, _ = self.predecir(entrada_actual)
                error_vector = deseado - prediccion

                if np.any(error_vector != 0):
                    errores_totales += 1
                    for n in range(3):
                        if error_vector[n] != 0:
                            self.pesos[n] += self.factor_aprendizaje * error_vector[n] * entrada_actual

            self.errors_history.append(errores_totales)
            self.epoch_count = epoca

            if errores_totales == 0:
                self.training_complete = True
                print(f"✓ Entrenamiento completado en la época {epoca}")
                break

        if not self.training_complete:
            print(f"⚠ Se alcanzó el máximo de épocas ({max_epocas}) con {self.errors_history[-1]} errores.")

        self.iteracion = self.epoch_count
        self.bandera = not self.training_complete
        self.y, _ = self.predecir(self.entradas[-1])
        return self.errors_history

    def clasificar_equipo(self, gf, gc, gv):
        # FIX 2: Se normaliza la entrada antes de predecir
        entrada = self._normalizar_entrada(gf, gc, gv)
        prediccion, sumas = self.predecir(entrada)

        if np.sum(prediccion == 1.0) > 1:
            indice_ganador = np.argmax(sumas)
        elif 1.0 in prediccion:
            indice_ganador = np.where(prediccion == 1.0)[0][0]
        else:
            return prediccion, sumas, "Sin clasificación clara"

        categoria = f"{self.nombres_neuronas[indice_ganador]} (Confianza: {round(sumas[indice_ganador], 2)})"
        return prediccion, sumas, categoria

    def getEntradas(self, index):
        if self.fila < len(self.entradas):
            return self.entradas[self.fila][index]
        return self.entradas[-1][index]

    def getSalidas(self, fila):
        if fila < len(self.salidas_deseadas):
            return self.salidas_deseadas[fila]
        return self.salidas_deseadas[-1]

    def entrenamiento_epoca(self):
        errores_totales = 0

        for entrada_actual, deseado in zip(self.entradas, self.salidas_deseadas):
            prediccion, _ = self.predecir(entrada_actual)
            error_vector = deseado - prediccion

            if np.any(error_vector != 0):
                errores_totales += 1
                for n in range(3):
                    if error_vector[n] != 0:
                        self.pesos[n] += self.factor_aprendizaje * error_vector[n] * entrada_actual

        self.errors_history.append(errores_totales)
        self.epoch_count += 1
        self.bandera = errores_totales != 0
        self.training_complete = errores_totales == 0
        self.y, _ = self.predecir(self.entradas[-1])

        return errores_totales

    def Entrenamiento(self):
        self.errors_history = []
        self.epoch_count = 0
        self.training_complete = False
        return self.entrenamiento_completo()

    def Aprendizaje(self):
        if self.training_complete:
            return 0
        return self.entrenamiento_epoca()

    def PruebaFuncionamiento(self, gf, gc, gv):
        return self.clasificar_equipo(gf, gc, gv)


# --- PRUEBA RÁPIDA ---
if __name__ == "__main__":
    modelo = PerceptronAnalistaFutbol()
    modelo.Entrenamiento()

    casos = [
        (75, 28, 9,  "Campeón esperado"),
        (50, 48, 4,  "Media Tabla esperado"),
        (28, 72, 1,  "Descenso esperado"),
        (60, 44, 5,  "Límite (Campeón/Media)"),
        (80, 70, 0,  "Contradicción"),
    ]

    print("\n--- RESULTADOS DE PRUEBA ---")
    for gf, gc, gv, descripcion in casos:
        _, _, categoria = modelo.PruebaFuncionamiento(gf, gc, gv)
        print(f"{descripcion:<30} → {categoria}")