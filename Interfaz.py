from tkinter import *
import tkinter.scrolledtext as scrolledtext # Scroll para area de Comentario.
from tkinter import messagebox # Mensajes en ventana al presionar un boton.

raiz = Tk()
raiz.title("CRUD")
miFrame = Frame(raiz, width=800, height=800)
miFrame.pack()

# TODO: Barra del Menu
miMenu = Menu(raiz)
raiz.config(menu=miMenu)

# Primer Menu - BBDD
archivoBBDD = Menu(miMenu, tearoff=0)
archivoBBDD.add_command(label="Conexion")
archivoBBDD.add_command(label="Salir")

# Segundo Menu - Borrar
archivoBorrar = Menu(miMenu, tearoff=0)
archivoBorrar.add_command(label="Borrar campos")

# Tercer Menu - CRUD
archivoCRUD = Menu(miMenu, tearoff=0)
archivoCRUD.add_command(label="Crear")
archivoCRUD.add_command(label="Leer")
archivoCRUD.add_command(label="Actualizar")
archivoCRUD.add_command(label="Borrar")

# Cuarto Menu - Ayuda
archivoAyuda = Menu(miMenu, tearoff=0)
archivoAyuda.add_command(label="Creador")
archivoAyuda.add_command(label="Version")

miMenu.add_cascade(label="BBDD", menu=archivoBBDD)
miMenu.add_cascade(label="Borrar", menu=archivoBorrar)
miMenu.add_cascade(label="CRUD", menu=archivoCRUD)
miMenu.add_cascade(label="Ayuda", menu=archivoAyuda)

# TODO: Campo de ID
idLabel = Label(miFrame, text="ID")
idLabel.grid(row=0, column=0, sticky="w", pady=10)
idCaja = Entry(miFrame)
idCaja.grid(row=0, column=1, pady=10, columnspan=4)

# TODO: Campo de NOMBRE
nombreLabel = Label(miFrame, text="Nombre")
nombreLabel.grid(row=1, column=0, sticky="w", pady=10)
nombreCaja = Entry(miFrame)
nombreCaja.grid(row=1, column=1, pady=10, columnspan=4)

# TODO: Campo de APELLIDO
apellidoLabel = Label(miFrame, text="Apellido")
apellidoLabel.grid(row=2, column=0, sticky="w", pady=10)
apellidoCaja = Entry(miFrame)
apellidoCaja.grid(row=2, column=1, pady=10, columnspan=4)

# TODO: Campo de CONTRASEÑA
passwordLabel = Label(miFrame, text="Contraseña")
passwordLabel.grid(row=3, column=0, sticky="w", pady=10)
passwordCaja = Entry(miFrame, show="*")
passwordCaja.grid(row=3, column=1, pady=10, columnspan=4)

# TODO: Campo de COMENTARIO
comentarioLabel = Label(miFrame, text="Comentario")
comentarioLabel.grid(row=4, column=0, sticky="w", pady=10)
comentarioCaja = scrolledtext.ScrolledText(miFrame)
comentarioCaja.config(width=23, height=5)
comentarioCaja.grid(row=4, column=1, pady=10, columnspan=4)

# TODO: BOTONES

botonCreate = Button(miFrame, text="CREAR", padx=10, pady=10)
botonCreate.grid(row=5, column=0, padx=0)

botonRead = Button(miFrame, text="LEER", padx=10, pady=10)
botonRead.grid(row=5, column=1, padx=0)

botonUpdate = Button(miFrame, text="ACTUALIZAR", padx=10, pady=10)
botonUpdate.grid(row=5, column=3, padx=6)

botonDelete = Button(miFrame, text="BORRAR", padx=10, pady=10)
botonDelete.grid(row=5, column=4)

raiz.mainloop()