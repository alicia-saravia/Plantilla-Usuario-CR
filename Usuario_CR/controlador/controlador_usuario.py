from Usuario_CR import app
from flask import render_template, request, redirect
from Usuario_CR.modelo.modelo_usuario import Usuario


@app.route('/users')          # El decorador "@" asocia esta ruta con la función inmediatamente siguiente
def usuarios():
    usuarios = Usuario.get_all()
    return render_template('index.html', usuarios = usuarios)

@app.route('/users/<id>')      # recibe una ruta variable del tipo /users/1
def show(id):
    data = {
        'id': id
    }
    usuario = Usuario.mostrar_usuario(data)
    return render_template('show.html', usuario = usuario)

@app.route('/users/<id>/edit')      # recibe una ruta variable del tipo /users/1
def editar(id):
    data = {
        'id': id
    }
    usuario = Usuario.mostrar_usuario(data)  
    return render_template('edit.html', usuario = usuario)

@app.route('/users/new')
def nuevos_usuario():
    return render_template('add.html')

@app.route('/process', methods = ['POST'])
def process():
    result = Usuario.insertar_usuarios(request.form)
    print(result)
    return redirect('/users')

@app.route('/update' , methods = ['POST'])      # recibe una ruta variable del tipo /users/1
def update():
    usuario = Usuario.update(request.form)
    print(request.form)
    return redirect('/users/' + request.form['id'])

@app.route('/delete/<id>')      # recibe una ruta variable del tipo /users/1
def delete(id):
    data = {
        'id': id
    }
    usuario = Usuario.delete(data)
    return redirect('/users')
    
@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return "ESTA RUTA NO FUE ENCONTRADA", 404
    #return render_template('404.html'), 404