from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/mensajeria/contactos", methods=['GET'])
def get_contactos_by_alias():
    alias = request.args.get('mialias')

    return jsonify(alias)

@app.route("/mensajeria/contactos/<alias>", methods=['POST'])
def post_contacto(alias: str):
    data = request.json
    contacto = data.get('contacto') # Alias del contacto
    nombre = data.get('nombre') # Solo relevante si el usuario es nuevo

    return jsonify(alias, contacto, nombre)

@app.route("/mensajeria/enviar", methods=['POST'])
def post_enviar():
    data = request.json
    usuario = data.get('usuario') # Alias del que envia
    contacto = data.get('contacto') # Alias del destinatario
    mensaje = data.get('mensaje') # Texto del mensaje

    return jsonify(usuario, contacto, mensaje)

@app.route("/mensajeria/recibidos", methods=['GET'])
def post_recibidos():
    alias = request.args.get('mialias')

    return jsonify(alias)

if __name__ == "__main__":
    app.run(debug=True)