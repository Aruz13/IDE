import tkinter as tk
from tkinter import ttk, messagebox

def abrir_nuevo_archivo():
    messagebox.showinfo("File", "Abrir nuevo archivo")

def crear_nuevo_archivo():
    messagebox.showinfo("File", "Crear nuevo archivo")

def mostrar_about():
    about_text = "IDE de la materia Compiladores"
    messagebox.showinfo("About", about_text)

def vincular_cajones_texto(event):
    global cajon_texto_2

    # Obtener la línea actual del cajón de texto 2
    linea_actual = int(cajon_texto_2.index(tk.CURRENT).split('.')[0])

    # Obtener el texto de la línea actual en el cajón de texto 2
    texto_linea_actual = cajon_texto_2.get(f"{linea_actual}.0", f"{linea_actual}.end")

    # Actualizar el cajón de texto 1 con los números de línea
    actualizar_numeros_linea()

    # Resaltar la línea actual en negrita
    cajon_texto_1.tag_remove("negrita", "1.0", tk.END)
    cajon_texto_1.tag_add("negrita", f"{linea_actual}.0", f"{linea_actual}.end")
    cajon_texto_1.tag_config("negrita", font=("Helvetica", 8, "bold"))

def actualizar_numeros_linea():
    global cajon_texto_1, cajon_texto_2

    # Obtener la primera y última línea visible en el cajón de texto 2
    primera_linea_visible = int(cajon_texto_2.index("@0,0").split('.')[0])
    ultima_linea_visible = int(cajon_texto_2.index("@0,99999999999999").split('.')[0])

    # Calcular el rango de líneas para prellenar el cajón de texto 1
    rango_prellenado = range(max(1, primera_linea_visible - 10), max(ultima_linea_visible + 10, 1))

    # Borrar el contenido actual del cajón de texto 1
    cajon_texto_1.delete("1.0", tk.END)

    # Agregar números de línea al cajón de texto 1
    for i in rango_prellenado:
        cajon_texto_1.insert(tk.END, f"{i}\n")

    # Configurar el ancho máximo del cajón de texto 1
    cajon_texto_1.config(width=6)

def cambiar_tema(tema):
    if tema == "claro":
        ventana.tk_setPalette(background="#FFFFFF", foreground="#000000")
    elif tema == "oscuro":
        ventana.tk_setPalette(background="#2E2E2E", foreground="#FFFFFF")

def abrir_ventana():
    # Crear una instancia de la ventana principal
    global ventana
    ventana = tk.Tk()
    ventana.title("IDE Compiladores")

    # Crear una barra de menú
    menu_bar = tk.Menu(ventana)
    ventana.config(menu=menu_bar)

    # Menú "File" con opciones "Nuevo" y "Abrir"
    file_menu = tk.Menu(menu_bar, tearoff=0)
    file_menu.add_command(label="Nuevo", command=crear_nuevo_archivo)
    file_menu.add_command(label="Abrir", command=abrir_nuevo_archivo)
    menu_bar.add_cascade(label="File", menu=file_menu)

    # Menú "About" con opción "IDE Compiladores"
    about_menu = tk.Menu(menu_bar, tearoff=0)
    about_menu.add_command(label="IDE Compiladores", command=mostrar_about)
    menu_bar.add_cascade(label="About", menu=about_menu)

    # Menú "Tema" con opciones "Claro" y "Oscuro"
    tema_menu = tk.Menu(menu_bar, tearoff=0)
    tema_menu.add_command(label="Claro", command=lambda: cambiar_tema("claro"))
    tema_menu.add_command(label="Oscuro", command=lambda: cambiar_tema("oscuro"))
    menu_bar.add_cascade(label="Tema", menu=tema_menu)

    # Crear un contenedor principal (frame)
    contenedor_principal = ttk.PanedWindow(ventana, orient=tk.VERTICAL)
    contenedor_principal.pack(expand=True, fill="both")

    # Primera fila con cajones 1, 2 y 3
    fila_1 = ttk.PanedWindow(contenedor_principal, orient=tk.HORIZONTAL)
    contenedor_principal.add(fila_1)

    # Crear cajones de texto en la primera fila
    global cajon_texto_1
    cajon_texto_1 = tk.Text(fila_1, wrap="none", height=10, width=6)
    fila_1.add(cajon_texto_1)

    global cajon_texto_2
    cajon_texto_2 = tk.Text(fila_1, wrap="word", height=10, width=20)
    fila_1.add(cajon_texto_2)
    cajon_texto_2.bind("<KeyRelease>", vincular_cajones_texto)

    # Crear un Notebook para cajon_texto_3 en la primera fila
    notebook_3 = ttk.Notebook(fila_1)
    for i in range(5):
        frame = tk.Frame(notebook_3)
        text_widget = tk.Text(frame, wrap="word")
        text_widget.pack(expand=True, fill="both")
        notebook_3.add(frame, text=f"Pestaña {i+1}")

    cajon_texto_3 = notebook_3
    fila_1.add(cajon_texto_3)

    # Segunda fila con cajon 4
    fila_2 = ttk.PanedWindow(contenedor_principal, orient=tk.HORIZONTAL)
    contenedor_principal.add(fila_2)

    # Crear un Notebook para cajon_texto_4 en la segunda fila
    notebook_4 = ttk.Notebook(fila_2)
    for i in range(4):
        frame = tk.Frame(notebook_4)
        text_widget = tk.Text(frame, wrap="word")
        text_widget.pack(expand=True, fill="both")
        notebook_4.add(frame, text=f"Pestaña {i+1}")

    cajon_texto_4 = notebook_4
    fila_2.add(cajon_texto_4)

    # Configurar que el cajón 1 no sea redimensionable horizontalmente
    cajon_texto_1.configure(width=6)
    # Mostrar la ventana
    ventana.mainloop()
    #Hola

# Llamar a la función para abrir la ventana
abrir_ventana()
