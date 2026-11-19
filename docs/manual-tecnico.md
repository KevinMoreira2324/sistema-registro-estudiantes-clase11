# MANUAL TÉCNICO

## Descripción técnica

El Gestor de Tareas es una aplicación desarrollada en Python que permite administrar una lista de tareas mediante una interfaz de consola. El usuario puede agregar nuevas tareas, visualizar las tareas almacenadas y eliminar aquellas que ya no necesite.

<br aria-hidden="true">

## Tecnología utilizada

- Python 3.x
- Consola de comandos (CMD o Terminal)
- Visual Studio Code (opcional)

<br aria-hidden="true">

## Requisitos técnicos

### Hardware
- Procesador básico.
- 2 GB de RAM o superior.

### Software
- Python 3.x instalado.
- Sistema operativo Windows, Linux o macOS.

<br aria-hidden="true">

## Estructura del proyecto

```text
Gestor_Tareas/
│
├── gestor_tareas.py
├── README.md
├── manual_usuario.md
└── manual_tecnico.md
```

<br aria-hidden="true">

## Preparación o instalación

1. Descargar e instalar Python desde https://www.python.org.
2. Activar la opción **Add Python to PATH** durante la instalación.
3. Crear una carpeta para el proyecto.
4. Guardar el archivo `gestor_tareas.py` dentro de la carpeta creada.

<br aria-hidden="true">

## Forma de ejecución

1. Abrir la terminal o consola.
2. Acceder a la carpeta donde está guardado el proyecto.

```bash
cd ruta_de_la_carpeta
```

3. Ejecutar el programa:

```bash
python gestor_tareas.py
```

o

```bash
py gestor_tareas.py
```

<br aria-hidden="true">

## Explicación breve del funcionamiento

Al ejecutar el programa se muestra un menú con las siguientes opciones:

```text
=== GESTOR DE TAREAS ===
1. Ver tareas
2. Añadir tarea
3. Eliminar tarea
4. Salir
```

El usuario selecciona una opción introduciendo el número correspondiente. Las tareas se almacenan en una lista dentro del programa. Cuando se agrega una nueva tarea, esta se guarda en la lista; cuando se elimina una tarea, se elimina de la misma lista.

El programa utiliza:

- Variables para almacenar información.
- Listas para guardar las tareas.
- Condicionales (`if`, `elif`, `else`) para controlar las opciones del menú.
- Bucles (`while`) para mantener el programa en ejecución.
- Manejo de errores (`try-except`) para evitar fallos al introducir 