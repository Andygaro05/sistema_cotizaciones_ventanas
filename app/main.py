from datetime import datetime
from ventana import Ventana
from cotizacion import Cotizacion
from cliente import Cliente


def mostrar_menu():
    print("1. Crear cotización")
    print("2. Salir")


def crear_cotizacion():
    ventanas = []
    # Fecha con hora
    fecha = datetime.now()
    fecha = fecha.strftime("%y/%m/%d %H:%M:%S %p")
    nombre_cliente = input("Ingrese el nombre del cliente: ")
    empresa_cliente = input("Ingrese el nombre de la empresa: ")
    direccion = input("Ingrese la dirección de la empresa: ")
    tipos_ventanas = int(input("Ingrese cuantos estilos diferentes de ventana desea: "))
    cantidad_ventanas = [0] * tipos_ventanas
    for i in range(tipos_ventanas):
        estilo = input("Ingrese el estilo de la ventana (O, XO, OXXO, OXO): ")
        ancho = float(input("Ingrese el ancho de la ventana (cm): "))
        alto = float(input("Ingrese el alto de la ventana (cm): "))
        acabado = input("Ingrese el tipo de acabado (Pulido, Lacado Brillante, Lacado Mate, Anodizado): ")
        tipo_vidrio = input("Ingrese el tipo de vidrio (Transparente, Bronce, Azul): ")
        esmerilado = input("Esmerilado (S/N)? ").lower() == 's'
        cantidad_ventanas[i] = int(input(f"Ingrese cuantas ventanas quiere con este estilo: "))

        ventana = Ventana(ancho, alto, estilo, acabado,tipo_vidrio, esmerilado)
        ventanas.append(ventana)

    cliente = Cliente(nombre_cliente, empresa_cliente, direccion)
    cotizacion = Cotizacion(cliente, ventanas, fecha)
    total = cotizacion.calcular_total()
    print(f"Nombre: {nombre_cliente}")
    print(f"Empresa: {empresa_cliente}")
    print(f"El costo total de la cotización es: ${total:.2f}")


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
