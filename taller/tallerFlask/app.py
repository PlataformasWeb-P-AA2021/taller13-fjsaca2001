from flask import Flask, render_template
import requests
import json

app = Flask(__name__, template_folder='templates')


@app.route("/")
def hello_world():
    return "<p>Hola, Mundo!</p><a href='http://127.0.0.1:5000/losEdificios'>Edificios</a><br><a href='http://127.0.0.1:5000/losDepartamentos'>Departamentos</a>"


@app.route("/losEdificios")
def losEdificios():
    """
    """
    r = requests.get("http://127.0.0.1:8000/api/edificio/",
                     auth=('fjsaca', '123456'))
    edificios = json.loads(r.content)['results']
    nroEdificios = json.loads(r.content)['count']
    return render_template("losEdificios.html", edificios=edificios,
                           nroEdificios=nroEdificios)


@app.route("/losDepartamentos")
def losDepartamentos():
    """
    """
    r = requests.get("http://127.0.0.1:8000/api/departamento/",
                     auth=('fjsaca', '123456'))
    departamentos = json.loads(r.content)['results']
    nroDepartamentos = json.loads(r.content)['count']
    departamentos2 = []
    for d in departamentos:
        departamentos2.append({'nombrePropietario': d['nombrePropietario'], 'costoDepartamento': d['costoDepartamento'],
                               'numeroCuartos': d['numeroCuartos'], 'edificio': obtenerEdificio(d['edificio'])})
    return render_template("losDepartamentos.html", departamentos=departamentos2,
                           nroDepartamentos=nroDepartamentos)


# funciones ayuda

def obtenerEdificio(url):
    """
    """
    r = requests.get(url, auth=('fjsaca', '123456'))
    edificio = json.loads(r.content)['nombre'] + " - " + json.loads(r.content)['ciudad'] + " - " + json.loads(r.content)['direccion']
    return edificio
