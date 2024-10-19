class Cotizacion:
    numero_cotizacion = 1

    def __init__(self, cliente, ventanas, fecha):
        self.cliente = cliente
        self.ventanas = ventanas
        self.fecha = fecha
        self.numero = Cotizacion.numero_cotizacion
        Cotizacion.numero_cotizacion += 1

    def calcular_total(self):
        total = sum(ventana.calcular_costo_ventana() for ventana in self.ventanas)
        descuento = total * 0.1 if len(self.ventanas) > 100 else 0
        return total - descuento, descuento