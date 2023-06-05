from tkinter import *
from tkinter import ttk
import tkinter as tk
from ControladorAlmacenB import *

controlador= ControladorAlmacenB()

def alta():
    controlador.altaProductos(varNom1.get(),varClas1.get(),varMar1.get(),varPre1.get())

def baja():
    confirmar=messagebox.askyesno('Pregunta','Confirma si quieres dar de Baja el Producto')
    if confirmar==True:
        controlador.bajaProductos(varBaja.get())
    else:
        messagebox.showinfo('Listo','El producto no ha sido dado de baja')

def consultar():
    Consu=controlador.consultarProductos()
    tabla.delete(*tabla.get_children())
    for producto in Consu:
        cadena=str(producto[0])+" "+str(producto[1])+" "+str(producto[2])+" "+str(producto[3])+" "+str(producto[4])
        
        tabla.insert('',tk.END,text=producto[0],values=cadena)
        tabla.bind('<<TreeviewSelect>>',consultar)

def actNombre():
    controlador.actualizarNombre(varid1.get(),varNom2.get())

def actClas():
    controlador.actualizarClasificacion(varid2.get(),varClas2.get())
    messagebox.showinfo("Listo","Se actualizo la Clasificacion")

def actMar():
    controlador.actualizarMarca(varid3.get(),varMar2.get())
    messagebox.showinfo("Listo","Se actualizo la Marca")

def actPre():
    controlador.actualizarPrecio(varid4.get(),varPre2.get())
    messagebox.showinfo("Listo","Se actualizo el Precio")

ventana=Tk()
ventana.title("Almacen de Bebidas")
ventana.geometry("700x450")

panel=ttk.Notebook(ventana)
panel.pack(fill='both',expand='yes')

pest1=ttk.Frame(panel)
pest2=ttk.Frame(panel)
pest3=ttk.Frame(panel)
pest4=ttk.Frame(panel)
pest5=ttk.Frame(panel)

titulo1=Label(pest1,text="ALTA de Productos", fg="#c075fa",font=("ALGERIAN",18)).pack()
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

btnAlta=Button(pest1,text="ALTA",bg="#d1a2f5",command=alta).pack()

titulo2=Label(pest2,text="BAJA de Productos", fg="#c075fa",font=("ALGERIAN",18)).pack()
varBaja=tk.StringVar()
lblBaja=Label(pest2,text="Identificador de Productos: ").pack()
txtBaja=Entry(pest2,textvariable=varBaja).pack()

btnBaja=Button(pest2,text="BAJA",bg="#d1a2f5",command=baja).pack()

titulo3=Label(pest3,text="Consultar Productos", fg="#c075fa",font=("ALGERIAN",18)).pack()
btnConsulta=Button(pest3,text="CONSULTAR",bg="#d1a2f5",command=consultar).pack()
subCon=Label(pest3,text="\n Productos dados de Alta \n",fg="#ac8dc4",font=("Brush Script MT",17)).pack()
textCon=tk.Text(pest3,height=10,width=60)
textCon.pack()

column=('num','nom','clas','mar','pre')
tabla=ttk.Treeview(textCon,columns=column,show='headings')
tabla.heading('num',text='ID')
tabla.heading('nom',text='Nombre')
tabla.heading('clas',text='Clasificacion')
tabla.heading('mar',text='Marca')
tabla.heading('pre',text='Precio')
tabla.pack()

titulo4=Label(pest4,text="ACTUALIZAR Productos", fg="#c075fa",font=("ALGERIAN",18)).pack()
varid1=tk.StringVar()
lblid1=Label(pest4,text="ID del Producto: ").pack()
txtid1=Entry(pest4,textvariable=varid1).pack()
varNom2=tk.StringVar()
lb1Nom2=Label(pest4,text="Nombre: ").pack()
txtNom2=Entry(pest4,textvariable=varNom2).pack()
btnActualizar1=Button(pest4,text="ACTUALIZAR NOMBRE",bg="#d1a2f5",command=actNombre).pack()
varid2=tk.StringVar()
lblid2=Label(pest4,text="ID del Producto: ").pack()
txtid2=Entry(pest4,textvariable=varid2).pack()
varClas2=tk.StringVar()
lb1Clas2=Label(pest4,text="Clasificacion: ").pack()
txtClas2=Entry(pest4,textvariable=varClas2).pack()
btnActualizar2=Button(pest4,text="ACTUALIZAR CLASIFICACION",bg="#d1a2f5",command=actClas).pack()
varid3=tk.StringVar()
lblid3=Label(pest4,text="ID del Producto: ").pack()
txtid3=Entry(pest4,textvariable=varid3).pack()
varMar2=tk.StringVar()
lb1Mar2=Label(pest4,text="Marca: ").pack()
txtMar2=Entry(pest4,textvariable=varMar2).pack()
btnActualizar3=Button(pest4,text="ACTUALIZAR MARCA",bg="#d1a2f5",command=actMar).pack()
varid4=tk.StringVar()
lblid4=Label(pest4,text="ID del Producto: ").pack()
txtid4=Entry(pest4,textvariable=varid4).pack()
varPre2=tk.StringVar()
lb1Pre2=Label(pest4,text="Precio: ").pack()
txtPre2=Entry(pest4,textvariable=varPre2).pack()
btnActualizar4=Button(pest4,text="ACTUALIZAR PRECIO",bg="#d1a2f5",command=actPre).pack()

titulo4=Label(pest5,text="OPERACIONES", fg="#c075fa",font=("ALGERIAN",18)).pack()
btnPromedio=Button(pest5,text="PROMEDIO",bg="#d1a2f5").pack()

panel.add(pest1,text="ALTA de productos")
panel.add(pest2,text="BAJA de productos")
panel.add(pest3,text="CONSULTAR productos")
panel.add(pest4,text="ACTUALIZAR productos")
panel.add(pest5,text="Operaciones")

ventana.mainloop()