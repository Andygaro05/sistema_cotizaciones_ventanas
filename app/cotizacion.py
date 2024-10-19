class Cotizacion:
    def __init__(self, cliente:object, ventanas:list, fecha:str):
        self.cliente = cliente
        self.ventanas = ventanas
        # self.cantidad_ventanas = cantidad_ventanas
        self.fecha = fecha

    def calcular_total(self):
        total = sum(ventana.calcular_costo_ventana() for ventana in self.ventanas)
        if len(self.ventanas) > 100:
            total *= 0.9
        return total