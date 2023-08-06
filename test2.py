import tkinter as tk
from tkinter import filedialog
#from otra_interfaz import OtraInterfaz  # Importar la nueva clase
from test import *
import os
import subprocess


class InterfazTkinter:
    def __init__(self, root):
        self.root = root
        self.root.title("Interfaz con Tkinter")
        
        self.menu_bar = tk.Menu(root)
        
        # Crear el menú "Inicio" y agregar opción "Cambiar Interfaz Gráfica"
        self.inicio_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.inicio_menu.add_command(label="Cambiar Interfaz Gráfica", command=self.abrir_otra_interfaz)
        
        # Agregar el menú "Inicio" al principio de la barra de menú
        self.menu_bar.add_cascade(label="Inicio", menu=self.inicio_menu)
        
        # Crear el menú "Archivo" y agregar opciones
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Abrir GIF", command=self.choose_gif)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Salir", command=root.quit)
        
        # Agregar el menú "Archivo" a la barra de menú
        self.menu_bar.add_cascade(label="Archivo", menu=self.file_menu)
        
        # Asignar la barra de menú a la ventana
        self.root.config(menu=self.menu_bar)
        
        # Cuadro de texto para ingresar texto
        self.text_input = tk.Entry(root)
        self.text_input.grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        
        # Variable para almacenar la ruta del GIF
        self.gif_path = tk.StringVar()
        self.gif_path.set("A:\\Python\\Proyectos\\img\\audio_fotolead984.gif")
        
        # Cargar la imagen GIF
        self.gif_image = tk.PhotoImage(file=self.gif_path.get())
        
        # Mostrar la imagen GIF en una etiqueta
        self.gif_display = tk.Label(root, image=self.gif_image)
        self.gif_display.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
        
        # Cuadro de texto de solo lectura para mostrar nuevo texto
        self.new_text_input = tk.Entry(root, state="readonly", justify="center")
        self.new_text_input.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
        
        # Botón para cambiar elementos
        self.change_elements_btn = tk.Button(root, text="Cambiar Elementos", command=self.change_elements)
        self.change_elements_btn.grid(row=3, column=0, padx=10, pady=10)
        
        # Botón para cambiar texto
        self.change_text_btn = tk.Button(root, text="Cambiar Texto", command=self.change_label_text)
        self.change_text_btn.grid(row=3, column=1, padx=10, pady=10)
        
        # Botón para seleccionar un nuevo GIFs
        self.file_chooser_btn = tk.Button(root, text="Seleccionar GIF", command=self.choose_gif)
        self.file_chooser_btn.grid(row=4, column=0, columnspan=2, padx=10, pady=10)
        
        # Área de texto para mostrar contenido
        self.text_display = tk.Text(root, wrap=tk.WORD, state="disabled")
        self.text_display.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

    def abrir_otra_interfaz(self):
        try:
            subprocess.Popen(["python", "A:\\Python\\Proyectos\\gui\\test.py"])  # Abrir el archivo test.py
            self.root.destroy()  # Cerrar la ventana actual de Tkinter
        except FileNotFoundError:
            print("Archivo 'test.py' no encontrado.")
    
    def change_elements(self):
        # Obtener el texto ingresado y mostrarlo en el área de texto
        input_text = self.text_input.get()
        self.text_display.config(state="normal")
        self.text_display.delete(1.0, tk.END)
        self.text_display.insert(tk.END, input_text)
        self.text_display.config(state="disabled")
        
        # Mostrar el GIF
        self.gif_display.config(image=self.gif_image)
    
    def change_label_text(self):
        # Obtener el nuevo texto y mostrarlo en el área de texto
        new_text = self.new_text_input.get()
        self.text_display.config(state="normal")
        self.text_display.delete(1.0, tk.END)
        self.text_display.insert(tk.END, new_text)
        self.text_display.config(state="disabled")
    
    def choose_gif(self):
        # Abrir un cuadro de diálogo para seleccionar un nuevo GIF
        file_path = filedialog.askopenfilename(filetypes=[("GIF files", "*.gif")])
        if file_path:
            # Actualizar la ruta del GIF y mostrar la nueva imagen
            self.gif_path.set(file_path)
            self.gif_image = tk.PhotoImage(file=self.gif_path.get())
            self.gif_display.config(image=self.gif_image)

if __name__ == "__main__":
    root = tk.Tk()
    app = InterfazTkinter(root)
    root.mainloop()
