import math
from flask import Flask, render_template, request
import forms
#from flask_wtf.csrf import CSRFProtect


app= Flask(__name__)
app.secret_key ='clave secreta'
#csrf=CSRFProtect()

# ruta (como se quiere llamar la pagina)
@app.route("/")
def index():
    title="IDGS804 - IntroFlask"
    listado=["Juan","Ana","Pedro","Luisa"]

    return render_template('index.html',title=title,listado=listado )

@app.route("/saludo1", methods=['GET', 'POST'])
def saludo1():
    return render_template('saludo1.html')

@app.route("/saludo2")
def saludo2():
    return render_template('saludo2.html')

@app.route("/hola")
def func():
    return 'Hola, Mundo-hola'


@app.route("/user/<string:user>")
def user(user):
    return f'Hola, {user}'

@app.route("/numero/<int:n>")
def numero(n):
    return f'<h1>Núero: {n}</h1>'

@app.route("/user/<int:id>/<string:username>")
def username(id,username):
    return f"<h1>Hola, {username}! Tu ID es: {id}"

@app.route("/suma/<float:n1>/<float:n2>")
def suma(n1,n2):
    return f"<h1>La suma es:, {n1+n2}</h1>"

@app.route("/default/")
@app.route("/default/<string:param>")
def func2(param="juan"):
    return f"<h1>Hola, {param},</h1>"


@app.route("/operas")
def operas():
    return'''
        <form>
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        </br>
        <label for="name">apaterno:</label>
        <input type="text" id="name" name="name" required>
        </br>
        <input type="submit" value="Submit">
    </form>       
        '''


@app.route("/operasBas", methods=['GET','POST'])
def operasBas():
        res=None
        if request.method == 'POST':
            n1=request.form.get('num1')
            n2=request.form.get('num2')

            if request.form.get('operacion')=='suma':
                res=float(n1)+float(n2)
            if request.form.get('operacion')=='resta':
                res=float(n1)-float(n2)
            if request.form.get('operacion')=='multiplicacion':
                res=float(n1)*float(n2)
            if request.form.get('operacion')=='divicion':
                res=float(n1)/float(n2)

        return render_template('operasBas.html',res=res)

@app.route("/resultado", methods=['GET', 'POST'])
def resul1():
    n1=request.form.get('num1')
    n2=request.form.get('num2')
    return f"<h1>la suma es: {float(n1)+float(n2)}</h1>"

@app.route ('/distancia',  methods=['GET', 'POST'])
def distancia():
    resultado = None

    if request.method == 'POST':
        x1 = float(request.form.get('x1'))
        y1 = float(request.form.get('y1'))
        x2 = float(request.form.get('x2'))
        y2 = float(request.form.get('y2'))

        resultado = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    return render_template('distancia.html', distancia=resultado)

@app.route("/alumnos", methods=['GET', 'POST'])
def alumnos():
    mat=0
    nom=''
    ape=''
    email=''
    alumno_clas=forms.UserForm(request.form)
    if request.method=='POST'and alumno_clas.validate():
        mat =alumno_clas.matricula.data
        nom =alumno_clas.nombre.data
        ape =alumno_clas.apellido.data
        email =alumno_clas.correo.data
    return render_template("alumnos.html",form=alumno_clas, mat=mat, nom=nom, ape=ape,email=email)



if __name__=='__main__':
    #csrf.init_app(app)
    app.run(debug=True)