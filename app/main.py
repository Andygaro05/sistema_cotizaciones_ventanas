from rich import print
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt 
from datetime import datetime
from ventana import Ventana
from cotizacion import Cotizacion
from cliente import Cliente


def mostrar_menu():
    console = Console()
    table = Table(title="Menú Principal")
    table.add_column("Opción")
    table.add_column("Descripción")
    table.add_row("1", "Crear cotización")
    table.add_row("2", "Salir")
    console.print(table)


def crear_cotizacion():
    ventanas = []
    # Fecha con hora
    fecha = datetime.now()
    fecha = fecha.strftime("%y/%m/%d %H:%M:%S %p")
    nombre_cliente = Prompt.ask("[bold green]Ingrese el nombre del cliente[/bold green]")
    empresa_cliente = Prompt.ask("[bold green]Ingrese el nombre de la empresa[/bold green]")
    direccion = Prompt.ask("[bold green]Ingrese la dirección de la empresa[/bold green]")
    tipos_ventanas = int(input("Ingrese cuantos estilos diferentes de ventana desea: "))
    for i in range(tipos_ventanas):
        estilo = input("Ingrese el estilo de la ventana (O, XO, OXXO, OXO): ")
        ancho = float(input("Ingrese el ancho de la ventana (cm): "))
        alto = float(input("Ingrese el alto de la ventana (cm): "))
        acabado = input("Ingrese el tipo de acabado (Pulido, Lacado Brillante, Lacado Mate, Anodizado): ")
        tipo_vidrio = input("Ingrese el tipo de vidrio (Transparente, Bronce, Azul): ")
        esmerilado = input("Esmerilado (S/N)? ").lower() == 's'
        cantidad_ventanas = int(input(f"Ingrese cuantas ventanas quiere con este estilo: "))

        ventana = Ventana(ancho, alto, estilo, acabado,tipo_vidrio, esmerilado)
        for _ in range(cantidad_ventanas):
            ventanas.append(ventana)

    cliente = Cliente(nombre_cliente, empresa_cliente, direccion)
    cotizacion = Cotizacion(cliente, ventanas, fecha)
    total = cotizacion.calcular_total()
    cotizacion.imprimir_factura()

def main():
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")
        if opcion == '1':
            crear_cotizacion()
        elif opcion == '2':
            print("Saliendo...")
            break
        else:
            print("Opción inválida. Intente de nuevo.")


if __name__ == "__main__":
    main()