from Usuario_CR import app
from flask import render_template, request, redirect
from Usuario_CR.modelo.modelo_usuario import Usuario


@app.route('/users')          # El decorador "@" asocia esta ruta con la función inmediatamente siguiente
def usuarios():
    usuarios = Usuario.get_all()
    return render_template('index.html', usuarios = usuarios)

@app.route('/users/new')
def nuevos_usuario():
    return render_template('add.html')

@app.route('/process', methods = ['POST'])
def process():
    result = Usuario.insertar_usuarios(request.form)
    print(result)
    return redirect('/users')

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return "ESTA RUTA NO FUE ENCONTRADA", 404
    #return render_template('404.html'), 404