from imp import reload
from sqlite3.dbapi2 import OperationalError
from tkinter import *
import tkinter.scrolledtext as scrolledtext # Scroll para area de Comentario.
from tkinter import messagebox # Mensajes en ventana al presionar un boton.
import Conexion
import sys


raiz = Tk()
raiz.title("CRUD")
miFrame = Frame(raiz, width=800, height=800)
miFrame.pack(side=LEFT)

miFrame2 = Frame(raiz, width=800, height=800)
miFrame2.pack(side=TOP, pady=10, padx=5)
miFrame2.config(bd=2)
miFrame2.config(relief="sunken") 

# TODO: Funciones utilizadas

idCrud = BooleanVar()
nombreCrud = StringVar()
apellidoCrud = StringVar()
passwordCrud = StringVar()
comentarioCrud = StringVar()

miCursor = StringVar()
conn = StringVar()

def conectar():
    global miCursor, conn
    conn = Conexion.conexion()
    miCursor = conn.cursor()

def insertarDatos():
    idCrud = idCaja.get()
    if idCrud == "":
        nombreCrud = nombreCaja.get()
        apellidoCrud = apellidoCaja.get()
        passwordCrud = passwordCaja.get()
        comentarioCrud = comentarioCaja.get("1.0", 'end') # Debemos agregar esos datos para obtener la info de esta caja.
        # Para verificar que el comentario no se encuentre vacio, debemos utilizar esta opcion.
        if nombreCrud == "" or apellidoCrud == "" or passwordCrud == "" or not comentarioCrud:
            messagebox.showinfo(title="Campos vacios", message="Debes rellenar todos los campos, con excepcion de la ID", icon="warning")
        else:
            try:
                miCursor.execute("INSERT INTO PERSONA VALUES(NULL, ?, ?, ?, ?)", (nombreCrud, apellidoCrud, passwordCrud, comentarioCrud))
                conn.commit()
                messagebox.showinfo(title='Insercion correcta', message='Los datos han sido insertados correctamente', icon='info')
                limpiarPantalla()
            except NameError:
                messagebox.showinfo(title='Desconectado', message='Debes conectarte a la BD', icon='warning')
            except AttributeError:
                messagebox.showinfo(title='Desconectado', message='Debes conectarte a la BD', icon='warning')
    else:
        print("no podemos insertar :c")
        messagebox.showinfo(title='Quitar ID', message='No debes ingresar una ID para registrar datos.', icon='warning')

def mostrarDatos():
    idCrud = idCaja.get()
    limpiarPantalla()
    try:
        miCursor.execute("SELECT * FROM PERSONA WHERE per_id = {}".format(idCrud))
        datos = miCursor.fetchall()
        print("datos: ", datos)
        if datos:
            for _ , nombre, apellido, password, comentario  in datos:
                nombreCaja.insert(0, nombre)
                apellidoCaja.insert(0, apellido)
                passwordCaja.insert(0, password)
                comentarioCaja.insert("1.0",comentario)
        else:
            messagebox.showinfo(title="Usuario no encontrado", message="No se ha logrado encontrar al usuario buscado", icon="info")
    except:
        messagebox.showinfo(title='Desconectado', message='Debes conectarte a la BD', icon='warning')
        limpiarPantalla()

def actualizarDatos():
    idCrud = idCaja.get()
    try:
        try:
            miCursor.execute("SELECT per_id FROM PERSONA WHERE per_id = {}".format(idCrud))
            datos = miCursor.fetchall()
        except OperationalError:
            messagebox.showinfo(title="Usuario no encontrado", message="No se ha logrado encontrar al usuario buscado, recuerda agregar la id del usuario a modificar.", icon="info")
        nombreCrud = nombreCaja.get()
        apellidoCrud = apellidoCaja.get()
        passwordCrud = passwordCaja.get()
        comentarioCrud = comentarioCaja.get("1.0", 'end')
        if idCrud != "":
            try:
                miCursor.execute("UPDATE PERSONA SET per_nombre = ?, per_apellido = ?, per_password = ?, per_comentario = ? WHERE per_id = {}".format(datos[0][0]), (nombreCrud, apellidoCrud, passwordCrud, comentarioCrud))
                conn.commit()
                messagebox.showinfo(title="Usuario Modificado", message="Se han modificado correctamente los datos", icon="info")
            except IndexError:
                messagebox.showinfo(title="Usuario no encontrado", message="No se ha logrado encontrar al usuario buscado", icon="info")
    except AttributeError:
        messagebox.showinfo(title='Desconectado', message='Debes conectarte a la BD', icon='warning')

