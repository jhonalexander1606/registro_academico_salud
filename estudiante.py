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
    entry_c.config(bg="light gray", fg="black", font=("Times New Roman", 18), width=6)
    entry_c.focus_set()
    entry_c.place(x=400,y=60)

    # etiqueta para valor corte 2
    lb_c = Label(toplevel_notas_calculo, text = "corte 2 = ")
    lb_c.config(bg="light gray", fg="black", font=("Helvetica", 18))
    lb_c.place(x=260, y=110)

    # caja de texto para corte 2
    entry_c = Entry(toplevel_notas_calculo, textvariable=nota_2_calculo)
    entry_c.config(bg="light gray", fg="black", font=("Times New Roman", 18), width=6)
    entry_c.place(x=400,y=110)

    # etiqueta para valor corte 3
    lb_c = Label(toplevel_notas_calculo, text = "corte 3 = ")
    lb_c.config(bg="light gray", fg="black", font=("Helvetica", 18))
    lb_c.place(x=260, y=160)

    # caja de texto para corte 3
    entry_c = Entry(toplevel_notas_calculo, textvariable=nota_3_calculo)
    entry_c.config(bg="light gray", fg="black", font=("Times New Roman", 18), width=6)
    entry_c.place(x=400,y=160)

    # etiqueta para valor corte 4
    lb_c = Label(toplevel_notas_calculo, text = "corte 4 = ")
    lb_c.config(bg="light gray", fg="black", font=("Helvetica", 18))
    lb_c.place(x=260, y=210)

    # caja de texto para corte 4
    entry_c = Entry(toplevel_notas_calculo, textvariable=nota_4_calculo)
    entry_c.config(bg="light gray", fg="black", font=("Times New Roman", 18), width=6)
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
    entry_c.config(bg="light gray", fg="black", font=("Times New Roman", 18), width=6)
    entry_c.focus_set()
    entry_c.place(x=400,y=60)

    # etiqueta para valor corte 2
    lb_c = Label(toplevel_notas_quimica, text = "corte 2 = ")
    lb_c.config(bg="light gray", fg="black", font=("Helvetica", 18))
    lb_c.place(x=260, y=110)

    # caja de texto para corte 2
    entry_c = Entry(toplevel_notas_quimica, textvariable=nota_2_quimica)
    entry_c.config(bg="light gray", fg="black", font=("Times New Roman", 18), width=6)
    entry_c.place(x=400,y=110)

    # etiqueta para valor corte 3
    lb_c = Label(toplevel_notas_quimica, text = "corte 3 = ")
    lb_c.config(bg="light gray", fg="black", font=("Helvetica", 18))
    lb_c.place(x=260, y=160)

    # caja de texto para corte 3
    entry_c = Entry(toplevel_notas_quimica, textvariable=nota_3_quimica)
    entry_c.config(bg="light gray", fg="black", font=("Times New Roman", 18), width=6)
    entry_c.place(x=400,y=160)

    # etiqueta para valor corte 4
    lb_c = Label(toplevel_notas_quimica, text = "corte 4 = ")
    lb_c.config(bg="light gray", fg="black", font=("Helvetica", 18))
    lb_c.place(x=260, y=210)

    # caja de texto para corte 4
    entry_c = Entry(toplevel_notas_quimica, textvariable=nota_4_quimica)
    entry_c.config(bg="light gray", fg="black", font=("Times New Roman", 18), width=6)
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
    entry_c.config(bg="light gray", fg="black", font=("Times New Roman", 18), width=6)
    entry_c.focus_set()
    entry_c.place(x=400,y=60)

    # etiqueta para valor corte 2
    lb_c = Label(toplevel_notas_programacion, text = "corte 2 = ")
    lb_c.config(bg="light gray", fg="black", font=("Helvetica", 18))
    lb_c.place(x=260, y=110)

    # caja de texto para corte 2
    entry_c = Entry(toplevel_notas_programacion, textvariable=nota_2_programacion)
    entry_c.config(bg="light gray", fg="black", font=("Times New Roman", 18), width=6)
    entry_c.place(x=400,y=110)

    # etiqueta para valor corte 3
    lb_c = Label(toplevel_notas_programacion, text = "corte 3 = ")
    lb_c.config(bg="light gray", fg="black", font=("Helvetica", 18))
    lb_c.place(x=260, y=160)

    # caja de texto para corte 3
    entry_c = Entry(toplevel_notas_programacion, textvariable=nota_3_programacion)
    entry_c.config(bg="light gray", fg="black", font=("Times New Roman", 18), width=6)
    entry_c.place(x=400,y=160)

    # etiqueta para valor corte 4
    lb_c = Label(toplevel_notas_programacion, text = "corte 4 = ")
    lb_c.config(bg="light gray", fg="black", font=("Helvetica", 18))
    lb_c.place(x=260, y=210)

    # caja de texto para corte 4
    entry_c = Entry(toplevel_notas_programacion, textvariable=nota_4_programacion)
    entry_c.config(bg="light gray", fg="black", font=("Times New Roman", 18), width=6)
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


