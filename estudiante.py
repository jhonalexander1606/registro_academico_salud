# se importa la libreria tkinter con todas sus funciones
from tkinter import *
from tkinter import messagebox
import tkinter as tk
# funciones por definir 

ventana_principal = tk.Tk()

# titulo de la ventana
ventana_principal.title("regisgtro")

# tamaño de la ventana
ventana_principal.geometry("600x600")

# deshabilitar boton de maximizar
ventana_principal.resizable(False, False)

# color de fondo de la ventana
ventana_principal.config(bg="white")

#cambio del icono de la ventana principal 
icon = tk.PhotoImage(file="img/logo_uis.png")
ventana_principal.iconphoto(True, icon) 

#--------------------------------
# variables globales
#--------------------------------

#imagen de fondo ventana principal
f_vp = PhotoImage(file="img/fondo_ven_p.png")

# fondo de la ventana principal

fondo_ventana_prin = Label(ventana_principal, image = f_vp) 
fondo_ventana_prin.place(x= 0, y=0)

#titulo de la ventana principal

titulo_n = Label(fondo_ventana_prin, text="Registro academico")
titulo_n.config(bg = "lavender blush",fg="black", font=("Helvetica", 20))
titulo_n.place(x=50,y=10)

# imagen para el label de notas

fondo_lb_notas = PhotoImage(file="img/fondo_frame_notas.png" )

#--------------------------------
# label entrada datos
#--------------------------------

label_entrada = Label(ventana_principal, image =fondo_lb_notas )
label_entrada.config(bg="white", width=575, height=215)
label_entrada.place(x=10, y=60)


#imagene del label de notas

nota_i= PhotoImage(file = "img/notas.png") 
label_logo = Label(label_entrada, image = nota_i)
label_logo.place(x= 30, y = 15)
# imagenes de fondo

# titulo del registro salud
titulo_n = Label(fondo_ventana_prin, text="Registro medico")
titulo_n.config(bg = "lavender blush",fg="black", font=("Helvetica", 20))
titulo_n.place(x=50,y=290)

# imagen para el label de la salud





# run
# se ejecuta el metodo mainloop() de la clase Tk() a través de la instancia ventana_principal. Este metodo despliega la ventana en pantalla y queda a la espera de lo que el usuario haga (click en un boton, escribir, etc).  Cada acción del usuario se conoce como un evento.  El método mainloop() es un bucle infinito.
ventana_principal.mainloop()
