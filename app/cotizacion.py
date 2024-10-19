class Cotizacion:
    numero_cotizacion = 1

    def __init__(self, cliente:object, ventanas:list[object], fecha:str):
        self.cliente = cliente
        self.ventanas = ventanas
        self.fecha = fecha
        self.numero = Cotizacion.numero_cotizacion
        Cotizacion.numero_cotizacion += 1

    def calcular_total(self):
        total = sum(ventana.calcular_costo_ventana() for ventana in self.ventanas)
        if len(self.ventanas) > 100:
            descuento = total * 0.1
            total -= descuento
        else:
            descuento = 0
        return total, descuento

    def imprimir_factura(self):
        print("-" * 30)
        print("COTIZACIÓN")
        print("-" * 30)
        print(f"Número de Cotización: {self.numero}")
        print(f"Cliente: {self.cliente.nombre}")
        print(f"Empresa: {self.cliente.empresa}")
        print(f"Fecha: {self.fecha}")
        print()

        # Agrupar las ventanas por estilo y calcular el total por estilo
        ventanas_por_estilo = {}
        for ventana in self.ventanas:
            estilo = ventana.estilo
            if estilo not in ventanas_por_estilo:
                ventanas_por_estilo[estilo] = [ventana]
            else:
                ventanas_por_estilo[estilo].append(ventana)

        for estilo, ventanas in ventanas_por_estilo.items():
            total_estilo = sum(ventana.calcular_costo_ventana() for ventana in ventanas)
            print(f"Estilo: {estilo}")
            print(f"Cantidad: {len(ventanas)}")
            print(f"Total: ${total_estilo:.2f}")
            print()

        # Total general y descuento
        total_general, descuento = self.calcular_total()
        print(f"Total General (sin descuento): ${total_general + descuento:.2f}")
        print(f"Descuento (10%): ${descuento:.2f}")
        print(f"Total a pagar: ${total_general:.2f}")
        print()
        print(f"Su pedido será enviado entre 1 y 7 días hábiles a la ubicación {self.cliente.direccion}")
        print("-" * 30)