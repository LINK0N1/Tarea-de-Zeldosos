import json
import os
import tkinter as tk
from tkinter import messagebox

# ==========================================
# 1. MODELO Y LÓGICA DE NEGOCIO (QUIZ ENGINE)
# ==========================================

class Question:
    """Representa una pregunta individual dentro del Quiz."""
    def __init__(self, pregunta, opciones, respuesta_correcta, puntos_base=100):
        self.pregunta = pregunta
        self.opciones = opciones
        self.respuesta_correcta = respuesta_correcta
        self.puntos_base = puntos_base

class QuizEngine:
    """Maneja la lógica del estado del juego, puntuación y temporizador."""
    def __init__(self, filepath_json):
        self.filepath_json = filepath_json
        self.preguntas = []
        self.indice_actual = 0
        self.score_total = 0
        self.respuestas_correctas = 0
        self.tiempo_limite = 15  # Límite en segundos por pregunta (Bonus B1)
        self.tiempo_restante = self.tiempo_limite
        
        self.cargar_preguntas()

    def cargar_preguntas(self):
        """Carga el banco de preguntas desde un archivo JSON (Bonus B3)."""
        if not os.path.exists(self.filepath_json):
            raise FileNotFoundError(f"No se encontró el archivo {self.filepath_json}")
            
        with open(self.filepath_json, 'r', encoding='utf-8') as file:
            data = json.load(file)
            self.preguntas = [
                Question(q['pregunta'], q['opciones'], q['respuesta_correcta'], q.get('puntos_base', 100))
                for q in data
            ]

    def obtener_pregunta_actual(self):
        if self.indice_actual < len(self.preguntas):
            return self.preguntas[self.indice_actual]
        return None

    def validar_respuesta(self, opcion_seleccionada):
        """Valida la respuesta y calcula el puntaje dinámico en base al tiempo restante (Bonus B2)."""
        pregunta = self.obtener_pregunta_actual()
        if not pregunta:
            return False, 0

        es_correcta = (opcion_seleccionada == pregunta.respuesta_correcta)
        puntos_obtenidos = 0

        if es_correcta:
            self.respuestas_correctas += 1
            # Bonus B2: Bonus de velocidad (Puntos base + [tiempo restante * 10])
            puntos_obtenidos = pregunta.puntos_base + (self.tiempo_restante * 10)
            self.score_total += puntos_obtenidos

        return es_correcta, puntos_obtenidos

    def siguiente_pregunta(self):
        self.indice_actual += 1
        self.tiempo_restante = self.tiempo_limite

    def ha_finalizado(self):
        return self.indice_actual >= len(self.preguntas)

    def reiniciar(self):
        self.indice_actual = 0
        self.score_total = 0
        self.respuestas_correctas = 0
        self.tiempo_restante = self.tiempo_limite


# ==========================================
# 2. INTERFAZ GRÁFICA (TKINTER GUI)
# ==========================================

