from flask import Flask,render_template,request,redirect,url_for,flash
from flask_mysqldb import MySQL

app=Flask(__name__)

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='DB_Floreria'
app.secret_key='mysecretkey'
mysql=MySQL(app)

@app.route('/')
def index1():
    CC=mysql.connection.cursor()
    CC.execute('select * from tbflores')
    Flores=CC.fetchall()
    return render_template('index1.html',listaFlores=Flores)
    

@app.route('/ingresar', methods=['POST'])
def ingresar():
    if request.method =='POST':
        Vnombre=request.form['txtNombre']
        Vcantidad=request.form['Cantidad']
        Vprecio=request.form['Precio']
        CS=mysql.connection.cursor()
        CS.execute('insert into tbflores (nombre,cantidad,precio) values (%s,%s,%s)',(Vnombre,Vcantidad,Vprecio))
        mysql.connection.commit()
        
        flash('La flor fue agregada')
        return redirect(url_for('index1'))

@app.route('/eliminar/<id>',methods=['POST'])
    def eliminar(id):
        if request.method== 'POST':
    

if __name__ == '__main__':
    app.run(port=5001,debug=True)