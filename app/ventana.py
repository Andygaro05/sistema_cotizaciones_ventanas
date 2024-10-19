class Ventana:
    def __init__(self, ancho:float, alto:float, estilo:str, acabado_aluminio:str, tipo_vidrio:str, esmerilado=False):
        self.ancho = ancho
        self.alto = alto
        self.estilo = estilo
        self.acabado_aluminio = acabado_aluminio
        self.tipo_vidrio = tipo_vidrio
        
        if esmerilado == "s":
            self.esmerilado = True
        else:
            self.esmerilado = False

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
        self.precio_esquina = 4310
        self.precio_chapa = 16200
        self.precio_esmerilado = 5.20

    def numero_naves(self):
        match self.estilo.upper():
            case 'O':
                return 1
            case 'XO':
                return 2
            case 'OX':
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
        alto_vidrio = self.alto - (2 * 1.5)
        area_vidrio_total = ancho_vidrio * alto_vidrio * self.numero_naves()

        #costos
        costo_base = area_vidrio_total * self.precio_vidrio[self.tipo_vidrio]
        if self.esmerilado == True:
            costo_esmerilado = area_vidrio_total * self.precio_esmerilado 
        else:
            costo_esmerilado = 0
        return costo_base + costo_esmerilado

    def calcular_costo_aluminio(self):
        ancho_perfil = self.ancho/ self.numero_naves()
        #El 4 es por las esquinas y como son 2 pero se insertan 1 cm a cada placa
        ancho_perfil = ancho_perfil - (4*2-2)
        alto_perfil = self.alto - (4*2-2)
        longitud_aluminio = 2*ancho_perfil * self.numero_naves() + 2 * alto_perfil *self.numero_naves()

        #Se divide entre 100 pq el precio del aluminio es en metro y el calculo nos da en cm
        costo_aluminio = longitud_aluminio * self.precio_aluminio[self.acabado_aluminio] / 100
        return costo_aluminio

    def calcular_costo_esquinas(self):
        return self.precio_esquina * 4 * self.numero_naves()

    def calcular_costo_chapas(self):
        if "X" in self.estilo:
            return 16200
        return 0

    def calcular_costo_ventana(self):
        return self.calcular_costo_vidrio() + self.calcular_costo_aluminio() + self.calcular_costo_esquinas() + self.calcular_costo_chapas()
