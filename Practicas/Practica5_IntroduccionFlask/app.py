#importacion del framework
from flask import Flask,render_template,request,redirect,url_for,flash
from flask_mysqldb import MySQL
#inicializacion del APP o servidor
app= Flask(__name__)
#Configuracion de la conexion
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='bdflask'
app.secret_key='mysecretkey'
mysql=MySQL(app)
#declaracion de ruta  http://localhost:5000 
@app.route('/')
def index():
    return render_template('index.html')

#ruta http:localhost:5000/guaradr tipo POST para Insert
@app.route('/guardar', methods=['POST'])
def guardar():
    if request.method =='POST':
        #pasamos a variables el contenido de los inputs
        Vtitulo=request.form['txtTitulo']
        Vartista=request.form['txtArtista']
        Vanio=request.form['txtAnio']
        #Conectar y ejecutar  el insert
        CS=mysql.connection.cursor()
        CS.execute('insert into tb_albums(titulo,artista,anio) values(%s,%s,%s)',(Vtitulo,Vartista,Vanio))
        mysql.connection.commit()
        #print(titulo,artista,anio)
    
    flash('El album fue agregado correctamente')
    return redirect(url_for('index'))    

@app.route('/eliminar')
def eliminar():
    return "Se elimino de la BD"

#ejecucion del Servidor en el Puerto 5000
if __name__ == '__main__':
    app.run(port=5000,debug=True)