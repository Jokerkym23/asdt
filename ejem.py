import os
import datetime

# Función para agregar una tarea a la lista de tareas pendientes
def agregar_tarea(titulo, descripcion, fecha_vencimiento=None):
    tarea = {"Titulo": titulo, "Descripcion": descripcion, "Fecha de Vencimiento": fecha_vencimiento}
    tareas_pendientes.append(tarea)

# Función para listar todas las tareas pendientes
def listar_tareas(tareas):
    for i, tarea in enumerate(tareas, start=1):
        print(f"Tarea {i}:")
        print(f"Título: {tarea['Titulo']}")
        print(f"Descripción: {tarea['Descripcion']}")
        if tarea['Fecha de Vencimiento']:
            print(f"Fecha de Vencimiento: {tarea['Fecha de Vencimiento']}")
        print("-" * 30)

# Función para marcar una tarea como completada
def marcar_completada(indice):
    tarea_completada = tareas_pendientes.pop(indice - 1)
    tarea_completada["Fecha de Completado"] = datetime.datetime.now()
    tareas_completadas.append(tarea_completada)

# Función para mostrar las tareas completadas
def mostrar_tareas_completadas():
    for i, tarea in enumerate(tareas_completadas, start=1):
        print(f"Tarea Completada {i}:")
        print(f"Título: {tarea['Titulo']}")
        print(f"Descripción: {tarea['Descripcion']}")
        print(f"Fecha de Completado: {tarea['Fecha de Completado']}")
        print("-" * 30)

# Función para guardar las tareas en un archivo de texto
def guardar_tareas(nombre_archivo, tareas):
    with open(nombre_archivo, "w") as archivo:
        for tarea in tareas:
            archivo.write(f"Título: {tarea['Titulo']}\n")
            archivo.write(f"Descripción: {tarea['Descripcion']}\n")
            if tarea['Fecha de Vencimiento']:
                archivo.write(f"Fecha de Vencimiento: {tarea['Fecha de Vencimiento']}\n")
            archivo.write("-" * 30 + "\n")

# Función para cargar las tareas desde un archivo de texto
def cargar_tareas(nombre_archivo):
    tareas = []
    try:
        with open(nombre_archivo, "r") as archivo:
            tarea = {}
            for linea in archivo:
                linea = linea.strip()
                if linea.startswith("Título: "):
                    tarea["Titulo"] = linea.split("Título: ")[1]
                elif linea.startswith("Descripción: "):
                    tarea["Descripcion"] = linea.split("Descripción: ")[1]
                elif linea.startswith("Fecha de Vencimiento: "):
                    tarea["Fecha de Vencimiento"] = linea.split("Fecha de Vencimiento: ")[1]
                elif linea == "-" * 30:
                    tareas.append(tarea)
                    tarea = {}
    except FileNotFoundError:
        pass
    return tareas

# Nombre de los archivos de texto para las tareas pendientes y completadas
archivo_tareas_pendientes = "tareas_pendientes.txt"
archivo_tareas_completadas = "tareas_completadas.txt"

# Cargar las tareas pendientes y completadas desde los archivos
tareas_pendientes = cargar_tareas(archivo_tareas_pendientes)
tareas_completadas = cargar_tareas(archivo_tareas_completadas)

while True:
    print("\n--- Administrador de Tareas ---")
    print("1. Agregar una tarea")
    print("2. Listar tareas pendientes")
    print("3. Marcar tarea como completada")
    print("4. Mostrar tareas completadas")
    print("5. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    if opcion == "1":
        titulo = input("Ingrese el título de la tarea: ")
        descripcion = input("Ingrese la descripción de la tarea: ")
        fecha_vencimiento = input("Ingrese la fecha de vencimiento (opcional, formato: yyyy-mm-dd): ")
        if fecha_vencimiento:
            fecha_vencimiento = datetime.datetime.strptime(fecha_vencimiento, "%Y-%m-%d")
        agregar_tarea(titulo, descripcion, fecha_vencimiento)
        print("Tarea agregada con éxito.")
    
    elif opcion == "2":
        if tareas_pendientes:
            print("\n--- Tareas Pendientes ---")
            listar_tareas(tareas_pendientes)
        else:
            print("No hay tareas pendientes.")
    
    elif opcion == "3":
        if tareas_pendientes:
            print("\n--- Tareas Pendientes ---")
            listar_tareas(tareas_pendientes)
            indice = int(input("Ingrese el número de la tarea que desea marcar como completada: "))
            if 1 <= indice <= len(tareas_pendientes):
                marcar_completada(indice)
                guardar_tareas(archivo_tareas_pendientes, tareas_pendientes)
                guardar_tareas(archivo_tareas_completadas, tareas_completadas)
                print("Tarea marcada como completada con éxito.")
            else:
                print("Número de tarea inválido.")
        else:
            print("No hay tareas pendientes para marcar como completadas.")
    
    elif opcion == "4":
        if tareas_completadas:
            print("\n--- Tareas Completadas ---")
            mostrar_tareas_completadas()
        else:
            print("No hay tareas completadas.")
    
    elif opcion == "5":
        print("Saliendo del programa...")
        break
    
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")