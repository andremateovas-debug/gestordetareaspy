# gestor de tareas 
#  objetivo: organizar tus tareas diarias de forma sencilla y eficiente
# descripcion: permite agregar, ver y cancelar tareas en una lista de tareas
# las tareas se guardan en un archivo de texto para su posterior consulta y gestión

# Autor: Andre Mateo Vasquez Mosqueda


import os


ARCHIVO_TAREAS = os.path.join(os.path.dirname(__file__), "tareas.txt")

def cargar_tareas():
    if os.path.exists(ARCHIVO_TAREAS):
        with open(ARCHIVO_TAREAS, "r", encoding="utf-8") as archivo:
            tareas = {}
            for linea in archivo.readlines():
                linea = linea.strip()
                if linea and ": " in linea:
                    id_tarea, texto = linea.split(": ", 1)
                    tareas[int(id_tarea)] = texto
            return tareas
    return {}

def guardar_tareas(tareas):
    with open(ARCHIVO_TAREAS, "w", encoding="utf-8") as archivo:
        for id_tarea in sorted(tareas.keys()):
            archivo.write(f"{id_tarea}: {tareas[id_tarea]}\n")

def mostrar_menu():
    
    print("Bienvenido a tu lista de tareas.")
    print("_" * 62)
    print("Puedes: \n - agregar tareas \n - ver las tareas disponibles \n - Cancelar tareas  \n - salir del programa.")
    print("_" * 62)

def obtener_proximo_id(tareas):
    return max(tareas.keys()) + 1 if tareas else 1


tareas = cargar_tareas()
mostrar_menu()

while True:
    accion = input("¿Que deseas hacer? \n - si (Agregar) \n - ver (Ver tareas) \n - no (Borrar tareas) \n - salir ").lower().strip()
    
    if accion == "si":
        tarea = input("Ingrese la tarea: ").strip()

        if tarea == "salir":
            print("Saliendo del programa")
            break
        elif tarea:
            id_tarea = obtener_proximo_id(tareas)
            tareas[id_tarea] = tarea
            guardar_tareas(tareas)
            print("Tarea agregada")
            print(f"Tarea: {tarea} ID: {id_tarea}")
        
        else:
            print("La tarea no puede estar vacía.")
    
    elif accion == "no":
        if tareas == {}:
            print("No hay tareas disponibles para cancelar")
        else:
            try:
                id_cancelar = int(input("Ingrese el ID de la tarea que desea cancelar: "))
                if id_cancelar in tareas:
                    del tareas[id_cancelar]
                    guardar_tareas(tareas)
                    print("Tarea cancelada.")
                else:
                    print("La tarea no se encuentra en la lista")
            except ValueError:
                print("ID inválido")
    
    elif accion == "salir":
        print("Saliendo del programa")
        break
    
    elif accion == "ver":
        if tareas == {}:
            print("No hay tareas disponibles")
        else:
            print("Tareas disponibles:")
            for id_tarea in sorted(tareas.keys()):
                print(f"  {id_tarea}. {tareas[id_tarea]}")
    
    else:
        print("Acción no reconocida. Por favor, ingresa una acción válida")
