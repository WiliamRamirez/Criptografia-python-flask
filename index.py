import string
from flask import Flask, render_template, request, redirect, url_for, flash

from function.cifrado_poli_alfabetico import fun_cifrado_poli_alfabeto_encriptar, fun_cifrado_poli_alfabeto_desencriptar
from function.cifrado_relleno import fun_cifrado_relleno_encriptar, fun_cifrado_relleno_desencriptar
from function.cifrado_sustitucion import fun_cifrado_sustitucion_encriptar, fun_cifrado_sustitucion_desencriptar
from function.cifrado_transposicion import fun_cifrado_transposicion_encriptar, fun_cifrado_transposicion_desencriptar

app = Flask(__name__)

app.secret_key = 'wserdctfvygijmiqfuimuiq'


@app.route('/')
def home():
    return render_template('home.html')


# cifrado por sustitucion encriptacion
@app.route('/encriptar_sustitucion', methods=['POST'])
def encriptar_sustitucion():
    if request.method == 'POST':
        mensaje: str = request.form['mensaje']
        desplace: int = int(request.form['desplace'])
        mensaje_cifrado = fun_cifrado_sustitucion_encriptar(desplace, mensaje)
        flash(mensaje, 'msg')
        flash(mensaje_cifrado, 'msg_encrypted')
        return redirect(url_for('cifrado_sustitucion_encriptar'))


@app.route('/cifrado_sustitucion_encriptar')
def cifrado_sustitucion_encriptar():
    return render_template('cifrado_sustitucion_encriptar.html')


# cifrado por sustitucion desencriptar
@app.route('/desencriptar_sustitucion', methods=['POST'])
def desencriptar_sustitucion():
    if request.method == 'POST':
        mensaje_cifrado: str = request.form['mensaje']
        desplace: int = int(request.form['desplace'])
        mensaje = fun_cifrado_sustitucion_desencriptar(desplace, mensaje_cifrado)
        flash(mensaje_cifrado, 'msg')
        flash(mensaje, 'msg_encrypted')
        return redirect(url_for('cifrado_sustitucion_desencriptar'))


@app.route('/cifrado_sustitucion_desencriptar')
def cifrado_sustitucion_desencriptar():
    return render_template('cifrado_sustitucion_desencriptar.html')


# cifrado por relleno de una sola vez
@app.route('/encriptar_relleno', methods=['POST'])
def encriptar_relleno():
    if request.method == 'POST':
        mensaje: str = request.form['mensaje']
        result = fun_cifrado_relleno_encriptar(mensaje)
        flash(result[0], 'msg_encrypted')
        flash(result[1], 'msg')
        return redirect(url_for('cifrado_relleno_encriptar'))


@app.route('/cifrado_relleno_encriptar')
def cifrado_relleno_encriptar():
    return render_template('cifrado_relleno_encriptar.html')


@app.route('/desencriptar_relleno', methods=['POST'])
def desencriptar_relleno():
    if request.method == 'POST':
        bits_cifrados: str = request.form['mensajeBits']
        bits_relleno: str = request.form['rellenoBits']
        mensaje = fun_cifrado_relleno_desencriptar(bits_cifrados, bits_relleno)
        flash(mensaje, 'msg')
        return redirect(url_for('cifrado_relleno_desencriptar'))


@app.route('/cifrado_relleno_desencriptar')
def cifrado_relleno_desencriptar():
    return render_template('cifrado_relleno_desencriptar.html')


# cifrado por transposicion encriptar
@app.route('/encriptar_transposicion', methods=['POST'])
def encriptar_transposicion():
    if request.method == 'POST':
        mensaje: str = request.form['mensaje']
        clave: str = request.form['clave']
        mensaje_cifrado = fun_cifrado_transposicion_encriptar(mensaje, clave)
        flash(mensaje, 'msg')
        flash(mensaje_cifrado, 'msg_encrypted')
        return redirect(url_for('cifrado_transposicion_encriptar'))


@app.route('/cifrado_transposicion_encriptar')
def cifrado_transposicion_encriptar():
    return render_template('cifrado_transposicion_encriptar.html')


# cifrado por transposicion desencriptar
@app.route('/desencriptar_transposicion', methods=['POST'])
def desencriptar_transposicion():
    if request.method == 'POST':
        mensaje_cifrado: str = request.form['mensaje']
        clave: str = request.form['clave']
        mensaje = fun_cifrado_transposicion_desencriptar(mensaje_cifrado, clave)
        flash(mensaje_cifrado, 'msg')
        flash(mensaje, 'msg_encrypted')
        return redirect(url_for('cifrado_transposicion_desencriptar'))


@app.route('/cifrado_transposicion_desencriptar')
def cifrado_transposicion_desencriptar():
    return render_template('cifrado_transposicion_desencriptar.html')


# cifrado por poli alfabeto encriptar
@app.route('/encriptar_poli_alfabeto', methods=['POST'])
def encriptar_poli_alfabeto():
    if request.method == 'POST':
        mensaje: str = request.form['mensaje']
        clave: str = request.form['clave']
        mensaje_cifrado = fun_cifrado_poli_alfabeto_encriptar(mensaje, clave)
        flash(mensaje, 'msg')
        flash(mensaje_cifrado, 'msg_encrypted')
        return redirect(url_for('cifrado_poli_alfabeto_encriptar'))


@app.route('/cifrado_poli_alfabeto_encriptar')
def cifrado_poli_alfabeto_encriptar():
    return render_template('cifrado_poli_alfabeto_encriptar.html')


# cifrado por poli alfabeto desencriptar
@app.route('/desencriptar_poli_alfabeto', methods=['POST'])
def desencriptar_poli_alfabeto():
    if request.method == 'POST':
        mensaje_cifrado: str = request.form['mensaje']
        clave: str = request.form['clave']
        mensaje = fun_cifrado_poli_alfabeto_desencriptar(mensaje_cifrado, clave)
        flash(mensaje_cifrado, 'msg')
        flash(mensaje, 'msg_encrypted')
        return redirect(url_for('cifrado_poli_alfabeto_desencriptar'))


@app.route('/cifrado_poli_alfabeto_desencriptar')
def cifrado_poli_alfabeto_desencriptar():
    return render_template('cifrado_poli_alfabeto_desencriptar.html')


if __name__ == '__main__':
    app.run(debug=True)