# top level de algebra

def abrir_toplevel_notas_algebra():
    global toplevel_notas_algebra
    toplevel_notas_algebra = Toplevel()
    toplevel_notas_algebra.title("Promedio notas")
    toplevel_notas_algebra.resizable(False, False)
    toplevel_notas_algebra.geometry("600x300")
    toplevel_notas_algebra.config(bg="white")

    #fondo del top level de algebra
    ln_fondo = Label(toplevel_notas_algebra, image=fondo_top_algebra)
    ln_fondo.place(x=0,y=0)

    # logo de la app
    lb_logo_n = Label(toplevel_notas_algebra, image=logo_top_algebra, bg="white")
    lb_logo_n.place(x=20,y=50)

    # titulo de las notas de algebra
    lb_titulo_algebra=Label(toplevel_notas_algebra,text="Notas Semestre")
    lb_titulo_algebra.config(bg="misty rose", fg="black", font=("Helvetica", 18))
    lb_titulo_algebra.place(x=280,y=10)

    # etiqueta para valor corte 1
    lb_c = Label(toplevel_notas_algebra, text = "corte 1 = ",)
    lb_c.config(bg="light gray", fg="black", font=("Helvetica", 18))
    lb_c.place(x=260, y=60)

    # caja de texto para corte 1
    entry_c = Entry(toplevel_notas_algebra, textvariable=nota_1_algebra)
    entry_c.config(bg="light gray", fg="black", font=("Times New Roman", 18), width=6)
    entry_c.focus_set()
    entry_c.place(x=400,y=60)

    # etiqueta para valor corte 2
    lb_c = Label(toplevel_notas_algebra, text = "corte 2 = ")
    lb_c.config(bg="light gray", fg="black", font=("Helvetica", 18))
    lb_c.place(x=260, y=110)

    # caja de texto para corte 2
    entry_c = Entry(toplevel_notas_algebra, textvariable=nota_2_algebra)
    entry_c.config(bg="light gray", fg="black", font=("Times New Roman", 18), width=6)
    entry_c.place(x=400,y=110)

    # etiqueta para valor corte 3
    lb_c = Label(toplevel_notas_algebra, text = "corte 3 = ")
    lb_c.config(bg="light gray", fg="black", font=("Helvetica", 18))
    lb_c.place(x=260, y=160)

    # caja de texto para corte 3
    entry_c = Entry(toplevel_notas_algebra, textvariable=nota_3_algebra)
    entry_c.config(bg="light gray", fg="black", font=("Times New Roman", 18), width=6)
    entry_c.place(x=400,y=160)

    # etiqueta para valor corte 4
    lb_c = Label(toplevel_notas_algebra, text = "corte 4 = ")
    lb_c.config(bg="light gray", fg="black", font=("Helvetica", 18))
    lb_c.place(x=260, y=210)

    # caja de texto para corte 4
    entry_c = Entry(toplevel_notas_algebra, textvariable=nota_4_algebra)
    entry_c.config(bg="light gray", fg="black", font=("Times New Roman", 18), width=6)
    entry_c.place(x=400,y=210)

    # boton de calcular_ programacion
    bt_calcular = Button(toplevel_notas_algebra, text="aceptar", command=aceptar_a)
    bt_calcular.place(x=390, y=250, width=90,height= 40)
    bt_calcular.config(bg = "lavenderblush2")

def aceptar_a():
    global n1_a,n2_a,n3_a,n4_a
    global nf_a
    n1_a = int(nota_1_algebra.get())
    n2_a = int(nota_2_algebra.get())
    n3_a = int(nota_3_algebra.get())
    n4_a = int(nota_4_algebra.get())

    toplevel_notas_algebra.destroy()

