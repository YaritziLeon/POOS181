from tkinter import *
from tkinter import ttk
import tkinter as tk

ventana=Tk()
ventana.title("Almacen de Bebidas")
ventana.geometry("700x500")
# Creamos nuestros panel
panel=ttk.Notebook(ventana)
panel.pack(fill='both',expand='yes')
#Creamos nuestras pestañas
pest1=ttk.Frame(panel)
pest2=ttk.Frame(panel)
pest3=ttk.Frame(panel)
pest4=ttk.Frame(panel)

titulo1=Label(pest1,text="ALTA de Productos", fg="#9fd2fc",font=("ALGERIAN",18)).pack()
varNom1=tk.StringVar()
lb1Nom1=Label(pest1,text="Nombre: ").pack()
txtNom1=Entry(pest1,textvariable=varNom1).pack()
varClas1=tk.StringVar()
lb1Clas1=Label(pest1,text="Clasificacion: ").pack()
txtClas1=Entry(pest1,textvariable=varClas1).pack()
varMar1=tk.StringVar()
lb1Mar1=Label(pest1,text="Marca: ").pack()
txtMar1=Entry(pest1,textvariable=varMar1).pack()
varPre1=tk.StringVar()
lb1Pre1=Label(pest1,text="Precio: ").pack()
txtPre1=Entry(pest1,textvariable=varPre1).pack()

btnGuardar=Button(pest1,text="ALTA",bg="#abf7d2").pack()

panel.add(pest1,text="ALTA de productos")
panel.add(pest2,text="BAJA de productos")
panel.add(pest3,text="CONSULTAR productos")
panel.add(pest4,text="ACTUALIZAR productos")

ventana.mainloop()