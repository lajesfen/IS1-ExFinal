from flask import Flask, request, jsonify
from datetime import datetime
from typing import List

app = Flask(__name__)

class Contacto:
    def __init__(self, alias, fechaRegistro):
        self.alias = alias
        self.fechaRegistro = fechaRegistro

class Usuario:
    def __init__(self, alias: str, nombre: str):
        self.alias = alias
        self.nombre = nombre
        self.listaContactos: List[Contacto] = []
        self.mensajesEnviados: List[Mensaje] = []
        self.mensajesRecibidos: List[Mensaje] = []

    def agregarContacto(self, alias: str, nombre: str):
        usuario = dataHandler.get_usuario(alias) # Busca un usuario por su alias

        if usuario is None: # Si el usuario no existe...
            usuario = Usuario(alias, nombre) # Crea un usuario nuevo
            contacto = Contacto(alias, datetime.now()) # y lo agrega como contacto
            
            dataHandler.add_usuario(usuario)
            self.listaContactos.append(contacto)
        else:
            contacto = Contacto(alias, datetime.now())
            self.listaContactos.append(contacto)

    def listarContactos(self):
        return [ f"{contacto.alias} : {dataHandler.get_usuario(contacto.alias).nombre}" for contacto in self.listaContactos ]

    def enviarMensaje(self, destinario: str, contenido: str):
        usuario = dataHandler.get_usuario(destinario)
        mensaje = Mensaje(self, usuario, contenido, datetime.now())

        self.mensajesEnviados.append(mensaje)
        usuario.mensajesRecibidos.append(mensaje)
    
    def verHistorialMensajes(self):
        return [f"{mensaje.reminente.alias} te escribió \"{mensaje.contenido}\" el {mensaje.fechaEnvio}" for mensaje in self.mensajesRecibidos]

class Mensaje:
    def __init__(self, reminente: Usuario, destinario: Usuario, contenido, fechaEnvio):
        self.reminente = reminente
        self.destinario = destinario
        self.contenido = contenido
        self.fechaEnvio = fechaEnvio

class DataHandler():
    def __init__(self):
        self.usuarios: List[Usuario] = []

    def get_usuarios(self):
        return self.usuarios

    def add_usuario(self, data: Usuario):
        self.usuarios.append(data)

    def get_usuario(self, alias: str):
        for usuario in self.usuarios:
            if usuario.alias == alias:
                return usuario
        return None

@app.route("/mensajeria/contactos", methods=['GET'])
def get_contactos_by_alias():
    alias = request.args.get('mialias')
    usuario = dataHandler.get_usuario(alias)

    res = usuario.listarContactos()
    return jsonify(res)

@app.route("/mensajeria/contactos/<alias>", methods=['POST'])
def post_contacto(alias: str):
    data = request.json
    contacto = data.get('contacto') # Alias del contacto
    nombre = data.get('nombre') # Solo relevante si el usuario es nuevo

    usuario = dataHandler.get_usuario(alias)
    usuario.agregarContacto(contacto, nombre)
    return jsonify('Contacto agregado')

@app.route("/mensajeria/enviar", methods=['POST'])
def post_enviar():
    data = request.json
    usuario = data.get('usuario') # Alias del que envia
    contacto = data.get('contacto') # Alias del destinatario
    mensaje = data.get('mensaje') # Texto del mensaje

    usuario = dataHandler.get_usuario(usuario)
    usuario.enviarMensaje(contacto, mensaje)
    return jsonify('Mensaje enviado')

@app.route("/mensajeria/recibidos", methods=['GET'])
def post_recibidos():
    alias = request.args.get('mialias')

    usuario = dataHandler.get_usuario(alias)
    res = usuario.verHistorialMensajes()
    return jsonify(res)

if __name__ == "__main__":
    dataHandler = DataHandler()
    dataHandler.add_usuario(Usuario('cpaz', 'Christian'))
    dataHandler.add_usuario(Usuario('lmunoz', 'Luisa'))
    dataHandler.add_usuario(Usuario('mgrau', 'iguel'))
    
    app.run(debug=True)