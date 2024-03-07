import tkinter as tk
from tkinter import ttk, messagebox, filedialog
from PIL import Image, ImageTk
import platform

nombre_archivo_guardado = ""
cambios_no_guardados = False
# Hola Hector


def abrir_nuevo_archivo():
    global cajon_texto_2, nombre_archivo_abierto, nombre_archivo_guardado

    # Abrir un cuadro de diálogo para seleccionar el archivo
    nombre_archivo_abierto = filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.txt")])
    nombre_archivo_guardado = nombre_archivo_abierto
    # Verificar si se seleccionó un archivo
    if nombre_archivo_abierto:
        # Leer el contenido del archivo seleccionado y cargarlo en el cajón de texto 2
        with open(nombre_archivo_abierto, 'r') as archivo:
            contenido = archivo.read()
            cajon_texto_2.delete("1.0", tk.END)  # Limpiar el contenido actual
            cajon_texto_2.insert("1.0", contenido)
            actualizar_numeros_linea()
            scroll_Mouse(0)
            scroll_both_widgets(0)


def crear_nuevo_archivo():
    global cajon_texto_2, nombre_archivo_guardado, cambios_no_guardados

    # Verificar si hay cambios no guardados
    if cambios_no_guardados:
        # Mostrar ventana de confirmación
        respuesta = messagebox.askyesno("Confirmar", "¿Está seguro de abrir un nuevo archivo? Se perderán los cambios no guardados.")
        if not respuesta:
            return  # Si el usuario elige cancelar, no hacer nada

    # Limpiar el cajón de texto 2 y la variable de nombre de archivo guardado
    cajon_texto_2.delete("1.0", tk.END)
    nombre_archivo_guardado = ""
    cambios_no_guardados = False


def guardar_archivo_como():
    global cajon_texto_2, nombre_archivo_guardado, cambios_no_guardados

    # Abrir un cuadro de diálogo para seleccionar la ubicación y el nombre del archivo
    nombre_archivo_guardado = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Archivos de texto", "*.txt")])

    # Verificar si se seleccionó un archivo
    if nombre_archivo_guardado:
        with open(nombre_archivo_guardado, 'w') as archivo:
            # Obtener el contenido del cajón de texto 2 y escribirlo en el archivo
            contenido = cajon_texto_2.get("1.0", tk.END)
            archivo.write(contenido)
            cambios_no_guardados = False


def guardar_archivo():
    print("hola")
    global cajon_texto_2, nombre_archivo_guardado, cambios_no_guardados

    # Verificar si ya hay un archivo abierto
    if nombre_archivo_guardado:
        # Sobrescribir el archivo existente
        with open(nombre_archivo_guardado, 'w') as archivo:
            contenido = cajon_texto_2.get("1.0", tk.END)
            archivo.write(contenido)
            cambios_no_guardados = False
    else:
        # Abrir un cuadro de diálogo para seleccionar la ubicación y el nombre del archivo
        nombre_archivo_guardado = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Archivos de texto", "*.txt")])

        # Verificar si se seleccionó un archivo
        if nombre_archivo_guardado:
            with open(nombre_archivo_guardado, 'w') as archivo:
                contenido = cajon_texto_2.get("1.0", tk.END)
                archivo.write(contenido)
                cambios_no_guardados = False


def mostrar_about():
    about_text = "IDE de la materia Compiladores"
    messagebox.showinfo("About", about_text)


def cerrar_archivo():
    print("cerrar")
    cajon_texto_2.delete(1.0, "end")


def mostrar_run():
    about_text = "Compilar programa"
    messagebox.showinfo("Compilar", about_text)


def cambiar_tema(tema):
    if tema == "claro":
        ventana.tk_setPalette(background="#FFFFFF", foreground="#000000")
    elif tema == "oscuro":
        ventana.tk_setPalette(background="#2E2E2E", foreground="#FFFFFF")


def actualizar_numeros_linea(event=None):
    # Actualizar los números de línea
    global auxnum
    cajon_texto_1.config(state="normal")

    # Obtener el número actual de líneas en el cajón de texto 2
    num_lineas_actual = int(cajon_texto_2.index(tk.END).split('.')[0])
    # print(cajon_texto_2.index(tk.INSERT), num_lineas_actual)
    if auxnum > 2:
        # Si se agregaron líneas
        if num_lineas_actual > auxnum:
            # Agregar números de línea adicionales
            for i in range(auxnum + 1, num_lineas_actual + 1):
                cajon_texto_1.insert(tk.END, f"{i}\n")

            auxnum = num_lineas_actual
        else:
            # Si se eliminaron líneas
            for i in range(auxnum, num_lineas_actual, -1):
                cajon_texto_1.delete(f"{i}.0", f"{i + 1}.0")

            auxnum = num_lineas_actual
    else:
        # Si es la primera vez, inicializar los números de línea
        cajon_texto_1.delete(1.0, tk.END)
        for i in range(1, num_lineas_actual + 1):
            cajon_texto_1.insert(tk.END, f"{i}\n")

        auxnum = num_lineas_actual

    cajon_texto_1.config(state="disabled")
    cajon_texto_1.yview_moveto(cajon_texto_2.yview()[0])

