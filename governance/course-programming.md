# Programación y contexto global del curso

Este documento conserva las decisiones docentes que deben orientar la preparación
de clases y materiales. No sustituye los archivos curriculares de cada unidad ni
las instrucciones específicas incluidas en el `AGENTS.md` de cada sesión.

## Alcance y responsabilidades

La asignatura se organiza en cinco unidades didácticas:

| Unidad | Responsable | Contenido general |
|---:|---|---|
| 01 | Gabriel Modia | Fundamentos de sistemas y arquitecturas de computadores |
| 02 | Francisco Fraile | Fundamentos de programación en Python |
| 03 | Gabriel Modia | Programación con Arduino y comunicaciones |
| 04 | Francisco Fraile | Programación estructurada y manipulación de datos en Python |
| 05 | Gabriel Modia | Visualización de datos e interfaces de usuario |

El proyecto `edem-computer-science-course` cubre principalmente las unidades 02 y
04. La programación de las demás unidades se incluye para conservar la visión
global y las dependencias entre materias.

## Organización de los materiales

Se mantienen tres proyectos con responsabilidades distintas:

- `computer_science_tutorials`: fuente canónica de tutoriales, follow-alongs,
  actividades de clase, ejercicios tipo examen y publicación Sphinx/Furo.
- `edem-computer-science-course`: repositorio privado de trabajo de cada
  estudiante, con gobernanza, skills y materiales de sesión descargados en
  `workspace/`.
- `edem-iot-challenge`: repositorio privado por equipo para el proyecto
  colaborativo y la metodología proto-SDD.

Antes de cada clase, el alumnado descarga el paquete de la sesión desde los
materiales publicados y lo guarda bajo:

```text
workspace/<unidad>/<sesión>/
```

Cada paquete debe incluir su propio `AGENTS.md` con el contexto curricular y los
límites de asistencia aplicables.

## Metodología común

Cada sesión dura aproximadamente 1 hora y 45 minutos. Como patrón de referencia:

| Fase | Duración orientativa | Propósito |
|---|---:|---|
| Activación e introducción | 10–15 min | Recuperar conocimientos previos y plantear el problema |
| Actividad conceptual activa | 15–20 min | Experimentar con el concepto antes de formalizarlo |
| Follow-along | 30–35 min | Construir y razonar sobre un ejemplo guiado |
| Práctica | 25–30 min | Aplicar el aprendizaje con autonomía creciente |
| Cierre | 5–10 min | Explicar resultados, revisar evidencias y hacer commit |

La secuencia pedagógica general es:

> experimentar o predecir → formalizar → programar acompañado → practicar →
> explicar

En los notebooks se debe reforzar el ciclo:

> predecir → ejecutar → comparar → explicar

Las actividades físicas o manipulativas son un recurso recomendado cuando ayudan
a comprender el concepto, pero no son obligatorias en todas las sesiones.

## Unidad 01 — Sistemas y arquitecturas

Responsable: Gabriel Modia.

Contenidos generales:

- Introducción a los sistemas informáticos.
- Arquitectura de computadores y elementos internos.
- Representación de información y datos en computadores.

Esta unidad proporciona el contexto conceptual previo a la programación.

## Unidad 02 — Fundamentos de programación en Python

Responsable: Francisco Fraile.

### Secuencia

| Sesión | Contenido principal |
|---:|---|
| 03 | Entorno de trabajo: VS Code, Jupyter, Git y uso gobernado de la IA |
| 04 | Introducción a Python, ejecución en notebooks, librerías y llamadas a funciones |
| 05 | Variables, tipos de datos y operadores numéricos |
| 06 | Expresiones booleanas y control de selección |
| 08 | Bucles, listas, construcción de series e introducción a Matplotlib |

### Sesión 03 — Entorno de trabajo

Objetivo: preparar el entorno técnico y establecer el flujo de trabajo del curso.

Contenidos:

- VS Code, Python y Jupyter Notebooks.
- Diferencia entre celdas Markdown y celdas de código.
- Repositorio individual creado desde la plantilla.
- Flujo Git mínimo: `clone`, `status`, `add`, `commit`, `push`.
- Papel de la IA como apoyo al aprendizaje y límites de su uso.
- Primera ejecución, modificación y registro de una actividad.

Actividad activa sugerida: programar a una persona mediante instrucciones
precisas para explorar secuencia, ambigüedad, estado y errores.

Evidencia esperada: entorno validado y primer commit individual.

### Sesión 04 — Python, notebooks, librerías y llamadas

Objetivo: comprender la ejecución de Python y utilizar funciones ya disponibles
sin definir todavía funciones propias.

Contenidos:

- Código, instrucciones, literales y ejecución secuencial.
- Estado y reinicio del kernel.
- Llamadas a funciones y argumentos.
- Funciones built-in iniciales, como `print()`, `input()`, `type()` y `help()`.
- Diferencia entre funciones integradas y funciones de una librería.
- Instalación básica de paquetes con `pip`.
- Importación mediante `import`, alias y `from ... import ...`.
- Lectura de errores de sintaxis y de ejecución sencillos.