def abrir_toplevel_imc():
    global toplevel_imc
    toplevel_imc = Toplevel()
    toplevel_imc.title("indice de masa corporal")
    toplevel_imc.resizable(False, False)
    toplevel_imc.geometry("250x200")
    toplevel_imc.config(bg="white")

    #fondo del top level de algebra
    ln_fondo = Label(toplevel_imc,image=fondo_top_imc)
    ln_fondo.place(x=0,y=0)

        # titulo del imc
    lb_titulo_imc=Label(toplevel_imc,text="indice de masa corporal")
    lb_titulo_imc.config(bg="saddle brown", fg="black", font=("Helvetica", 16))
    lb_titulo_imc.place(x=10,y=10)

    # altura

    al_imc = Label(toplevel_imc, text = "altura = ",)
    al_imc.config(bg="bisque3", fg="black", font=("Helvetica", 14))
    al_imc.place(x=25, y=70)

    # caja de texto para altura
    entry_c = Entry(toplevel_imc, textvariable=al_1)
    entry_c.config(bg="bisque3", fg="black", font=("Times New Roman", 18), width=6)
    entry_c.focus_set()
    entry_c.place(x=110,y=68)

    #peso

    pe_imc = Label(toplevel_imc, text = "Peso = ",)
    pe_imc.config(bg="bisque3", fg="black", font=("Helvetica", 14))
    pe_imc.place(x=25, y=110)

    # caja de texto para peso
    entry_c = Entry(toplevel_imc, textvariable=pe_1)
    entry_c.config(bg="bisque3", fg="black", font=("Times New Roman", 18), width=6)
    entry_c.place(x=110,y=109)

    #boton aceptar

    imc_aceptar = Button(toplevel_imc, text="aceptar", command=aceptar_imc)
    imc_aceptar.place(x=80, y=150, width=90,height= 40)
    imc_aceptar.config(bg = "khaki3")

def aceptar_imc():
    global peso, altura
    global imc
    peso = int(pe_1.get())
    altura = float(al_1.get())

    toplevel_imc.destroy()


# funcion para boton de datos 
def boton_datos():
    global toplevel_dat
    toplevel_dat = Toplevel()
    toplevel_dat.title("Datos")
    toplevel_dat.resizable(False, False)
    toplevel_dat.geometry("250x200")
    toplevel_dat.config(bg="white")

    #fondo top level datos
    fondo_da = Label(toplevel_dat,image=fondo_top_datos)
    fondo_da.place(x=0,y=0)

            # titulo del imc
    lb_titulo_dat=Label(toplevel_dat,text="Datos")
    lb_titulo_dat.config(bg="seagreen1", fg="black", font=("Helvetica", 16))
    lb_titulo_dat.place(x=30,y=18)

    # alergias

    al_imc = Label(toplevel_dat, text = "alergias= ",)
    al_imc.config(bg="cyan3", fg="black", font=("Helvetica", 14))
    al_imc.place(x=25, y=70)

    # caja de texto para alergias
    entry_c = Entry(toplevel_dat, textvariable=ale_1)
    entry_c.config(bg="cyan3", fg="black", font=("Times New Roman", 18), width=10)
    entry_c.focus_set()
    entry_c.place(x=120,y=68)

    #tipo de sangre

    pe_imc = Label(toplevel_dat, text = "Sangre = ",)
    pe_imc.config(bg="cyan3", fg="black", font=("Helvetica", 14))
    pe_imc.place(x=25, y=110)

    # caja de texto para tipo de sangre
    entry_c = Entry(toplevel_dat, textvariable=san)
    entry_c.config(bg="cyan3", fg="black", font=("Times New Roman", 18), width=6)
    entry_c.place(x=120,y=109)

    #boton de aceptar a datos  
    dat_aceptar = Button(toplevel_dat, text="aceptar", command=aceptar_dat)
    dat_aceptar.place(x=80, y=150, width=90,height= 40)
    dat_aceptar.config(bg = "khaki3")

def aceptar_dat():
    global alergias
    global sangre
    alergias = str(ale_1.get())
    sangre = str(san.get())

    toplevel_dat.destroy()





# funcion para boton registro

def registro_s():
    t_resultados_s.delete("1.0","end")
    imc = peso // (altura**2)
    ale_1= alergias
    san = sangre
    t_resultados_s.insert(INSERT,f"Tu indice de masa corporal es:\n {imc} ")

    t_resultados_s.insert(INSERT,f"\neres alergico a:\n{ale_1}\ntu tipo de sangre es:\n{san}")


