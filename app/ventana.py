class Ventana:
    def __init__(self, ancho, alto, estilo, acabado_aluminio, tipo_vidrio, esmerilado=False):
        self.ancho = ancho
        self.alto = alto
        self.estilo = estilo
        self.acabado_aluminio = acabado_aluminio
        self.tipo_vidrio = tipo_vidrio
        self.esmerilado = esmerilado

        # Precios por metro lineal
        self.precio_aluminio = {
            "Pulido": 50700,
            "Lacado Brillante": 54200,
            "Lacado Mate": 53600,
            "Anodizado": 57300
        }
        #Precio por cm^2
        self.precio_vidrio = {
            "Transparente": 8.25,
            "Bronce": 9.15,
            "Azul": 12.75
        }
        self.precio_esquina = 4310  # Precio por esquina
        self.precio_esmerilado = 5.20

    def numero_naves(self):
        match self.estilo.upper():
            case 'O':
                return 1
            case 'XO':
                return 2
            case 'OXO':
                return 3
            case 'OXXO':
                return 4
            case _:
                raise ValueError("Estilo de ventana no válido contactar a nuestros gerentes para una ventana personalizada")

    def calcular_costo_vidrio(self):
        #El 1.5 es la reducción del vidrio
        ancho_vidrio = (self.ancho - 2 * 1.5) / self.numero_naves()
        alto_vidrio = self.alto - 2 * 1.5
        area_vidrio_total = ancho_vidrio * alto_vidrio * self.numero_naves()

        #costos
        costo_base = area_vidrio_total * self.precio_vidrio[self.tipo_vidrio]
        costo_esmerilado = area_vidrio_total * self.precio_esmerilado if self.esmerilado else 0
        return costo_base + costo_esmerilado

    def calcular_costo_aluminio(self):
        ancho_perfil = (self.ancho - 2 * 1) / self.numero_naves()
        alto_perfil = self.alto - 2 * 1
        longitud_aluminio = 2 * ancho_perfil * self.numero_naves() + 2 * alto_perfil * self.numero_naves()

        #Se divide entre 100 pq el precio del aluminio es en metro y el calculo nos da en cm
        costo_aluminio = longitud_aluminio * self.precio_aluminio[self.acabado_aluminio] / 100
        return costo_aluminio

    def calcular_costo_esquinas(self):
        return self.precio_esquina * 4 * self.numero_naves()

    def calcular_costo_total(self):
        return self.calcular_costo_vidrio() + self.calcular_costo_aluminio() + self.calcular_costo_esquinas()

    
# Ejemplo de uso
# ventana1 = Ventana(120, 90, 'XO', 'Pulido', 'Transparente')
# costo_total_ventana1 = ventana1.calcular_costo_total()
# print("El costo total de la ventana 1 es:", costo_total_ventana1)

# ventana2 = Ventana(150, 120, 'OXXO', 'Lacado Mate', 'Azul', True)
# costo_total_ventana2 = ventana2.calcular_costo_total()
# print("El costo total de la ventana 2 es:", costo_total_ventana2)