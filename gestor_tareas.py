# gestor_tareas.py

tareas = []

while True:
    print("\n=== GESTOR DE TAREAS ===")
    print("1. Ver tareas")
    print("2. Añadir tarea")
    print("3. Eliminar tarea")
    print("4. Salir")

    opcion = input("Elige una opción: ")

    if opcion == "1":
        if len(tareas) == 0:
            print("No hay tareas.")
        else:
            print("\nTus tareas:")
            for i, tarea in enumerate(tareas, start=1):
                print(f"{i}. {tarea}")

    elif opcion == "2":
        nueva_tarea = input("Escribe la tarea: ")
        tareas.append(nueva_tarea)
        print("✅ Tarea añadida.")

    elif opcion == "3":
        if len(tareas) == 0:
            print("No hay tareas para eliminar.")
        else:
            for i, tarea in enumerate(tareas, start=1):
                print(f"{i}. {tarea}")

            try:
                numero = int(input("Número de la tarea a eliminar: "))
                tareas.pop(numero - 1)
                print("🗑️ Tarea eliminada.")
            except:
                print("Número no válido.")

    elif opcion == "4":
        print("¡Hasta luego!")
        break

    else:
        print("Opción no válida.")