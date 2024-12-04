import unittest
from unittest.mock import patch
from app import Usuario, app

class MessageTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.client = app.test_client()
        app.config['TESTING'] = True

    # Caso de Éxito

    # Enviar un mensaje a un contacto existente
    def test_send_message_to_existing_contact(self):
        with patch('classes.dataHandler.get_usuario') as mock_get_usuario:
            user1 = Usuario("Luna", "Gabriela")
            user2 = Usuario("Mp123", "Mirella")

            mock_get_usuario.side_effect = [None, user2]
            user1.agregarContacto(user2.alias, user2.nombre)
            user1.enviarMensaje(user2.alias, "Hola Mirella")

            self.assertEqual(len(user1.mensajesEnviados), 1)
            self.assertEqual(len(user2.mensajesRecibidos), 1)
            self.assertEqual(user1.mensajesEnviados[0].contenido, "Hola Mirella")

    # Casos de Falla

    # Enviar mensaje a un contacto no existente
    def test_send_message_to_non_existing_contact(self):
        with patch('classes.dataHandler.get_usuario') as mock_get_usuario:
            user1 = Usuario("Edi", "Edison")

            mock_get_usuario.return_value = None
            user1.enviarMensaje("NonExistentAlias", "Hola")

            self.assertEqual(len(user1.mensajesEnviados), 0)

    # Agregar a un contacto no existente
    def test_add_non_existing_contact(self):
        with patch('classes.dataHandler.get_usuario') as mock_get_usuario, \
             patch('classes.dataHandler.add_usuario') as mock_add_usuario:
            user1 = Usuario("Soft", "Jeremi")

            mock_get_usuario.return_value = None
            user1.agregarContacto("NewAlias", "Nuevo Usuario")

            self.assertEqual(len(user1.listaContactos), 1)
            mock_add_usuario.assert_called_once()
    
    # Crear un usuario existente
    def test_create_existing_user(self):
        with patch('classes.dataHandler.get_usuario') as mock_get_usuario:
            mock_get_usuario.side_effect = [None, Usuario("Mari", "Mariana")]

            user1 = Usuario("Mari", "Mariana")
            user2 = Usuario("Mari", "Mariana")

            self.assertEqual(user1.alias, user2.alias)
            self.assertEqual(user1.nombre, user2.nombre)


    # Casos de Prueba Adicionales

    # Agregar un contacto
    def test_agregar_usuario_existente(self):
        with patch('classes.dataHandler.get_usuario') as mock_get_usuario, \
             patch('classes.dataHandler.add_usuario') as mock_add_usuario:
            user1 = Usuario("Soft", "Jeremi")
            mock_get_usuario.return_value = user1

            user1.agregarContacto("Soft", "Jeremi")

            self.assertEqual(len(user1.listaContactos), 0)
            mock_add_usuario.assert_not_called()
    
    # Agregar un contacto que ya existe
    def test_agregar_usuario_ya_existente(self):
        with patch('classes.dataHandler.get_usuario') as mock_get_usuario, \
             patch('classes.dataHandler.add_usuario') as mock_add_usuario:
            user1 = Usuario("Soft", "Jeremi")
            user2 = Usuario("Soft", "Jeremi")
            mock_get_usuario.side_effect = [None, user2]

            user1.agregarContacto("Soft", "Jeremi")
            user1.agregarContacto("Soft", "Jeremi")

            self.assertEqual(len(user1.listaContactos), 1)
            mock_add_usuario.assert_called_once()

if __name__ == "__main__":
    unittest.main()