# boton para borrar

def boton_borrar_s():
        messagebox.showinfo("Registro medico", "Los datos serán borrados")
        b.set("")
        t_resultados_s.delete("1.0","end")



def boton_calcular_n():
    t_resultados_n.delete("1.0","end")
    if q.get()== 1 :
        nf_q =(n1_q+n2_q+n3_q+n4_q)/4
        nom =str(nombre_e.get())
        t_resultados_n.insert(INSERT,f" {nom} \ntus notas son:\nQuimica= {nf_q}")

    if c.get()== 1:
        nf_c=(n1_c+n2_c+n3_c+n4_c)/4
        t_resultados_n.insert(INSERT,f"\nCalculo 1= {nf_c}")
    
    if p.get()== 1:
        nf_p=(n1_p+n2_p+n3_p+n4_p)/4
        t_resultados_n.insert(INSERT,f"\nProgramacion= {nf_p}")

    if a.get()== 1:
        nf_a= (n1_a+n2_a+n3_a+n4_a)/4
        t_resultados_n.insert(INSERT,f"\nAlgebra= {nf_a}")

    if q.get()==0 and c.get()==0 and p.get()==0 and a.get()==0:
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
#variables de quimica
nota_1_quimica = StringVar()
nota_2_quimica = StringVar()
nota_3_quimica = StringVar()
nota_4_quimica = StringVar()
nf_q = StringVar()
#variables para los checkbutton
q = IntVar()
c = IntVar()
p = IntVar()
a = IntVar()
#variables para calculo
nota_1_calculo = StringVar()
nota_2_calculo = StringVar()
nota_3_calculo = StringVar()
nota_4_calculo = StringVar()
nf_c= StringVar()
#variables para programacion
nota_1_programacion = StringVar()
nota_2_programacion = StringVar()
nota_3_programacion = StringVar()
nota_4_programacion = StringVar()
nf_p= StringVar()
#variables para algebra
nota_1_algebra = StringVar()
nota_2_algebra = StringVar()
nota_3_algebra = StringVar()
nota_4_algebra = StringVar()
nf_a= StringVar()
#variable nombre estudiante
nom = StringVar
nombre_e= StringVar()
#variable del entry de altura y peso
altura= StringVar()
peso= StringVar()
pe_1= StringVar()
al_1 =StringVar()
imc= StringVar()
ale_1 = StringVar()
san= StringVar()
b=StringVar()
#---------------------------------------------------------------------------

#fondo de top level de programacion

fondo_top_programacion = PhotoImage(file="img/fondo_top_programacion.png")

# fondo de toplevel de quimica
fondo_top_quimica=PhotoImage(file="img/fondo_top_quimica.png")

#fondo de toplevel de calculo

fondo_top_calculo=PhotoImage(file="img/fondo_top_calculo.png")

# fondo de top level de algebra

fondo_top_algebra=PhotoImage(file="img/fondo_top_algebra.png")

#imagen de fondo ventana principal
f_vp = PhotoImage(file="img/fondo_ven_p.png")

#imagen de top level de quimica

logo_top_quimica = PhotoImage(file="img/logo_quimica.png")

#logo de toplevel de calculo

logo_top_calculo = PhotoImage(file="img/logo_calculo.png")

# logo de top level de programación

logo_top_programacion = PhotoImage(file="img/logo_programacion.png")

# logo de top level de algebra

logo_top_algebra=PhotoImage(file="img/logo_algebra.png")

# fondo de top level del imc

fondo_top_imc = PhotoImage(file="img/fondo_imc.png")

# fondo de top level de datos 
fondo_top_datos = PhotoImage(file="img/fondo_datos.png")

# fondo de la ventana principal

fondo_ventana_prin = Label(ventana_principal, image = f_vp) 
fondo_ventana_prin.place(x= 0, y=0)

#titulo del registro academico

titulo_n = Label(fondo_ventana_prin, text="Registro academico")
titulo_n.config(bg = "blanched almond",fg="black", font=("Helvetica", 20))
titulo_n.place(x=20,y=10)

# nombre estudiante titulo
nombre = Label(fondo_ventana_prin, text="Nombre:")
nombre.config(bg = "lightblue4",fg="black", font=("Helvetica", 15))
nombre.place(x=20,y=55)

