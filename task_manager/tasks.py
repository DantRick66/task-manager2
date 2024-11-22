"""
Módulo para gestionar tareas del proyecto.
"""

"""Añade una tarea a la lista."""
def add_task(tasks, task):
    tasks.append(task)
    print(f"Tarea '{task}' añadida con éxito.")


"""Lista todas las tareas."""
def list_tasks(tasks):
    if not tasks:
        print("No hay tareas.")
    else:
        print("\nLista de Tareas:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

"""Elimina una tarea de la lista por su número."""
def delete_task(tasks, task_number):
    if 0 < task_number <= len(tasks):
        removed = tasks.pop(task_number - 1)
        print(f"Tarea '{removed}' eliminada.")
    else:
        print("Número de tarea inválido.")
