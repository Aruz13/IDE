import tkinter as tk
from tkinter import ttk

def toggle_dark_mode():
    current_theme = root.tk_getPalette()  # Obtener el tema actual
    if current_theme == "":
        root.tk_setPalette(background='#2E2E2E', foreground='#FFFFFF')  # Cambiar a modo oscuro
    else:
        root.tk_setPalette("")  # Cambiar a modo claro

root = tk.Tk()
root.title("Ventana con Modo Oscuro")

# Botón para alternar el modo oscuro
dark_mode_button = ttk.Button(root, text="Alternar Modo Oscuro", command=toggle_dark_mode)
dark_mode_button.pack(pady=10)

# Agrega más elementos de la interfaz de usuario aquí...

root.mainloop()
