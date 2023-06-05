from tkinter import messagebox
import sqlite3
import bcrypt

class ControladorAlmacenB:
    
    def __init__(self):
        pass

    def conexionBD(self):
        try:
            conexion=sqlite3.connect("C:/Users/yarit/OneDrive/Documentos/GitHub/POOS181/Practicas/DB_AlmacenProductos.db")
            print("Conectado")
            return conexion
        except sqlite3.OperationalError:
            print("No se conecto")
    
    def altaProductos(self,nom,clas,marca,precio):
        conex=self.conexionBD()
        if(nom =="" or clas =="" or marca =="" or precio ==""):
            messagebox.showwarning("Formulario incompleto","Llena todos los campos")
            conex.close()
        else:
            cursor1=conex.cursor()
            datos=(nom,clas,marca,precio)
            sqlInsert="insert into Productos(nombre,clasificacion,marca,precio) values(?,?,?,?)"
            cursor1.execute(sqlInsert,datos)
            conex.commit()
            conex.close()
            messagebox.showinfo("Listo","Producto dado de Alta")
    
    def bajaProductos(self,id1):
        conex=self.conexionBD()
        if(id1==""):
            messagebox.showwarning("Error","Escribe un Identificador")
            conex.close()
        else:
            try:
                cursor2=conex.cursor()
                sqlDelete="delete from Productos where id= "+id1
                cursor2.execute(sqlDelete)
                conex.commit()
                conex.close()
                messagebox.showinfo("Listo","Producto dado de Baja")
            except sqlite3.OperationalError:
                print("Error")
    
    def consultarProductos(self):
        conex=self.conexionBD()
        try:
            cursor3=conex.cursor()
            sqlSelect="select * from Productos"
            cursor3.execute(sqlSelect)
            Cusuario=cursor3.fetchall()
            conex.close()
            return Cusuario
        except sqlite3.OperationalError:
            print("Error")
            
    def actualizarNombre(self,nom2,id2):
        conex=self.conexionBD()
        if(nom2 =="" or id2 ==""):
            messagebox.showwarning("Formulario incompleto","Llena todos los campos")
            conex.close()
        else:
            try:
                cursor4=conex.cursor()
                sqlUpdate1='update Productos set nombre=? where id= '+id2
                cursor4.execute(sqlUpdate1,nom2)
                conex.commit()
                messagebox.showinfo("Listo","Se actualizo el Nombre")
            except sqlite3.OperationalError:
                print("Error")
    
    def actualizarClasificacion(self,clas2,id3):
        conex=self.conexionBD()
        if(clas2 =="" or id3 ==""):
            messagebox.showwarning("Formulario incompleto","Llena todos los campos")
            conex.close()
        else:
            try:
                cursor5=conex.cursor()
                sqlUpdate2="update Productos set clasificacion=? where id= "+id3
                datos3=(clas2)
                cursor5.execute(sqlUpdate2,datos3)
                conex.commit()
                conex.close()
            except sqlite3.OperationalError:
                print("Error")
                
    def actualizarMarca(self,marca2,id4):
        conex=self.conexionBD()
        if(marca2 =="" or id4 ==""):
            messagebox.showwarning("Formulario incompleto","Llena todos los campos")
            conex.close()
        else:
            try:
                cursor6=conex.cursor()
                sqlUpdate3="update Productos set marca=? where id= "+id4
                datos4=(marca2)
                cursor6.execute(sqlUpdate3,datos4)
                conex.commit()
                conex.close()
            except sqlite3.OperationalError:
                print("Error")
    
    def actualizarPrecio(self,precio2,id5):
        conex=self.conexionBD()
        if(precio2 =="" or id5 ==""):
            messagebox.showwarning("Formulario incompleto","Llena todos los campos")
            conex.close()
        else:
            try:
                cursor7=conex.cursor()
                sqlUpdate4="update Productos set marca=? where id= "+id5
                datos5=(precio2)
                cursor7.execute(sqlUpdate4,datos5)
                conex.commit()
                conex.close()
            except sqlite3.OperationalError:
                print("Error")
    
    def promedio(self,precio):
        conex=self.conexionBD()
        try:
            cursor8=conex.cursor()
            sqlUpdate4="select precio from Productos"
            cursor8.execute(sqlUpdate4)
            if precio:
                total=sum(precio[0] for precio in precio)
                precio_promedio = total / len(precio)
                messagebox.showinfo("Promedio",precio_promedio)
            else:
                messagebox.showinfo("Promedio","No hay precios en la bd")
            conex.commit()
            conex.close()
        except sqlite3.OperationalError:
                print("Error")
                
    