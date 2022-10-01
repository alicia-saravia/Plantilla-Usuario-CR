# importar la función que devolverá una instancia de una conexión
from Usuario_CR.configuracion.mysqlconnection import connectToMySQL

# modelar la clase después de la tabla friend de nuestra base de datos
class Usuario:
    def __init__( self , data ):
        self.id = data['id']
        self.nombre = data['nombre']
        self.apellido = data['apellido']
        self.email = data['email']
        self.creado_en = data['creado_en']
        self.actualizado_en = data['actualizado_en']
        
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM usuarios;"
# asegúrate de llamar a la función connectToMySQL con el esquema al que te diriges
        results = connectToMySQL('usuarios').query_db(query)
        return results

    
    @classmethod
    def insertar_usuarios(cls, data):
        query = "INSERT INTO usuarios (nombre,apellido,email) VALUES (%(nombre)s,%(apellido)s,%(email)s)"
        resultado = connectToMySQL('usuarios').query_db(query, data)
        return resultado
            
