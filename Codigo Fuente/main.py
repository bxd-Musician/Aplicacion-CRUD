import mysql.connector
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

# Función para conectarse a la base de datos
def obtener_conexion():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="discjockey",
        database="unap"
    )

# Función para validar entradas y prevenir comandos peligrosos
def es_entrada_segura(*entradas):
    peligrosas = ['drop', 'delete', 'insert', 'update', '--', ';', '/', '/']
    for entrada in entradas:
        if any(p in entrada.lower() for p in peligrosas):
            return False
    return True

# Validar campos ingresados
def campos_validos(nombre, grado, seccion, edad, validar_edad=True):
    if not nombre or not grado or not seccion or (validar_edad and not edad.isdigit()):
        return False
    return es_entrada_segura(nombre, grado, seccion)

# Insertar un nuevo estudiante
def insertar_estudiante():
    nombre = entry_nombre.get()
    grado = entry_grado.get()
    seccion = entry_seccion.get()
    edad = entry_edad.get()

    if not campos_validos(nombre, grado, seccion, edad):
        messagebox.showwarning("Advertencia", "Datos inválidos o inseguros.")
        return

    try:
        with obtener_conexion() as conn:
            with conn.cursor() as cursor:
                query = "INSERT INTO estudiantes (nombre, grado, seccion, edad) VALUES (%s, %s, %s, %s)"
                cursor.execute(query, (nombre, grado, seccion, int(edad)))
                conn.commit()
        messagebox.showinfo("Éxito", "Estudiante insertado correctamente")
        limpiar_campos()
        actualizar_treeview()
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Actualizar un estudiante existente
def actualizar_estudiante():
    id_ = entry_id.get()
    nombre = entry_nombre.get()
    grado = entry_grado.get()
    seccion = entry_seccion.get()
    edad = entry_edad.get()

    if not id_.isdigit() or not campos_validos(nombre, grado, seccion, edad):
        messagebox.showwarning("Advertencia", "Datos inválidos o inseguros.")
        return

    try:
        with obtener_conexion() as conn:
            with conn.cursor() as cursor:
                query = "UPDATE estudiantes SET nombre = %s, grado = %s, seccion = %s, edad = %s WHERE id = %s"
                cursor.execute(query, (nombre, grado, seccion, int(edad), int(id_)))
                conn.commit()
        messagebox.showinfo("Éxito", f"Estudiante con ID {id_} actualizado")
        limpiar_campos()
        actualizar_treeview()
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Eliminar un estudiante
def eliminar_estudiante():
    id_ = entry_id.get()
    if not id_.isdigit():
        messagebox.showerror("Error", "ID inválido")
        return

    try:
        with obtener_conexion() as conn:
            with conn.cursor() as cursor:
                query = "DELETE FROM estudiantes WHERE id = %s"
                cursor.execute(query, (int(id_),))
                conn.commit()
        messagebox.showinfo("Éxito", f"Estudiante con ID {id_} eliminado")
        limpiar_campos()
        actualizar_treeview()
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Limpiar los campos de entrada
def limpiar_campos():
    entry_id.delete(0, END)
    entry_nombre.delete(0, END)
    entry_grado.delete(0, END)
    entry_seccion.delete(0, END)
    entry_edad.delete(0, END)

# Actualizar el contenido del Treeview con los datos actuales
def actualizar_treeview():
    # Limpiar Treeview
    for item in tree.get_children():
        tree.delete(item)
    try:
        with obtener_conexion() as conn:
            with conn.cursor() as cursor:
                cursor.execute("SELECT * FROM estudiantes")
                for row in cursor.fetchall():
                    tree.insert("", END, values=row)
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Función para cargar datos al seleccionar un registro en el Treeview
def seleccionar_item(event):
    seleccionado = tree.focus()
    if seleccionado:
        valores = tree.item(seleccionado, "values")
        entry_id.delete(0, END)
        entry_id.insert(0, valores[0])
        entry_nombre.delete(0, END)
        entry_nombre.insert(0, valores[1])
        entry_grado.delete(0, END)
        entry_grado.insert(0, valores[2])
        entry_seccion.delete(0, END)
        entry_seccion.insert(0, valores[3])
        entry_edad.delete(0, END)
        entry_edad.insert(0, valores[4])

# Interfaz gráfica con Tkinter
root = Tk()
root.title("Gestión de Estudiantes")
root.geometry("600x500")

# Frame para los campos de entrada
frame_entrada = Frame(root)
frame_entrada.pack(pady=10)

# Etiquetas y entradas
Label(frame_entrada, text="ID (para actualizar/eliminar)").grid(row=0, column=0, padx=5, pady=5, sticky=E)
entry_id = Entry(frame_entrada)
entry_id.grid(row=0, column=1, padx=5, pady=5)

Label(frame_entrada, text="Nombre").grid(row=1, column=0, padx=5, pady=5, sticky=E)
entry_nombre = Entry(frame_entrada)
entry_nombre.grid(row=1, column=1, padx=5, pady=5)

Label(frame_entrada, text="Grado").grid(row=2, column=0, padx=5, pady=5, sticky=E)
entry_grado = Entry(frame_entrada)
entry_grado.grid(row=2, column=1, padx=5, pady=5)

Label(frame_entrada, text="Sección").grid(row=3, column=0, padx=5, pady=5, sticky=E)
entry_seccion = Entry(frame_entrada)
entry_seccion.grid(row=3, column=1, padx=5, pady=5)

Label(frame_entrada, text="Edad").grid(row=4, column=0, padx=5, pady=5, sticky=E)
entry_edad = Entry(frame_entrada)
entry_edad.grid(row=4, column=1, padx=5, pady=5)

# Frame para los botones
frame_botones = Frame(root)
frame_botones.pack(pady=10)

Button(frame_botones, text="Insertar", command=insertar_estudiante, width=15).grid(row=0, column=0, padx=5)
Button(frame_botones, text="Actualizar", command=actualizar_estudiante, width=15).grid(row=0, column=1, padx=5)
Button(frame_botones, text="Eliminar", command=eliminar_estudiante, width=15).grid(row=0, column=2, padx=5)

# Frame para el Treeview (tabla)
frame_tabla = Frame(root)
frame_tabla.pack(pady=10, fill=BOTH, expand=True)

# Configurar Treeview
tree = ttk.Treeview(frame_tabla, columns=("ID", "Nombre", "Grado", "Sección", "Edad"), show="headings")
tree.heading("ID", text="ID")
tree.heading("Nombre", text="Nombre")
tree.heading("Grado", text="Grado")
tree.heading("Sección", text="Sección")
tree.heading("Edad", text="Edad")

tree.column("ID", width=50, anchor=CENTER)
tree.column("Nombre", width=150)
tree.column("Grado", width=80, anchor=CENTER)
tree.column("Sección", width=80, anchor=CENTER)
tree.column("Edad", width=50, anchor=CENTER)

# Agregar scrollbar vertical
scrollbar = Scrollbar(frame_tabla, orient=VERTICAL, command=tree.yview)
tree.configure(yscroll=scrollbar.set)
scrollbar.pack(side=RIGHT, fill=Y)
tree.pack(side=LEFT, fill=BOTH, expand=True)

# Evento para seleccionar un registro y cargarlo en los Entry
tree.bind("<<TreeviewSelect>>", seleccionar_item)

# Cargar datos iniciales en el Treeview
actualizar_treeview()

root.mainloop()
