# se importa la libreria tkinter con todas sus funciones
from tkinter import *
from tkinter import messagebox
import tkinter as tk

def abrir_toplevel_notas_calculo1():
    global toplevel_notas_calculo
    toplevel_notas_calculo = Toplevel()
    toplevel_notas_calculo.title("Promedio notas")
    toplevel_notas_calculo.resizable(False, False)
    toplevel_notas_calculo.geometry("600x300")
    toplevel_notas_calculo.config(bg="white")

    #fondo del top level de calculo
    ln_fondo = Label(toplevel_notas_calculo, image=fondo_top_calculo)
    ln_fondo.place(x=0,y=0)

    # logo de la app
    lb_logo_n = Label(toplevel_notas_calculo, image=logo_top_calculo, bg="white")
    lb_logo_n.place(x=20,y=50)

    # titulo de las notas de quimica
    lb_titulo_calculo=Label(toplevel_notas_calculo,text="Notas Semestre")
    lb_titulo_calculo.config(bg="misty rose", fg="black", font=("Helvetica", 18))
    lb_titulo_calculo.place(x=280,y=10)

    # etiqueta para valor corte 1
    lb_c = Label(toplevel_notas_calculo, text = "corte 1 = ",)
    lb_c.config(bg="light gray", fg="black", font=("Helvetica", 18))
    lb_c.place(x=260, y=60)

    # caja de texto para corte 1
    entry_c = Entry(toplevel_notas_calculo, textvariable=nota_1_calculo)
    entry_c.config(bg="light gray", fg="blue", font=("Times New Roman", 18), width=6)
    entry_c.focus_set()
    entry_c.place(x=400,y=60)

    # etiqueta para valor corte 2
    lb_c = Label(toplevel_notas_calculo, text = "corte 2 = ")
    lb_c.config(bg="light gray", fg="black", font=("Helvetica", 18))
    lb_c.place(x=260, y=110)

    # caja de texto para corte 2
    entry_c = Entry(toplevel_notas_calculo, textvariable=nota_2_calculo)
    entry_c.config(bg="light gray", fg="blue", font=("Times New Roman", 18), width=6)
    entry_c.place(x=400,y=110)

    # etiqueta para valor corte 3
    lb_c = Label(toplevel_notas_calculo, text = "corte 3 = ")
    lb_c.config(bg="light gray", fg="black", font=("Helvetica", 18))
    lb_c.place(x=260, y=160)

    # caja de texto para corte 3
    entry_c = Entry(toplevel_notas_calculo, textvariable=nota_3_calculo)
    entry_c.config(bg="light gray", fg="blue", font=("Times New Roman", 18), width=6)
    entry_c.place(x=400,y=160)

    # etiqueta para valor corte 4
    lb_c = Label(toplevel_notas_calculo, text = "corte 4 = ")
    lb_c.config(bg="light gray", fg="black", font=("Helvetica", 18))
    lb_c.place(x=260, y=210)

    # caja de texto para corte 4
    entry_c = Entry(toplevel_notas_calculo, textvariable=nota_4_calculo)
    entry_c.config(bg="light gray", fg="blue", font=("Times New Roman", 18), width=6)
    entry_c.place(x=400,y=210)

    # boton de calcular_ calculo 1
    bt_calcular = Button(toplevel_notas_calculo, text="aceptar",command=aceptar_c)
    bt_calcular.place(x=390, y=250, width=90,height= 40)
    bt_calcular.config(bg = "lavenderblush2")

def aceptar_c():
    global n1_c,n2_c,n3_c,n4_c
    global nf_c
    n1_c = int(nota_1_calculo.get())
    n2_c = int(nota_2_calculo.get())
    n3_c = int(nota_3_calculo.get())
    n4_c = int(nota_4_calculo.get())

    toplevel_notas_calculo.destroy()

