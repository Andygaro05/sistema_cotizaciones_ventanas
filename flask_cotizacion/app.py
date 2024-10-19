from flask import Flask, render_template, request, redirect, url_for
from cliente import Cliente
from cotizacion import Cotizacion
from ventana import Ventana
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cotizacion', methods=['GET', 'POST'])
def crear_cotizacion():
    if request.method == 'POST':
        nombre_cliente = request.form['nombre_cliente']
        empresa_cliente = request.form['empresa_cliente']
        direccion_cliente = request.form['direccion']
        tipos_ventanas = int(request.form['tipos_ventanas'])

        ventanas = []
        for i in range(tipos_ventanas):
            estilo = request.form[f'estilo_{i}']
            ancho = float(request.form[f'ancho_{i}'])
            alto = float(request.form[f'alto_{i}'])
            acabado = request.form[f'acabado_{i}']
            tipo_vidrio = request.form[f'tipo_vidrio_{i}']
            esmerilado = 'esmerilado_{i}' in request.form
            cantidad_ventanas = int(request.form[f'cantidad_ventanas_{i}'])

            ventana = Ventana(ancho, alto, estilo, acabado, tipo_vidrio, esmerilado)
            ventanas.extend([ventana] * cantidad_ventanas)

        cliente = Cliente(nombre_cliente, empresa_cliente, direccion_cliente)
        fecha = datetime.now().strftime("%y/%m/%d %H:%M:%S %p")
        cotizacion = Cotizacion(cliente, ventanas, fecha)

        total, descuento = cotizacion.calcular_total()

        return render_template('factura.html', cotizacion=cotizacion, total=total, descuento=descuento)

    return render_template('cotizacion.html')


if __name__ == '__main__':
    app.run(debug=True)