class QuizGUI:
    """Clase encargada exclusivamente de la capa de presentación visual."""
    def __init__(self, root, engine):
        self.root = root
        self.engine = engine
        self.timer_job = None
        
        self.root.title("Quiz App - Python Edition")
        self.root.geometry("500x450")
        self.root.resizable(False, False)
        
        self.opcion_seleccionada = tk.StringVar()
        self.crear_widgets()
        self.mostrar_pregunta()

    def crear_widgets(self):
        # Panel Superior: Puntaje y Temporizador (CORREGIDO: padx/pady en lugar de padding)
        self.frame_header = tk.Frame(self.root, bg="#eceff1", padx=10, pady=10)
        self.frame_header.pack(fill="x")

        self.lbl_score = tk.Label(self.frame_header, text="Puntos: 0", font=("Helvetica", 11, "bold"), bg="#eceff1")
        self.lbl_score.pack(side="left")

        self.lbl_timer = tk.Label(self.frame_header, text="Tiempo: 15s", font=("Helvetica", 11, "bold"), fg="#d32f2f", bg="#eceff1")
        self.lbl_timer.pack(side="right")

        # Cuerpo: Pregunta y Opciones (US1)
        self.frame_body = tk.Frame(self.root, padx=20, pady=20)
        self.frame_body.pack(fill="both", expand=True)

        self.lbl_pregunta = tk.Label(self.frame_body, text="", font=("Helvetica", 13, "bold"), wraplength=440, justify="left")
        self.lbl_pregunta.pack(anchor="w", pady=(0, 15))

        self.rb_opciones = []
        for i in range(4):
            rb = tk.Radiobutton(
                self.frame_body, text="", variable=self.opcion_seleccionada,
                value="", font=("Helvetica", 11), anchor="w", justify="left"
            )
            rb.pack(fill="x", pady=4)
            self.rb_opciones.append(rb)

        # Panel Inferior: Retroalimentación y Botón de Enviar (US2, US3)
        self.lbl_feedback = tk.Label(self.frame_body, text="", font=("Helvetica", 10, "italic"))
        self.lbl_feedback.pack(pady=10)

        self.btn_enviar = tk.Button(
            self.root, text="Confirmar Respuesta", font=("Helvetica", 11, "bold"),
            bg="#1976d2", fg="white", activebackground="#1565c0", activeforeground="white",
            command=self.procesar_respuesta
        )
        self.btn_enviar.pack(pady=(0, 20), ipadx=10, ipady=5)

    def mostrar_pregunta(self):
        """Carga la pregunta actual e inicia la cuenta regresiva."""
        pregunta = self.engine.obtener_pregunta_actual()
        if not pregunta:
            self.finalizar_juego()
            return

        self.opcion_seleccionada.set("")  # Limpiar selección previa
        self.lbl_feedback.config(text="")
        self.lbl_pregunta.config(text=f"P{self.engine.indice_actual + 1}. {pregunta.pregunta}")

        for i, opcion in enumerate(pregunta.opciones):
            self.rb_opciones[i].config(text=opcion, value=opcion, state="normal")

        self.btn_enviar.config(state="normal", text="Confirmar Respuesta", command=self.procesar_respuesta)
        self.actualizar_temporizador()

    def actualizar_temporizador(self):
        """Maneja el temporizador de 15 segundos (Bonus B1)."""
        self.lbl_timer.config(text=f"Tiempo: {self.engine.tiempo_restante}s")
        
        if self.engine.tiempo_restante > 0:
            self.engine.tiempo_restante -= 1
            self.timer_job = self.root.after(1000, self.actualizar_temporizador)
        else:
            self.lbl_feedback.config(text="¡Tiempo agotado!", fg="#d32f2f")
            self.deshabilitar_opciones()
            self.btn_enviar.config(text="Siguiente Pregunta", command=self.avanzar_pregunta, state="normal")

    def detener_temporizador(self):
        if self.timer_job:
            self.root.after_cancel(self.timer_job)
            self.timer_job = None

    def deshabilitar_opciones(self):
        for rb in self.rb_opciones:
            rb.config(state="disabled")

    def procesar_respuesta(self):
        """Valida la respuesta del usuario (US2, US3) y calcula puntaje dinámico (B2)."""
        opcion = self.opcion_seleccionada.get()
        if not opcion:
            messagebox.showwarning("Atención", "Por favor, selecciona una opción antes de enviar.")
            return

        self.detener_temporizador()
        self.deshabilitar_opciones()

        es_correcta, puntos = self.engine.validar_respuesta(opcion)

        if es_correcta:
            self.lbl_feedback.config(text=f"¡Correcto! +{puntos} pts (Bonus velocidad)", fg="#388e3c")
        else:
            correcta = self.engine.obtener_pregunta_actual().respuesta_correcta
            self.lbl_feedback.config(text=f"Incorrecto. La respuesta era: {correcta}", fg="#d32f2f")

        self.lbl_score.config(text=f"Puntos: {self.engine.score_total}")
        self.btn_enviar.config(text="Siguiente Pregunta", command=self.avanzar_pregunta)

    def avanzar_pregunta(self):
        """Avanza a la siguiente pregunta o finaliza (US4)."""
        self.detener_temporizador()
        self.engine.siguiente_pregunta()
        
        if self.engine.ha_finalizado():
            self.finalizar_juego()
        else:
            self.mostrar_pregunta()

    def finalizar_juego(self):
        """Muestra los resultados finales y permite reiniciar el Quiz (US5)."""
        self.detener_temporizador()
        total_preguntas = len(self.engine.preguntas)
        correctas = self.engine.respuestas_correctas
        puntos = self.engine.score_total

        mensaje = (
            f"¡Has completado el Quiz!\n\n"
            f"Respuestas correctas: {correctas} de {total_preguntas}\n"
            f"Puntuación final acumulada: {puntos} pts\n\n"
            f"¿Deseas reiniciar la partida?"
        )

        respuesta = messagebox.askyesno("Fin del Juego", mensaje)
        if respuesta:
            self.engine.reiniciar()
            self.lbl_score.config(text="Puntos: 0")
            self.mostrar_pregunta()
        else:
            self.root.destroy()


# ==========================================
# 3. PUNTO DE ENTRADA (MAIN)
# ==========================================

if __name__ == "__main__":
    try:
        engine = QuizEngine("questions.json")
        root = tk.Tk()
        app = QuizGUI(root, engine)
        root.mainloop()
    except Exception as e:
        print(f"Error al iniciar la aplicación: {e}")
        