def abrir_toplevel_notas_quimica():
    global toplevel_notas_quimica
    toplevel_notas_quimica = Toplevel()
    toplevel_notas_quimica.title("Promedio notas")
    toplevel_notas_quimica.resizable(False, False)
    toplevel_notas_quimica.geometry("600x300")
    toplevel_notas_quimica.config(bg="white")

    #fondo del top level de quimica
    ln_fondo = Label(toplevel_notas_quimica, image=fondo_top_quimica)
    ln_fondo.place(x=0,y=0)

    # logo de la app
    lb_logo_n = Label(toplevel_notas_quimica, image=logo_top_quimica, bg="white")
    lb_logo_n.place(x=20,y=50)

    # titulo de las notas de quimica
    lb_titulo_quimica=Label(toplevel_notas_quimica,text="Notas Semestre")
    lb_titulo_quimica.config(bg="misty rose", fg="black", font=("Helvetica", 18))
    lb_titulo_quimica.place(x=280,y=10)

    # etiqueta para valor corte 1
    lb_c = Label(toplevel_notas_quimica, text = "corte 1 = ",)
    lb_c.config(bg="light gray", fg="black", font=("Helvetica", 18))
    lb_c.place(x=260, y=60)

    # caja de texto para corte 1
    entry_c = Entry(toplevel_notas_quimica, textvariable=nota_1_quimica)
    entry_c.config(bg="light gray", fg="blue", font=("Times New Roman", 18), width=6)
    entry_c.focus_set()
    entry_c.place(x=400,y=60)

    # etiqueta para valor corte 2
    lb_c = Label(toplevel_notas_quimica, text = "corte 2 = ")
    lb_c.config(bg="light gray", fg="black", font=("Helvetica", 18))
    lb_c.place(x=260, y=110)

    # caja de texto para corte 2
    entry_c = Entry(toplevel_notas_quimica, textvariable=nota_2_quimica)
    entry_c.config(bg="light gray", fg="blue", font=("Times New Roman", 18), width=6)
    entry_c.place(x=400,y=110)

    # etiqueta para valor corte 3
    lb_c = Label(toplevel_notas_quimica, text = "corte 3 = ")
    lb_c.config(bg="light gray", fg="black", font=("Helvetica", 18))
    lb_c.place(x=260, y=160)

    # caja de texto para corte 3
    entry_c = Entry(toplevel_notas_quimica, textvariable=nota_3_quimica)
    entry_c.config(bg="light gray", fg="blue", font=("Times New Roman", 18), width=6)
    entry_c.place(x=400,y=160)

    # etiqueta para valor corte 4
    lb_c = Label(toplevel_notas_quimica, text = "corte 4 = ")
    lb_c.config(bg="light gray", fg="black", font=("Helvetica", 18))
    lb_c.place(x=260, y=210)

    # caja de texto para corte 4
    entry_c = Entry(toplevel_notas_quimica, textvariable=nota_4_quimica)
    entry_c.config(bg="light gray", fg="blue", font=("Times New Roman", 18), width=6)
    entry_c.place(x=400,y=210)

    # boton de calcular_ calculo 1
    bt_calcular = Button(toplevel_notas_quimica, text="aceptar", command=aceptar_q)
    bt_calcular.place(x=390, y=250, width=90,height= 40)
    bt_calcular.config(bg = "lavenderblush2")

def aceptar_q():
    global n1_q,n2_q,n3_q,n4_q
    global nf_q
    n1_q = int(nota_1_quimica.get())
    n2_q = int(nota_2_quimica.get())
    n3_q = int(nota_3_quimica.get())
    n4_q = int(nota_4_quimica.get())

    toplevel_notas_quimica.destroy()