def eliminarRegistro():
    
    idCrud = idCaja.get()
    try:
        try:
            miCursor.execute("SELECT per_id FROM PERSONA WHERE per_id = {}".format(idCrud))
            datos = miCursor.fetchall()
        except OperationalError:
            messagebox.showinfo(title="Usuario no encontrado", message="No se ha logrado encontrar al usuario buscado, recuerda agregar la id del usuario a eliminar.", icon="info")
        if idCrud != "":
            try:
                miCursor.execute("DELETE FROM PERSONA WHERE per_id = {}".format(datos[0][0]))
                conn.commit()
                messagebox.showinfo(title="Usuario Eliminado", message="Se ha eliminado correctamente al usuario", icon="info")
            except IndexError:
                messagebox.showinfo(title="Usuario no encontrado", message="No se ha logrado encontrar al usuario buscado", icon="info")
            finally:
                limpiarPantalla()
    except AttributeError:
        messagebox.showinfo(title='Desconectado', message='Debes conectarte a la BD', icon='warning')

def limpiarPantalla():
    nombreCaja.delete(0, END)
    apellidoCaja.delete(0, END)
    passwordCaja.delete(0, END)
    comentarioCaja.delete("1.0", END)

def mensajeCreador():
    messagebox.showinfo(title='¡Hola Mundo!', message='Creado por: Cristian Soto \n Contacto: crisandru1997@gmail.com', icon='info')

def mensajerVersion():
    messagebox.showinfo(title='Version', message='La versión de este software es 1.0', icon='info')

def terminarPrograma():
    sys.exit()

# TODO: Barra del Menu
miMenu = Menu(raiz)
raiz.config(menu=miMenu)

# Primer Menu - BBDD
archivoBBDD = Menu(miMenu, tearoff=0)
archivoBBDD.add_command(label="Conexion", command=conectar)
archivoBBDD.add_command(label="Salir", command=terminarPrograma)

# Segundo Menu - Borrar
archivoBorrar = Menu(miMenu, tearoff=0)
archivoBorrar.add_command(label="Borrar campos", command=limpiarPantalla)

# Tercer Menu - CRUD
archivoCRUD = Menu(miMenu, tearoff=0)
archivoCRUD.add_command(label="Crear", command=insertarDatos)
archivoCRUD.add_command(label="Leer", command=mostrarDatos)
archivoCRUD.add_command(label="Actualizar", command=actualizarDatos)
archivoCRUD.add_command(label="Borrar", command=eliminarRegistro)

# Cuarto Menu - Ayuda
archivoAyuda = Menu(miMenu, tearoff=0)
archivoAyuda.add_command(label="Creador", command=mensajeCreador)
archivoAyuda.add_command(label="Version", command=mensajerVersion)

miMenu.add_cascade(label="BBDD", menu=archivoBBDD)
miMenu.add_cascade(label="Borrar", menu=archivoBorrar)
miMenu.add_cascade(label="CRUD", menu=archivoCRUD)
miMenu.add_cascade(label="Ayuda", menu=archivoAyuda)

# TODO: Campo de ID
idLabel = Label(miFrame, text="ID")
idLabel.grid(row=0, column=0, sticky="w", pady=10, padx=10)
idCaja = Entry(miFrame)
idCaja.grid(row=0, column=1, pady=10, columnspan=4, padx=10)

# TODO: Campo de NOMBRE
nombreLabel = Label(miFrame, text="Nombre")
nombreLabel.grid(row=1, column=0, sticky="w", pady=10, padx=10)
nombreCaja = Entry(miFrame)
nombreCaja.grid(row=1, column=1, pady=10, columnspan=4, padx=10)

