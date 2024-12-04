# EXAMEN FINAL - IS1

## PREGUNTA 3
### 1. Qué cambiaría en el código (Clases / Métodos) - No implementación.
- Se modificaría la función agregarContacto para validar la cantidad de contactos en la lista antes de adicionar uno nuevo.
- Se crearía una función eliminarContacto que tome como parametros el alias del usuario, y el contacto que se desea eliminar. Una vez se ejecuta la función se elimina el contacto de la lista.
- Se crearía una función eliminarUsuario que recibiría como parámetro el alias del usuario. Al ejecutar el comando, se eliminaría de la lista de DataHandler. Adicionalmente, tendría que comprobar los contactos de cada usuario y eliminar el contacto utilizando la función definida anteriormente, debido a que el usuario ya no existe.

### 2. Nuevos casos de prueba a adicionar.
- Se agregaría el caso donde se intente eliminar un usuario inexistente.
- Se agregaría el caso donde se intente eliminar un contacto inexistente para ese usuario.
- Se agregaría el caso donde se intenta agregar un contacto a la lista de un usuario y esta ya se encuentra llena.

### 3. Cuánto riesgo hay de “romper” lo que ya funciona?
- El mayor riesgo ocurriría en la función eliminarUsuario, ya que se tendría que verificar que no queden contactos (ahora inexistentes) en las listas de los usuarios.