def abrir_toplevel_notas_programacion():
    global toplevel_notas_programacion
    toplevel_notas_programacion = Toplevel()
    toplevel_notas_programacion.title("Promedio notas")
    toplevel_notas_programacion.resizable(False, False)
    toplevel_notas_programacion.geometry("600x300")
    toplevel_notas_programacion.config(bg="white")

    #fondo del top level de quimica
    ln_fondo = Label(toplevel_notas_programacion, image=fondo_top_programacion)
    ln_fondo.place(x=0,y=0)

    # logo de la app
    lb_logo_n = Label(toplevel_notas_programacion, image=logo_top_programacion, bg="white")
    lb_logo_n.place(x=20,y=50)

    # titulo de las notas de quimica
    lb_titulo_quimica=Label(toplevel_notas_programacion,text="Notas Semestre")
    lb_titulo_quimica.config(bg="misty rose", fg="black", font=("Helvetica", 18))
    lb_titulo_quimica.place(x=280,y=10)

    # etiqueta para valor corte 1
    lb_c = Label(toplevel_notas_programacion, text = "corte 1 = ",)
    lb_c.config(bg="light gray", fg="black", font=("Helvetica", 18))
    lb_c.place(x=260, y=60)

    # caja de texto para corte 1
    entry_c = Entry(toplevel_notas_programacion, textvariable=nota_1_programacion)
    entry_c.config(bg="light gray", fg="blue", font=("Times New Roman", 18), width=6)
    entry_c.focus_set()
    entry_c.place(x=400,y=60)

    # etiqueta para valor corte 2
    lb_c = Label(toplevel_notas_programacion, text = "corte 2 = ")
    lb_c.config(bg="light gray", fg="black", font=("Helvetica", 18))
    lb_c.place(x=260, y=110)

    # caja de texto para corte 2
    entry_c = Entry(toplevel_notas_programacion, textvariable=nota_2_programacion)
    entry_c.config(bg="light gray", fg="blue", font=("Times New Roman", 18), width=6)
    entry_c.place(x=400,y=110)

    # etiqueta para valor corte 3
    lb_c = Label(toplevel_notas_programacion, text = "corte 3 = ")
    lb_c.config(bg="light gray", fg="black", font=("Helvetica", 18))
    lb_c.place(x=260, y=160)

    # caja de texto para corte 3
    entry_c = Entry(toplevel_notas_programacion, textvariable=nota_3_programacion)
    entry_c.config(bg="light gray", fg="blue", font=("Times New Roman", 18), width=6)
    entry_c.place(x=400,y=160)

    # etiqueta para valor corte 4
    lb_c = Label(toplevel_notas_programacion, text = "corte 4 = ")
    lb_c.config(bg="light gray", fg="black", font=("Helvetica", 18))
    lb_c.place(x=260, y=210)

    # caja de texto para corte 4
    entry_c = Entry(toplevel_notas_programacion, textvariable=nota_4_programacion)
    entry_c.config(bg="light gray", fg="blue", font=("Times New Roman", 18), width=6)
    entry_c.place(x=400,y=210)

    # boton de calcular_ programacion
    bt_calcular = Button(toplevel_notas_programacion, text="aceptar", command=aceptar_p)
    bt_calcular.place(x=390, y=250, width=90,height= 40)
    bt_calcular.config(bg = "lavenderblush2")

def aceptar_p():
    global n1_p,n2_p,n3_p,n4_p
    global nf_p
    n1_p = int(nota_1_programacion.get())
    n2_p = int(nota_2_programacion.get())
    n3_p = int(nota_3_programacion.get())
    n4_p = int(nota_4_programacion.get())

    toplevel_notas_programacion.destroy()


def boton_calcular_n():
    t_resultados_n.delete("1.0","end")
    if q.get()== 1 :
        nf_q =(n1_q+n2_q+n3_q+n4_q)/4
        t_resultados_n.insert(INSERT,f"Quimica= {nf_q}")

    if c.get()== 1:
        nf_c=(n1_c+n2_c+n3_c+n4_c)/4
        t_resultados_n.insert(INSERT,f"\nCalculo 1= {nf_c}")
    
    if p.get()== 1:
        nf_p=(n1_p+n2_p+n3_p+n4_p)/4
        t_resultados_n.insert(INSERT,f"\nProgramacion= {nf_p}")

    if q.get()==0 and c.get()==0 and p.get()==0:
        t_resultados_n.insert(INSERT,"debe escoger almenos una opcion")
    

def boton_borrar_n():
        messagebox.showinfo("Registro notas", "Los datos serán borrados")
        b.set("")
        t_resultados_n.delete("1.0","end")

# ventana principal
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
nota_1_quimica = StringVar()
nota_2_quimica = StringVar()
nota_3_quimica = StringVar()
nota_4_quimica = StringVar()
nf_q = StringVar()
q = IntVar()
c = IntVar()
p = IntVar()
nota_1_calculo = StringVar()
nota_2_calculo = StringVar()
nota_3_calculo = StringVar()
nota_4_calculo = StringVar()
nf_c= StringVar()
nota_1_programacion = StringVar()
nota_2_programacion = StringVar()
nota_3_programacion = StringVar()
nota_4_programacion = StringVar()
nf_p= StringVar()

b=StringVar()




#---------------------------------------------------------------------------

#fondo de top level de programacion

fondo_top_programacion = PhotoImage(file="img/fondo_top_programacion.png")


# fondo de toplevel de quimica
fondo_top_quimica=PhotoImage(file="img/fondo_top_quimica.png")

#fondo de toplevel de calculo

fondo_top_calculo=PhotoImage(file="img/fondo_top_calculo.png")

#

#imagen de fondo ventana principal
f_vp = PhotoImage(file="img/fondo_ven_p.png")

#imagen de top level de quimica

logo_top_quimica = PhotoImage(file="img/logo_quimica.png")

#logo de toplevel de calculo

