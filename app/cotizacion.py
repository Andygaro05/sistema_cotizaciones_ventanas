from rich import print, table
from rich.console import Console
from datetime import datetime

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
        if len(self.ventanas) > 100:
            descuento = total * 0.1
            total -= descuento
        else:
            descuento = 0
        return total, descuento

    def imprimir_factura(self):

        # Crear una tabla para la factura
        factura_table = table.Table(title="COTIZACIÓN", show_header=True, header_style="bold magenta")
        factura_table.add_column("Detalle", style="bold blue")
        factura_table.add_column("Valor", style="green")

        # Agregar filas a la tabla
        factura_table.add_row("Número de Cotización:", str(self.numero))
        factura_table.add_row("Cliente:", self.cliente.nombre)
        factura_table.add_column("Empresa:", self.cliente.empresa)
        factura_table.add_row("Fecha:", self.fecha)

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