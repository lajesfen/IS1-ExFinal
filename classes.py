from typing import List
from app import dataHandler
from datetime import datetime

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
        return [f"{contacto} : {dataHandler.get_usuario(contacto.alias).nombre}" for contacto in self.listaContactos]

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