# Quiz App - Juego de Preguntas y Respuestas en Python

## Integrantes del Equipo

* **Amaury Ali Tristán Córdova** - [@LINK0N1] https://github.com/LINK0N1
* **Andrea Dalith Zavala Barbosa** - [@AndreaZ75] https://github.com/AndreaZ75
* **Leonardo Rodríguez Flores** - [@RodriguezFloresLeonardo] https://github.com/RodriguezFloresLeonardo

---
## Descripción y Justificación del Proyecto 

### Descripción
**Quiz App** es una aplicación de consola desarrollada en Python que permite a los usuarios poner a prueba sus conocimientos a través de un juego de preguntas de opción múltiple. El sistema presenta preguntas secuenciales, brinda retroalimentación inmediata sobre la precisión de las respuestas, incluye un temporizador por pregunta y calcula un puntaje final acumulado al terminar la sesión.

### Justificación Formal
El proyecto se seleccionó del banco comunitario *App Ideas* de Florin Pop (Tier 1 / Beginner) para resolver la necesidad de contar con una herramienta educativa interactiva, liviana y accesible desde la terminal que permita evaluar conocimientos de forma rápida y lúdica. Esta elección representa un alcance técnicamente adecuado para el equipo dentro del marco temporal de la Práctica 1, ya que nos permite aplicar y validar de punta a punta las 5 fases del ciclo de vida del software (Comunicación, Planeación, Modelado, Construcción y Cierre) sin sobrepasar el tiempo disponible de desarrollo.

----

## Historias de Usuario

Basadas en los requisitos del repositorio *App Ideas* y adaptadas para la Guía de Práctica del curso:

* **US1 (Base):** *Como usuario*, quiero ver una pregunta a la vez con sus opciones correspondientes *para* poder concentrarme en responder de manera individual.
* **US2 (Base):** *Como usuario*, quiero seleccionar una opción mediante el teclado y recibir retroalimentación inmediata (correcto/incorrecto) *para* saber si respondí acertadamente.
* **US3 (Base):** *Como usuario*, quiero que el sistema avance automáticamente a la siguiente pregunta tras responder *para* tener una experiencia de juego fluida.
* **US4 (Base):** *Como usuario*, quiero ver mi puntaje total al finalizar la sesión *para* evaluar mi desempeño general.
* **US5 (Base):** *Como usuario*, quiero poder reiniciar la partida o salir del programa al terminar *para* volver a jugar si lo deseo.
* **US6 (Bonus - Temporizador):** *Como usuario*, quiero contar con un temporizador por pregunta *para* añadir un nivel adicional de reto al juego.

---

## Metodología de Desarrollo 

* **Metodología elegida:**  
Enfoque Ágil con Kanban Ligero.

### Justificación Técnica y Metodológica
Optamos por un enfoque ágil guiado por un tablero Kanban (gestionado a través de **GitHub Projects**) debido al tiempo reducido de ejecución (2 sesiones / 1 semana) y al tamaño de nuestro equipo (3 integrantes). Dado que la entrega requería iteraciones rápidas e incrementos funcionales constantes, organizar nuestro trabajo en columnas (`To Do`, `In Progress`, `Done`) nos permitió asignar un *Issue* a cada historia de usuario, priorizar las características base (US1 a US5) antes que las avanzadas (US6 y US7) y mantener visibilidad en tiempo real sobre los avances y responsabilidades de cada integrante.

---

## Estructura del Proyecto y Tecnologías

### Tecnologías Utilizadas
* **Lenguaje:** Python (uso de librerías estándar: `json`, `time`, `random`, `os`).
* **Control de Versiones y CASE:** Git, GitHub (Repositorio, Issues y GitHub Projects).
* **Modelado:** Draw.io / diagrams.net.

### Estructura de Archivos
```text
quiz-app-python/
│
├── docs/
│   └── diagram_architecture.png   # Diagrama de flujo del sistema (Fase de Modelado)
├── main.py                         # Código fuente principal del juego
├── questions.json                  # Banco de preguntas y respuestas en formato JSON
├── .gitignore                      # Archivos ignorados por Git
├── LICENSE                         # Licencia MIT
├── README.md                       # Documentación principal del proyecto
└── RETROSPECTIVA.md                # Informe de cierre y reflexión del equipo
```
---
## Retrospectiva del Equipo - Mini Proyecto (Zeldosos)
1. ¿Que funcionó bien?
La comunicación inicial: Aunque no teníamos mucha experiencia previa en proyectos colaborativos, logramos mantener buena comunicación para repartir las tareas iniciales y apoyarnos cuando alguien se atoraba.
Uso de herramientas visuales: Diseñar la lógica del flujo de trabajo y la estructura con ayuda de Mermaid.js nos ayudó mucho a entender cómo se conectaban las partes del código antes de empezar a moverle a las cosas.
Cumplimiento con la entrega básica: A pesar de las dudas con Git y la estructura general, logramos reunir las partes principales y completar la documentación solicitada.
2. ¿Que no funcionó bien / Nos costó trabajo?
Gestión y control de versiones con Git/GitHub: Al ser principiantes, nos dio bastante miedo cometer errores o sobrescribir cambios. Coordinar los commits y solucionar posibles conflictos fue la parte que más nos estresó.
Estimación de tiempos: Pensamos que seria menos tiempo el que nos tomaría organizar el repositorio e integrar la documentación. Dejamos varios detalles para el final porque pensábamos que sería más rápido de lo que realmente fue.
Falta de estándares al programar: Al inicio cada quién trabajó con su propia estructura o estilo, lo que hizo que al final fuera más difícil consolidar el proyecto de manera uniforme.
3. ¿Qué haríamos distinto la próxima vez?
Practicar más los flujos de Git desde el día 1: Definir reglas claras de cómo subir cambios ( pull request , nombres de ramas) antes de escribir código para no perdernos ni depender de una sola persona para actualizar el repositorio.
Organizar el trabajo en tareas más pequeñas: Dividir el proyecto en avances diarios más sencillos en lugar de intentar de hacer todo de una vez.
Documentar mas: Escribir las explicaciones, diagramas y comentarios a la par del código, en lugar de dejar toda la documentación y la retrospectiva para la fase de cierre.
