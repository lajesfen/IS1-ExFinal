from typing import List
from classes import Usuario

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