Actividad activa sugerida: ordenar físicamente las instrucciones de un programa,
predecir su salida e identificar una instrucción incorrecta.

Follow-along sugerido: programa interactivo breve que use funciones built-in,
inspeccione tipos, importe `math` y observe el estado del notebook.

Al terminar esta sesión, el alumnado debe reconocer una llamada, identificar sus
argumentos, instalar una librería e importar una función o módulo.

### Sesión 05 — Variables, tipos y operadores

Objetivo: adquirir los prerrequisitos numéricos necesarios para las prácticas de
Matemáticas antes de la sesión 06.

Contenidos:

- Variables, asignación y reasignación.
- Tipos `int`, `float` y `str`; anticipación mínima de `bool`.
- Operadores `+`, `-`, `*`, `/`, `//`, `%` y `**`.
- Precedencia y paréntesis.
- Conversión con `int()`, `float()` y `str()`.
- Expresiones para cálculos, conversiones y magnitudes geométricas.

Actividad activa sugerida: evaluación humana de expresiones, representando
variables, valores y operaciones.

Al terminar esta sesión, el alumnado debe realizar cálculos numéricos, reconocer
tipos básicos y convertir valores.

### Sesión 06 — Booleanos y control de selección

Objetivo: modelar decisiones mediante expresiones booleanas y estructuras
condicionales.

Contenidos:

- Valores booleanos.
- Comparaciones: `==`, `!=`, `<`, `<=`, `>` y `>=`.
- Operadores `and`, `or` y `not`.
- Estructuras `if`, `if-else` e `if-elif-else`.
- Condiciones compuestas, cobertura de casos y valores límite.
- Diagramas de flujo y pruebas representativas.

Actividad activa sugerida: clasificador humano construido con tarjetas y caminos
de decisión.

La iteración puede motivarse conceptualmente, pero no debe desplazar el objetivo
principal de la sesión.

### Sesión 08 — Bucles, listas, series y Matplotlib

Objetivo: repetir operaciones, conservar resultados y representarlos
gráficamente.

Contenidos:

- `for` y `range()`.
- Contadores y acumuladores sencillos.
- Listas como contenedores ordenados.
- Construcción progresiva mediante `append()`.
- Generación de series numéricas.
- Importación de `matplotlib.pyplot`.
- Uso inicial de `plot()`, etiquetas, título y `show()`.
- Predicción e interpretación de la forma de una gráfica.

Actividad activa sugerida: construir físicamente una serie paso a paso y
representar el papel del contador, el estado acumulado y la lista de resultados.

Al terminar esta sesión, el alumnado debe crear un bucle `for`, construir una
lista sencilla y representar sus valores. La definición de funciones propias se
reserva para la sesión 17.

## Unidad 03 — Arduino y comunicaciones

Responsable: Gabriel Modia.

Contenidos generales:

- Introducción a la plataforma Arduino.
- Tipos, elementos y topologías de red.
- Protocolos de comunicación y direcciones de Internet.
- Extensión de programación con Arduino.

Esta unidad separa temporalmente las unidades 02 y 04. Al retomar Python, conviene
activar explícitamente los conocimientos de variables, condicionales, bucles,
listas, importaciones y Matplotlib.

## Unidad 04 — Programación estructurada y manipulación de datos

Responsable: Francisco Fraile.

### Secuencia

| Sesión | Contenido principal |
|---:|---|
| 17 | Programación estructurada y definición de funciones |
| 18 | Iterables avanzados: tuplas, diccionarios y list comprehensions |
| 20 | NumPy: arrays y operaciones numéricas |
| 21 | Programación orientada a objetos |
| 22 | Datos estructurados, archivos, CSV, JSON y serialización |
| 23 | Pandas I: carga, inspección, indexación, filtrado y limpieza |
| 24 | Pandas II: joins, ordenación, agrupación, agregación y visualización |

### Sesión 17 — Funciones y programación estructurada

Objetivo: descomponer programas en unidades con responsabilidades claras.

Contenidos:

- Definición con `def`.
- Parámetros, argumentos y valores de retorno.
- Diferencia entre `print()` y `return`.
- Variables locales.
- Valores por defecto.
- Descomposición funcional.
- Docstrings y pruebas sencillas.
- Funciones que reciben o devuelven listas.

Actividad activa sugerida: máquina de funciones o rompecabezas funcional con
entradas, transformación, salida y responsabilidades.

Follow-along sugerido: refactorizar un notebook monolítico en funciones pequeñas.

### Sesión 18 — Iterables avanzados

Objetivo: seleccionar estructuras de datos apropiadas y comprender formas
compactas de transformación.

Contenidos:

- Repaso y operaciones relevantes con listas.
- Tuplas e inmutabilidad.
- Diccionarios, claves y valores.
- Recorrido de colecciones.
- Estructuras anidadas sencillas.
- Introducción a list comprehensions.
- Comparación entre comprensión y bucle explícito.

