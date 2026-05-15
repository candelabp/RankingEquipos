# Perceptrón Analista de Fútbol

## Introducción

Este proyecto consiste en un sistema de Inteligencia Artificial basado en una red neuronal simple (arquitectura de Perceptrón) diseñado para clasificar equipos de fútbol en diferentes categorías según sus estadísticas de rendimiento. Utilizando datos clave como goles a favor, goles en contra y partidos ganados de visitante, el modelo matemático "aprende" a identificar qué características definen a un equipo para ser considerado "Campeón", un equipo de "Media Tabla", o un equipo en riesgo de "Descenso".

**Diseñado y desarrollado por:** Candela Puerta y Juan Cruz Berrios.

---

## ¿Cómo funciona el Perceptrón?

### 1. La Estructura de Datos (Entradas y Salidas)
El modelo no entiende de "fútbol", entiende de números. Por eso los datos están organizados en matrices de NumPy:
* **Entradas (`self.entradas`)**: Cada fila es un equipo con 4 valores: `[Sesgo (1.0), Goles+, Goles-, Ganados Visitante]`. El Sesgo (Bias) es un valor constante que ayuda a la neurona a ajustarse mejor.
* **Salidas Deseadas (`self.salidas_deseadas`)**: Es lo que el modelo debería responder. Usamos un formato llamado *One-Hot*:
  * `[1, -1, -1]` -> Campeón.
  * `[-1, 1, -1]` -> Media Tabla.
  * `[-1, -1, 1]` -> Descenso.

### 2. Los Pesos (`self.pesos`)
Es una matriz de $3 \times 4$ (3 neuronas, una para cada categoría, y 4 entradas).
* Al inicio son valores aleatorios (`np.random.uniform`).
* Durante el entrenamiento, estos números cambian. Si una neurona debe activarse con muchos goles, su peso para "Goles+" aumentará.

### 3. El Corazón Matemático: Predicción
Para saber qué piensa el modelo sobre un equipo, usa dos pasos:

```python
def predecir(self, entrada):
    # Suma ponderada: z = (W1*X1 + W2*X2 + ...)
    sumas = np.dot(self.pesos, entrada) 

    # Función de activación (Escalón)
    predicciones = [1.0 if s > 0 else -1.0 for s in sumas]

    return np.array(predicciones), sumas
```
* **`np.dot` (Producto Punto)**: Multiplica cada estadística por su peso correspondiente y las suma.
* **Activación**: Si la suma es mayor a 0, la neurona dice "SÍ" (1.0); si no, dice "NO" (-1.0).

### 4. El Aprendizaje (Regla del Perceptrón)
Aquí es donde ocurre la "magia". El modelo revisa sus errores y se corrige:

```python
error_vector = deseado - prediccion
if np.any(error_vector != 0):
    for n in range(3): # Para cada una de las 3 neuronas
        self.pesos[n] += self.factor_aprendizaje * error_vector[n] * entrada_actual
```
La fórmula que usa es: $\Delta W = \eta \cdot (Deseado - Obtenido) \cdot Entrada$
* Si el modelo dijo "No" (-1) pero era "Sí" (1), el error es positivo y los pesos **suben**.
* Si el modelo dijo "Sí" (1) pero era "No" (-1), el error es negativo y los pesos **bajan**.
* El **Factor de Aprendizaje** ($\eta$) controla qué tan brusco es este cambio.

### 5. Clasificación Final
Como tenemos 3 neuronas, a veces más de una puede decir "SÍ" al mismo tiempo. Para desempatar, el código usa la fuerza de la señal:

```python
if np.sum(prediccion == 1.0) > 1:
    indice_ganador = np.argmax(sumas) # El que tenga la suma más alta gana
```
El equipo se asigna a la categoría cuya neurona haya tenido la suma ponderada más alta (la respuesta más "segura").

---

## Resumen del proceso:
1. **Entrada**: Recibe datos de un equipo (ej: Boca).
2. **Normalización**: Divide los goles por 100 para que los números sean pequeños y fáciles de procesar.
3. **Suma Ponderada**: Multiplica por los pesos.
4. **Activación**: Genera un vector de 1 y -1.
5. **Decisión**: Te dice "Es un equipo de Media Tabla".
