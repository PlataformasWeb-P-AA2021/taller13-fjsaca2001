from flask import Flask, render_template
import requests
import json

app = Flask(__name__, template_folder='templates')

@app.route("/")
def hello_world():
    return "<p>Hola, Mundo!</p>"


@app.route("/losestudiantes")
def los_estudiantes():
    """
    """
    r = requests.get("http://127.0.0.1:8090/api/estudiantes/",
            auth=('fjsaca', '123456'))
    estudiantes = json.loads(r.content)['results']
    numero_estudiantes = json.loads(r.content)['count']
    return render_template("losEdificios.html", estudiantes=estudiantes,
    numero_estudiantes=numero_estudiantes)


@app.route("/lostelefonos")
def los_telefonos():
    """
    """
    r = requests.get("http://127.0.0.1:8090/api/numerost/",
            auth=('fjsaca', '123456'))
    datos = json.loads(r.content)['results']
    numero = json.loads(r.content)['count']
    return render_template("losDepartamentos.html", datos=datos,
    numero=numero)


@app.route("/lostelefonosdos")
def los_telefonos_dos():
    """
    """
    r = requests.get("http://127.0.0.1:8090/api/numerost/",
            auth=('fjsaca', '123456'))
    datos = json.loads(r.content)['results']
    numero = json.loads(r.content)['count']
    datos2 = []
    for d in datos:
        datos2.append({'telefono':d['telefono'], 'tipo':d['tipo'],
        'estudiante': obtener_estudiante(d['estudiante'])})
    return render_template("lostelefonosdos.html", datos=datos2,
    numero=numero)

# funciones ayuda

def obtener_estudiante(url):
    """
    """
    r = requests.get(url, auth=('fjsaca', '123456'))
    nombre_estudiante = json.loads(r.content)['nombre']
    return nombre_estudiante
