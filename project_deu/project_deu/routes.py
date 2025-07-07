from flask import Blueprint, render_template

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('index.html')

@main.route('/about')
def about():
    return render_template('acerca.html')

@main.route('/observacion')
def obs():
    return render_template('agregar_observacion.html')

@main.route('/contactos')
def contactos():
    return render_template('contactos.html')

@main.route('/que_hacer')
def que_hacer():
    return render_template('que_hacer.html')

@main.route('/refugios')
def refugios():
    return render_template('refugios.html')
