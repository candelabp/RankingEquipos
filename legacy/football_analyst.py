import numpy as np
import os

class FutbolAnalystLayer:
    def __init__(self, datos_liga):
        """
        datos_liga: Matriz donde cada fila es un equipo [W_goles_favor, W_goles_contra, W_visitante]
        """
        # 1. Pesos (Personalidad de  Neuronas)
        self.weights = np.array([
            [1.5, -2.0, 1.0],  # Neurona Campeón (Valora ataque, castiga defensa floja)
            [0.5, -0.5, 0.2],  # Neurona Media Tabla (Busca balance moderado)
            [-1.2, 2.5, -0.8]  # Neurona Descenso (Se activa con crisis defensiva)
        ])
        
        # 2. Entrenamiento: Cálculo de promedios y sesgos automáticos
        # El bias se define para que el "punto de equilibrio" sea el promedio de la liga
        self.promedios_liga = np.mean(datos_liga, axis=0)
        self.biases = -np.dot(self.weights, self.promedios_liga)

    def predict(self, x):
        """
        x: [W_goles_favor, W_goles_contra, W_visitante]
        """
        # Suma ponderada: z = (W * x) + b
        z = np.dot(self.weights, x) + self.biases
        
        # Función de Activación (Escalón): 1 si supera el promedio, -1 si no
        output = np.where(z > 0, 1, -1)
        
        return output, z

def mostrar_resultado(equipo_stats, resultado, valores_z):
    etiquetas = ["CAMPEÓN", "MEDIA TABLA", "DESCENSO"]
    print("\n" + "="*45)
    print(f" ANÁLISIS DE EQUIPO: {equipo_stats}")
    print("="*45)
    for i in range(len(etiquetas)):
        voto = "SÍ [1]" if resultado[i] == 1 else "NO [-1]"
        print(f"Analista {etiquetas[i]:<15}: {voto} (Fuerza: {valores_z[i]:.2f})")
    print("="*45)

def ejecutar_programa():
    # Base de datos inicial (Liga Ejemplo)
    # [Goles Favor, Goles Contra, Ganados Visitante]
    liga_ejemplo = np.array([
        [50, 20, 8],  # Equipo A (Top)
        [30, 35, 3],  # Equipo B
        [25, 40, 2],  # Equipo C
        [40, 30, 5],  # Equipo D
        [15, 60, 1]   # Equipo E (Fondo)
    ])
    nombres_ejemplo = ["Boca", "Belgrano", "Racing", "Independiente", "RiBer"]
    
    modelo = None

    while True:
        print("\n" + " " * 10 + "--- MENÚ ANALISTA DE FÚTBOL ---")
        print("1. Entrenar Modelo (Cargar promedios de la Liga)")
        print("2. Test: Analizar equipo manual (Ingresar estadísticas)")
        print("3. Analizar Liga Completa (Equipos Hardcoded)")
        print("4. Salir")
        
        opcion = input("\nSeleccione una opción (1-4): ")

        if opcion == "1":
            modelo = FutbolAnalystLayer(liga_ejemplo)
            print("\n" + "-"*50)
            print("[OK] Modelo entrenado correctamente.")
            print(f"Promedios de la Liga -> GF: {modelo.promedios_liga[0]}, GC: {modelo.promedios_liga[1]}, GV: {modelo.promedios_liga[2]}")
            print(f"Sesgos calculados    -> {modelo.biases}")
            print("-"*50)
        
        elif opcion == "2":
            if modelo is None:
                print("\n[!] Error: Primero debe entrenar el modelo (Opción 1).")
                continue
            
            try:
                print("\nIngrese las estadísticas del equipo:")
                gf = float(input(" -> Goles a Favor: "))
                gc = float(input(" -> Goles en Contra: "))
                gv = float(input(" -> Ganados Visitante: "))
                
                equipo = np.array([gf, gc, gv])
                res, z = modelo.predict(equipo)
                mostrar_resultado(equipo, res, z)
            except ValueError:
                print("\n[!] Error: Por favor ingrese solo números.")

        elif opcion == "3":
            if modelo is None:
                print("\n[!] Error: Primero debe entrenar el modelo (Opción 1).")
                continue
            
            print("\nProcesando todos los equipos de la base de datos...")
            for i in range(len(liga_ejemplo)):
                print(f"\nAnalizando: {nombres_ejemplo[i]}")
                res, z = modelo.predict(liga_ejemplo[i])
                mostrar_resultado(liga_ejemplo[i], res, z)
        
        elif opcion == "4":
            print("\nCerrando el sistema de analistas... ¡Hasta pronto!")
            break
        else:
            print("\n[!] Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    ejecutar_programa()
