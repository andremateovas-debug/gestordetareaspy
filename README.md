# gestordetareaspy
Gestor de tareas locla simple y minimalista en consola de python.


Gestor de Tareas en Python

<img width="1265" height="305" alt="Image" src="https://github.com/user-attachments/assets/0a619efc-6710-4914-9c22-4c58fe36c093" />


Descripción:

Este proyecto es un gestor de tareas simple desarrollado en Python. Permite al usuario organizar sus tareas diarias mediante una interfaz de consola, con opciones para agregar, visualizar y eliminar tareas.

Las tareas se almacenan en un archivo de texto (tareas.txt) dentro de la carpeta de origen del archivo main.py, lo que permite conservar la información incluso después de cerrar el programa.

Funcionalidades:
 - Agregar nuevas tareas
 - Ver lista de tareas existentes
 - Eliminar tareas por ID
 - Guardado automático en archivo local
Tecnologías utilizadas
Python 
import os


Cómo ejecutar el proyecto:

Clona este repositorio:
git clone https://github.com/andremateovas-debug/gestordetareaspy.git




Accede a la carpeta del proyecto:
cd gestordetareaspy
Ejecuta el programa:
python main.py

<img width="1120" height="613" alt="image" src="https://github.com/user-attachments/assets/8029faa4-f303-41fe-8477-9a2f75d56dc1" />



Al iniciar el programa, podrás elegir entre las siguientes opciones:

si → Agregar tarea
ver → Mostrar tareas
no → Eliminar tarea
salir → Cerrar el programa

Cada tarea se guarda con un ID único para facilitar su gestión.

Estructura del proyecto
gestordetareaspy
 ┣  tareas.txt
 ┣  main.py
 ┗  README.md