logo_top_calculo = PhotoImage(file="img/logo_calculo.png")

# logo de top level de programación

logo_top_programacion = PhotoImage(file="img/logo_programacion.png")


# fondo de la ventana principal

fondo_ventana_prin = Label(ventana_principal, image = f_vp) 
fondo_ventana_prin.place(x= 0, y=0)

#titulo del registro academico

titulo_n = Label(fondo_ventana_prin, text="Registro academico")
titulo_n.config(bg = "blanched almond",fg="black", font=("Helvetica", 20))
titulo_n.place(x=20,y=10)

# imagen para el label de notas

fondo_lb_notas = PhotoImage(file="img/fondo_frame_notas.png" )

#--------------------------------
# label entrada datos
#--------------------------------

label_entrada = Label(ventana_principal, image =fondo_lb_notas )
label_entrada.config(bg="white", width=575, height=215)
label_entrada.place(x=10, y=90)


#logo del label de notas
nota_i= PhotoImage(file = "img/notas.png") 
label_logo = Label(label_entrada, image = nota_i)
label_logo.place(x= 8, y = 15)

# boton de label de notas de QUIMICA
bt_notas = Button(fondo_ventana_prin, text="Quimica", command=abrir_toplevel_notas_quimica)
bt_notas.place(x=280, y=10, width=80,height= 30)
bt_notas.config(bg = "peach puff")

# boton de label de notas de CALCULO 1
bt_notas = Button(fondo_ventana_prin, text="Calculo-1", command=abrir_toplevel_notas_calculo1)
bt_notas.place(x=380, y=10, width=80,height= 30)
bt_notas.config(bg = "peach puff")

#boton de label de notas de programacion
bt_notas = Button(fondo_ventana_prin, text="Programación", command=abrir_toplevel_notas_programacion)
bt_notas.place(x=480,y=10,width=80,height=30)
bt_notas.config(bg = "peach puff")

# titulo del registro salud
titulo_n = Label(fondo_ventana_prin, text="Registro medico")
titulo_n.config(bg = "lavender blush",fg="black", font=("Helvetica", 20))
titulo_n.place(x=20,y=320)

# imagen para el label de la salud

fondo_lb_salud = PhotoImage(file="img/fondo_label_salud.png" )

# label de entrada de salud

label_entrada_s = Label(ventana_principal, image= fondo_lb_salud )
label_entrada_s.config(bg="white", width=575, height=215)
label_entrada_s.place(x=10, y=360)

# logo del label de la salud

salud_i= PhotoImage(file = "img/salud.png") 
label_logo = Label(label_entrada_s, image = salud_i)
label_logo.place(x= 8, y = 15)
label_logo.config(bg= "light blue1")


#imagen para el label de texto


# titulo de notas final de semestre
titulo_n_f= Label(label_entrada, text="Notas Finales")
titulo_n_f.config(bg = "lightcyan2",fg="black", font=("Helvetica", 20))
titulo_n_f.place(x=385,y=10)

#cuadro de respuesta

t_resultados_n= Text(label_entrada)
t_resultados_n.config(bg="antiquewhite2", fg="gray1", font=("times new roman",15))
t_resultados_n.place(x=381,y=56,width=180,height=140)

# boton de calcular

bt_calcular_n = Button(label_entrada, text="calcular",command=boton_calcular_n)
bt_calcular_n.place(x=250, y=10, width=90,height= 40)
bt_calcular_n.config(bg = "darkolivegreen3",font=("Helvetica", 15))

# checkbutton de eleccion de quimica

cb_k = Checkbutton(label_entrada, text="Quimica",variable=q)
cb_k.config(bg="cadetblue2", fg="black", font=("Helvetica", 13))
cb_k.place(x=223, y=53)

# checkbutton de eleccion de calculo-1

cb_k = Checkbutton(label_entrada, text="Calculo-1",variable=c)
cb_k.config(bg="red3", fg="black", font=("Helvetica", 13))
cb_k.place(x=223, y=89)

cb_k = Checkbutton(label_entrada, text="Programacion",variable=p)
cb_k.config(bg="royalblue3", fg="black", font=("Helvetica", 13))
cb_k.place(x=223, y=124)

bt_borrar = Button(label_entrada, text="Borrar",command=boton_borrar_n)
bt_borrar.config(bg="light steel blue",fg= "black", font=("helvetica", 15) )
bt_borrar.place(x=250,y=160, width=80, height=35)

# run 
ventana_principal.mainloop()
