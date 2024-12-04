from flask import Flask

class Usuario:
    def __init__(self, alias: str, nombre: str):
        self.alias = alias
        self.nombre = nombre
        self.listaContactos = []
        self.mensajesEnviados = []
        self.mensajesRecibidos = []

        def agregarContacto(alias: str, nombre: str):
            newContacto = []
            newContacto.append(alias)
            newContacto.append(nombre)
            self.listaContactos.append(newContacto)

        def listarContactos():
            for contacto in self.listaContactos:
                return

        
        def enviarMensaje(destinario : Contacto, contenido: str):
            
            for contacto in self.listaContactos:
                if destinario == contacto:
                    newMensaje = []
                    newMensaje.append(self.alias)
                    newMensaje.append(destinario.alias)
                    newMensaje.append(contenido)

                    self.mensajesEnviados.append(newMensaje)
        
        def verHistorialMensajes():

            return

class Contacto:
    def __init__(self, alias, fechaRegistro):
        self.alias = alias
        self.fechaRegistro = fechaRegistro


class Mensaje:
    def __init__(self, reminente: Usuario, destinario: Usuario, contenido, fechaEnvio):
        self.reminente = reminente
        self.destinario = destinario
        self.contenido = contenido
        self.fechaEnvio = fechaEnvio

