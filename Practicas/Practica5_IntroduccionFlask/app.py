#importacion del framework
from flask import Flask,render_template,request
from flask_mysqldb import MySQL
#inicializacion del APP o servidor
app= Flask(__name__)
#Configuracion de la conexion
app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']=''
app.config['MYSQL_DB']='bdflask'
mysql=MySQL(app)
#declaracion de ruta  http://localhost:5000 
@app.route('/')
def index():
    return render_template('index.html')

#ruta http:localhost:5000/guaradr tipo POST para Insert
@app.route('/guardar', methods=['POST'])
def guardar():
    if request.method =='POST':
        titulo=request.form['txtTitulo']
        artista=request.form['txtArtista']
        anio=request.form['txtAnio']
        print(titulo,artista,anio)
    
    return 'Los datos llegaron'    

@app.route('/eliminar')
def eliminar():
    return "Se elimino de la BD"

#ejecucion del Servidor en el Puerto 5000
if __name__ == '__main__':
    app.run(port=5000,debug=True)