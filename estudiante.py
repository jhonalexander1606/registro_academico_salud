# se importa la libreria tkinter con todas sus funciones
from tkinter import *
from tkinter import messagebox

# funciones por definir 


ventana_principal = Tk()

# titulo de la ventana
ventana_principal.title("Temperatura 1.0")

# tamaño de la ventana
ventana_principal.geometry("600x500")

# deshabilitar boton de maximizar
ventana_principal.resizable(False, False)

# color de fondo de la ventana
ventana_principal.config(bg="white")

#--------------------------------
# variables globales
#--------------------------------

#imagen de fondo ventana principal
f_vp = PhotoImage(file="img/fondo_ven_p.png")

# frame fondo de la ventana principal

fondo_ventana_prin = Label(ventana_principal, image = f_vp) 
fondo_ventana_prin.place(x= 0, y=0)

#titulo de la ventana principal

titulo = Label(fondo_ventana_prin, text="Registro academico")
titulo.config(bg = "lemon chiffon",fg="black", font=("Helvetica", 20))
titulo.place(x=240,y=10)


# imagen para el frame de notas

fondo_fr_notas = PhotoImage(file="img/fondo_frame_notas.png", width=640 )

#--------------------------------
# frame entrada datos
#--------------------------------

frame_entrada = Label(ventana_principal, image =fondo_fr_notas )
frame_entrada.config(bg="white", width=675, height=180)
frame_entrada.place(x=10, y=60)



# imagenes de fondo



# run
# se ejecuta el metodo mainloop() de la clase Tk() a través de la instancia ventana_principal. Este metodo despliega la ventana en pantalla y queda a la espera de lo que el usuario haga (click en un boton, escribir, etc).  Cada acción del usuario se conoce como un evento.  El método mainloop() es un bucle infinito.
ventana_principal.mainloop()