# TODO: Campo de APELLIDO
apellidoLabel = Label(miFrame, text="Apellido")
apellidoLabel.grid(row=2, column=0, sticky="w", pady=10, padx=10)
apellidoCaja = Entry(miFrame)
apellidoCaja.grid(row=2, column=1, pady=10, columnspan=4, padx=10)

# TODO: Campo de CONTRASEÑA
passwordLabel = Label(miFrame, text="Contraseña")
passwordLabel.grid(row=3, column=0, sticky="w", pady=10, padx=10)
passwordCaja = Entry(miFrame, show="*")
passwordCaja.grid(row=3, column=1, pady=10, columnspan=4, padx=10)

# TODO: Campo de COMENTARIO
comentarioLabel = Label(miFrame, text="Comentario")
comentarioLabel.grid(row=4, column=0, sticky="w", pady=10, padx=10)
comentarioCaja = scrolledtext.ScrolledText(miFrame)
comentarioCaja.config(width=23, height=5)
comentarioCaja.grid(row=4, column=1, pady=10, columnspan=4, padx=10)

# TODO: BOTONES

botonCreate = Button(miFrame, text="CREAR", padx=15, pady=10, command=insertarDatos)
botonCreate.grid(row=5, column=0, padx=10, pady=20)

botonRead = Button(miFrame, text="LEER", padx=15, pady=10, command=mostrarDatos)
botonRead.grid(row=5, column=1, padx=10, pady=20)

botonUpdate = Button(miFrame, text="ACTUALIZAR", padx=15, pady=10, command=actualizarDatos)
botonUpdate.grid(row=5, column=3, padx=10, pady=20)

botonDelete = Button(miFrame, text="BORRAR", padx=15, pady=10, command=eliminarRegistro)
botonDelete.grid(row=5, column=4, padx=10, pady=20)


# asdsa
id_mostrar_label = Label(miFrame2, text="ID")
id_mostrar_label.grid(row=0, column=6, sticky="w", pady=10, padx=25)

nombre_mostrar_label = Label(miFrame2, text="Nombre")
nombre_mostrar_label.grid(row=0, column=8, sticky="w", pady=10, padx=50)

apellido_mostrar_label = Label(miFrame2, text="Apellido")
apellido_mostrar_label.grid(row=0, column=10, sticky="w", pady=10, padx=50)

contrasena_mostrar_label = Label(miFrame2, text="Contraseña")
contrasena_mostrar_label.grid(row=0, column=12, sticky="w", pady=10, padx=50)

comentario_mostrar_label = Label(miFrame2, text="Comentario")
comentario_mostrar_label.grid(row=0, column=14, sticky="w", pady=10, padx=50)

def ListadoDatos():
    conectar()
    try:
        miCursor.execute("SELECT * FROM PERSONA")
        datos = miCursor.fetchall()
        print("datos: ", datos)
        i = 1
        if datos:
            for dato in datos:
                nombre_mostrar_label = Label(miFrame2, text=dato[0])
                nombre_mostrar_label.grid(row=i, column=6, sticky="w", pady=0, padx=25)
                nombre_mostrar_label = Label(miFrame2, text=dato[1])
                nombre_mostrar_label.grid(row=i, column=8, sticky="w", pady=0, padx=50)
                apellido_mostrar_label = Label(miFrame2, text=dato[2])
                apellido_mostrar_label.grid(row=i, column=10, sticky="w", pady=0, padx=50)
                contrasena_mostrar_label = Label(miFrame2, text=dato[3])
                contrasena_mostrar_label.grid(row=i, column=12, sticky="w", pady=0, padx=50)
                comentario_mostrar_label = Label(miFrame2, text=dato[4])
                comentario_mostrar_label.grid(row=i, column=14, sticky="w", pady=0, padx=50)
                i = i + 1
        else:
            messagebox.showinfo(title="Usuario no encontrado", message="No se ha logrado encontrar al usuario buscado", icon="info")
    except:
        messagebox.showinfo(title='Desconectado', message='Debes conectarte a la BD', icon='warning')
        limpiarPantalla()
        
ListadoDatos()

raiz.mainloop()