from flask import Flask, jsonify
app = Flask(__name__)
@app.route("/")
def inicio():
 return jsonify({
 "mensaje": "API funcionando",
 "curso": "Desarrollo de APIs"
 })
@app.route("/alumnos")
def alumnos():
 return jsonify([
 {
 "id": 1,
 "nombre": "Ana"
 },
 {
 "id": 2,
 "nombre": "Carlos"
 }
 ])

# Nueva ruta /redes agregada 
@app.route("/redes")
def redes():
    return jsonify({
        "mensaje": "¡Hola! Bienvenidos"
    })
if __name__ == "__main__":
 app.run(debug=True)