Debe priorizarse la legibilidad; las comprensiones no se utilizarán cuando oculten
el razonamiento que se pretende aprender.

### Sesión 20 — NumPy

Objetivo: conectar las series y listas conocidas con arrays y cálculo numérico.

Contenidos:

- Creación de arrays.
- `shape`, `dtype` y `size`.
- Indexación y slicing.
- Operaciones elemento a elemento.
- Vectores y matrices.
- Producto escalar y matricial.
- Transposición y compatibilidad dimensional.
- Comparación entre bucles y operaciones vectorizadas.
- Representación de resultados con Matplotlib.

Actividad activa sugerida: array humano o multiplicación matricial física.

### Sesión 21 — Programación orientada a objetos

Objetivo: comprender objetos como agrupaciones de estado y comportamiento.

Contenidos:

- Motivación de la programación orientada a objetos.
- Clases e instancias.
- Atributos.
- Métodos.
- Constructor `__init__`.
- Uso de `self`.
- Creación y uso de objetos sencillos.
- Responsabilidades de una clase.
- Ejemplos vinculados con sensores o dispositivos.

Debe evitarse introducir jerarquías de herencia o patrones avanzados si no son
necesarios para el objetivo básico.

### Sesión 22 — Datos estructurados y serialización

Objetivo: representar, guardar y recuperar registros antes de trabajar con
DataFrames.

Contenidos:

- Registros y estructuras anidadas.
- Lectura y escritura básica de archivos.
- Texto, CSV y JSON.
- Serialización y deserialización.
- Comparación entre representaciones.
- Registros de sensores como contexto aplicado.
- Introducción conceptual a los datos tabulares.

Actividad activa sugerida: representar el mismo registro mediante tarjetas como
diccionario, fila CSV y objeto JSON.

### Sesión 23 — Pandas I

Objetivo: cargar, inspeccionar, seleccionar y limpiar datos estructurados.

Contenidos:

- `Series` y `DataFrame`.
- Carga desde CSV y creación desde diccionarios.
- `head()`, `info()`, `describe()`, `shape` y `columns`.
- Selección de columnas.
- `loc` e `iloc`.
- Filtrado booleano.
- Tipos, conversiones y valores ausentes.
- Reglas básicas de validación y limpieza.

Actividad activa sugerida: DataFrame humano y dataset defectuoso.

### Sesión 24 — Pandas II

Objetivo: integrar tablas y producir resúmenes interpretables.

Contenidos:

- Claves e identificadores.
- `merge()` y joins básicos.
- Registros sin correspondencia y duplicados.
- `sort_values()`.
- `groupby()`.
- Agregaciones: `count`, `sum`, `mean`, `min` y `max`.
- Agrupaciones por una o varias variables.
- Visualización e interpretación de agregados.
- Flujo integrado: cargar, inspeccionar, limpiar, combinar, agrupar y visualizar.

Actividad activa sugerida: join con tarjetas seguido de agrupación física.

## Unidad 05 — Visualización e interfaces

Responsable: Gabriel Modia.

Contenidos generales:

- Introducción a la visualización de datos.
- Introducción al diseño e implementación de interfaces de usuario.

La experiencia previa con Matplotlib en las unidades 02 y 04 debe servir como
punto de partida para esta unidad.

## Sesión 30 — Síntesis y ensayo de examen

Objetivo: integrar contenidos y practicar una resolución autónoma y verificable.

Dinámica orientativa:

1. Explicación de la actividad y lectura del problema.
2. Resolución individual.
3. Comparación por parejas.
4. Discusión de estrategias y errores frecuentes.
5. Revisión y segunda oportunidad de corrección.

La asistencia de IA debe estar desactivada o restringida por un `AGENTS.md`
específico de práctica de examen. Nunca debe proporcionar una solución completa.

## Dependencias curriculares críticas

- Antes de la sesión 06, el alumnado debe conocer operadores numéricos,
  instalación e importación de librerías.
- Antes de la sesión 17, debe conocer llamadas a funciones, bucles, listas,
  construcción de series y una introducción a Matplotlib.
- La definición de funciones propias comienza formalmente en la sesión 17.
- Tuplas, diccionarios y list comprehensions comienzan en la sesión 18.
- NumPy comienza en la sesión 20.
- Las clases comienzan en la sesión 21.
- Pandas comienza en la sesión 23.

Al preparar cualquier material, se deben respetar estas dependencias y consultar
el archivo específico de la unidad:

- `governance/curriculum/unit-02.md`
- `governance/curriculum/unit-04.md`

## Criterios para preparar una sesión

Cada paquete de sesión debería declarar:

- objetivo de aprendizaje;
- conocimientos previos;
- conceptos introducidos;
- conceptos todavía no permitidos;
- breve activación o actividad conceptual;
- recorrido del follow-along;
- práctica de refuerzo;
- evidencia observable de aprendizaje;
- nivel máximo de asistencia de IA;
- instrucciones para el cierre y el commit.

Los materiales deben conectar teoría, ejecución y explicación sin concentrar
demasiados conceptos nuevos en una misma sesión.