#entry para el nombre:
entry_n = Entry(fondo_ventana_prin, textvariable=nombre_e)
entry_n.config(bg="lightblue3", fg="black", font=("Times New Roman", 18), width=20)
entry_n.focus_set()
entry_n.place(x=110,y=55)

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
bt_notas.place(x=380, y=50, width=80,height= 30)
bt_notas.config(bg = "peach puff")

# boton de label de notas de CALCULO 1
bt_notas = Button(fondo_ventana_prin, text="Calculo-1", command=abrir_toplevel_notas_calculo1)
bt_notas.place(x=380, y=10, width=80,height= 30)
bt_notas.config(bg = "peach puff")

#boton de label de notas de programacion
bt_notas = Button(fondo_ventana_prin, text="Programación", command=abrir_toplevel_notas_programacion)
bt_notas.place(x=480,y=10,width=80,height=30)
bt_notas.config(bg = "peach puff")

#boton de label de notas de algebra
bt_notas = Button(fondo_ventana_prin, text="Algebra", command=abrir_toplevel_notas_algebra)
bt_notas.place(x=480,y=50,width=80,height=30)
bt_notas.config(bg = "peach puff")

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

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

# cuadro de resultados de  la salud

t_resultados_s= Text(label_entrada_s)
t_resultados_s.config(bg= "lightblue1",fg = "black", font=("Helvetica", 10))
t_resultados_s.place(x=330,y=60, width=210,height=140)

# boton top level de indice de masa corporal

b_imc = Button(label_entrada_s, text="IMC", command=abrir_toplevel_imc)
b_imc.place(x=320,y=10, width=90,height=40)
b_imc.config(bg="darkolivegreen3",font=("helvetica", 15))

# boton top level de datos medicos

b_datos = Button(label_entrada_s, text="Datos",command=boton_datos)
b_datos.place(x=460,y=10, width=90,height=40)
b_datos.config(bg="red3",font=("helvetica", 15))

# boton registro

bt_registro = Button(label_entrada_s, text="Borrar", command=boton_borrar_s)
bt_registro.place(x=225, y=140, width=90,height= 40)
bt_registro.config(bg = "plum3",font=("Helvetica", 15))

# boton borrar

bt_registro = Button(label_entrada_s, text="Registro",command=registro_s)
bt_registro.place(x=225, y=80, width=90,height= 40)
bt_registro.config(bg = "khaki",font=("Helvetica", 15))


# titulo de notas final de semestre
titulo_n_f= Label(label_entrada, text="Notas Finales")
titulo_n_f.config(bg = "lightcyan2",fg="black", font=("Helvetica", 20))
titulo_n_f.place(x=385,y=10)

#cuadro de respuesta

t_resultados_n= Text(label_entrada)
t_resultados_n.config(bg="antiquewhite2", fg="gray1", font=("times new roman",15))
t_resultados_n.place(x=376,y=56,width=198,height=110)

# boton de calcular

bt_calcular_n = Button(label_entrada, text="calcular",command=boton_calcular_n)
bt_calcular_n.place(x=222, y=6, width=90,height= 40)
bt_calcular_n.config(bg = "darkolivegreen3",font=("Helvetica", 15))

# checkbutton de eleccion de quimica

cb_k = Checkbutton(label_entrada, text="Quimica",variable=q)
cb_k.config(bg="cadetblue2", fg="black", font=("Helvetica", 15))
cb_k.place(x=219, y=50)

# checkbutton de eleccion de calculo-1

cb_k = Checkbutton(label_entrada, text="Calculo-1",variable=c)
cb_k.config(bg="red3", fg="black", font=("Helvetica", 15))
cb_k.place(x=219, y=91)

#checkbutton de eleccion de programacion

cb_k = Checkbutton(label_entrada, text="Programacion",variable=p)
cb_k.config(bg="royalblue3", fg="black", font=("Helvetica", 15))
cb_k.place(x=219, y=132)

#checkbutton de eleccion de algebra

cb_k = Checkbutton(label_entrada, text="Algebra",variable=a)
cb_k.config(bg="springgreen2", fg="black", font=("Helvetica", 15))
cb_k.place(x=219, y=174)


bt_borrar = Button(label_entrada, text="Borrar",command=boton_borrar_n)
bt_borrar.config(bg="light steel blue",fg= "black", font=("helvetica", 15) )
bt_borrar.place(x=410,y=175, width=120, height=35)

# run 
ventana_principal.mainloop()