def scroll_both_widgets(event):
    # Resaltar la línea actual donde está el cursor
    current_line = cajon_texto_2.index(tk.INSERT).split('.')[0]
    tag_name = "highlight"
    cajon_texto_2.tag_delete(tag_name)
    cajon_texto_2.tag_add(tag_name, f"{current_line}.0", f"{current_line}.end+1c")
    cajon_texto_2.tag_config(tag_name, background="lightgray", foreground="black")

    num_lineas_actual = int(cajon_texto_2.index(tk.END).split('.')[0])
    print(cajon_texto_2.index(tk.INSERT), num_lineas_actual)



def scroll_Mouse(event):
    cajon_texto_1.yview_moveto(cajon_texto_2.yview()[0])


def scroll_Mouse1(event):
    cajon_texto_2.yview_moveto(cajon_texto_1.yview()[0])


def abrir_ventana():
    # Crear una instancia de la ventana principal
    global ventana
    ventana = tk.Tk()
    ventana.title("IDE Compiladores")
    sistema_operativo = platform.system()
    print(sistema_operativo)
    global auxnum
    auxnum = 0
    # Crear una barra de menú
    menu_bar = tk.Menu(ventana)
    ventana.config(menu=menu_bar)

    # Menú "File" con opciones "Nuevo" y "Abrir"
    file_menu = tk.Menu(menu_bar, tearoff=0)
    file_menu.add_command(label="Nuevo", command=crear_nuevo_archivo)
    file_menu.add_command(label="Abrir", command=abrir_nuevo_archivo)
    file_menu.add_command(label="Guardar", command=guardar_archivo)
    file_menu.add_command(label="Guardar Como", command=guardar_archivo_como)
    menu_bar.add_cascade(label="File", menu=file_menu)

    # Menú "About" con opción "IDE Compiladores"
    run_menu = tk.Menu(menu_bar, tearoff=0)
    run_menu.add_command(label="Compilar", command=mostrar_run)
    menu_bar.add_cascade(label="Run", menu=run_menu)

    # Menú "Tema" con opciones "Claro" y "Oscuro"
    tema_menu = tk.Menu(menu_bar, tearoff=0)
    tema_menu.add_command(label="Claro", command=lambda: cambiar_tema("claro"))
    tema_menu.add_command(label="Oscuro", command=lambda: cambiar_tema("oscuro"))
    menu_bar.add_cascade(label="Tema", menu=tema_menu)

    # Botones con iconos
    icono_nuevo = Image.open("images/new.png")  # Ruta al icono de nuevo
    icono_nuevo = icono_nuevo.resize((20,20), Image.LANCZOS)
    icono_nuevo = ImageTk.PhotoImage(icono_nuevo)
    boton_nuevo = ttk.Button(menu_bar, image=icono_nuevo, command=crear_nuevo_archivo)
    boton_nuevo.image = icono_nuevo  # Conservar referencia para evitar que se elimine por el recolector de basura
    menu_bar.add_cascade(label="Nuevo", command=crear_nuevo_archivo, compound=tk.LEFT)

    icono_abrir = Image.open("images/open.png")  # Ruta al icono de abrir
    icono_abrir = icono_abrir.resize((20,20), Image.LANCZOS)
    icono_abrir = ImageTk.PhotoImage(icono_abrir)
    boton_abrir = ttk.Button(menu_bar, image=icono_abrir, command=abrir_nuevo_archivo)
    boton_abrir.image = icono_abrir

    menu_bar.add_cascade(label="Abrir", command=abrir_nuevo_archivo, compound=tk.LEFT)

    icono_guardar = Image.open("images/save.png")  # Ruta al icono de guardar
    icono_guardar = icono_guardar.resize((20,20), Image.LANCZOS)
    icono_guardar = ImageTk.PhotoImage(icono_guardar)
    boton_guardar = ttk.Button(menu_bar, image=icono_guardar, command=guardar_archivo)
    boton_guardar.image = icono_guardar

    menu_bar.add_cascade(label="Guardar", command=guardar_archivo, compound=tk.LEFT)
    menu_bar.add_cascade(label="Cerrar", command=cerrar_archivo, compound=tk.LEFT)

    # Menú "About" con opción "IDE Compiladores"
    about_menu = tk.Menu(menu_bar, tearoff=0)
    about_menu.add_command(label="IDE Compiladores", command=mostrar_about)
    menu_bar.add_cascade(label="About", menu=about_menu)

    # Crear un contenedor principal (frame)
    contenedor_principal = ttk.PanedWindow(ventana, orient=tk.VERTICAL)
    contenedor_principal.pack(expand=True, fill="both")

    # Primera fila con cajones 1, 2 y 3
    fila_1 = ttk.PanedWindow(contenedor_principal, orient=tk.HORIZONTAL)
    contenedor_principal.add(fila_1)

    # Crear cajones de texto en la primera fila
    global cajon_texto_1
    cajon_texto_1 = tk.Text(fila_1, width=4, wrap="none", state="disabled")
    cajon_texto_1.pack(side=tk.LEFT, fill=tk.Y)
    fila_1.add(cajon_texto_1)
    cajon_texto_1.insert(tk.END,"1")

    global cajon_texto_2
    cajon_texto_2 = tk.Text(fila_1, wrap="none", insertbackground="black")
    cajon_texto_2.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    fila_1.add(cajon_texto_2)
    # cajon_texto_2.bind("<KeyRelease>", vincular_cajones_texto)

    # Vincular la actualización de los números de línea con el desplazamiento del texto
    cajon_texto_2.bind('<Configure>', actualizar_numeros_linea)
    cajon_texto_2.bind('<Key>', actualizar_numeros_linea)

    # Vincular el desplazamiento del widget de números de línea con el widget de texto
    cajon_texto_2.bind('<KeyRelease>', scroll_both_widgets)

    if sistema_operativo == "Linux":
        cajon_texto_2.bind('<Button-4>', scroll_Mouse)
        cajon_texto_2.bind('<Button-5>', scroll_Mouse)
        cajon_texto_1.bind('<Button-4>', scroll_Mouse)
        cajon_texto_1.bind('<Button-5>', scroll_Mouse)
    else:
        cajon_texto_2.bind('<MouseWheel>', scroll_Mouse)
    # Crear un Notebook para cajon_texto_3 en la primera fila
    notebook_3 = ttk.Notebook(fila_1)

    frame = tk.Frame(notebook_3)
    text_widget = tk.Text(frame, wrap="word")
    text_widget.pack(expand=True, fill="both")
    notebook_3.add(frame, text=f"Lexico")
    frame = tk.Frame(notebook_3)
    text_widget = tk.Text(frame, wrap="word")
    text_widget.pack(expand=True, fill="both")
    notebook_3.add(frame, text=f"Sintactico")
    frame = tk.Frame(notebook_3)
    text_widget = tk.Text(frame, wrap="word")
    text_widget.pack(expand=True, fill="both")
    notebook_3.add(frame, text=f"Semantico")
    frame = tk.Frame(notebook_3)
    text_widget = tk.Text(frame, wrap="word")
    text_widget.pack(expand=True, fill="both")
    notebook_3.add(frame, text=f"Hash Table")
    frame = tk.Frame(notebook_3)
    text_widget = tk.Text(frame, wrap="word")
    text_widget.pack(expand=True, fill="both")
    notebook_3.add(frame, text=f"Codigo Intermedio")

    cajon_texto_3 = notebook_3
    # cajon_texto_3 = tk.Text(fila_1, wrap="word", height=10, width=150)
    fila_1.add(cajon_texto_3)

    # Segunda fila con cajon 4
    fila_2 = ttk.PanedWindow(contenedor_principal, orient=tk.HORIZONTAL)

    contenedor_principal.add(fila_2)

    # Crear un Notebook para cajon_texto_4 en la segunda fila
    notebook_4 = ttk.Notebook(fila_2)
    frame = tk.Frame(notebook_4)
    text_widget = tk.Text(frame, wrap="word")
    text_widget.pack(expand=True, fill="both")
    notebook_4.add(frame, text=f"Errores Lexicos")
    frame = tk.Frame(notebook_4)
    text_widget = tk.Text(frame, wrap="word")
    text_widget.pack(expand=True, fill="both")
    notebook_4.add(frame, text=f"Errores Sintacticos")
    frame = tk.Frame(notebook_4)
    text_widget = tk.Text(frame, wrap="word")
    text_widget.pack(expand=True, fill="both")
    notebook_4.add(frame, text=f"Errores Semanticos")
    frame = tk.Frame(notebook_4)
    text_widget = tk.Text(frame, wrap="word")
    text_widget.pack(expand=True, fill="both")
    notebook_4.add(frame, text=f"Resultados")

    cajon_texto_4 = notebook_4
    fila_2.add(cajon_texto_4)

    # Mostrar la ventana
    ventana.mainloop()
    # Hola


# Llamar a la función para abrir la ventana
abrir_ventana()