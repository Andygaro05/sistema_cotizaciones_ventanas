import pytest
import sys
import os

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.ventana import Ventana
from app.cotizacion import Cotizacion
from app.cliente import Cliente

def test_calcular_costo_vidrio_simple():
    """
    Prueba el cálculo del costo del vidrio para una ventana simple.
    """
    ventana = Ventana(ancho=12, alto=15, estilo="O", acabado_aluminio="Pulido",
                      tipo_vidrio="Transparente", esmerilado=False)
    costo_vidrio = ventana.calcular_costo_vidrio()
    costo_esperado = 891.0
    assert costo_vidrio == costo_esperado

def test_calcular_costo_vidrio_esmerilado():
    """
    Prueba el cálculo del costo del vidrio para una ventana esmerilada.
    """
    ventana = Ventana(ancho=24, alto=30, estilo="XO",
                      acabado_aluminio="Lacado Mate", tipo_vidrio="Bronce", esmerilado=True)
    costo_vidrio = ventana.calcular_costo_vidrio()
    costo_esperado = 5188.05
    assert costo_vidrio == costo_esperado

def test_calcular_costo_vidrio_estilo_invalido():
    """
    Prueba el comportamiento cuando se utiliza un estilo de ventana inválido.
    """
    with pytest.raises(ValueError):
        ventana = Ventana(ancho=100, alto=150, estilo="Z", acabado_aluminio="Pulido",
                          tipo_vidrio="Transparente", esmerilado=False)
        ventana.calcular_costo_vidrio()

def test_calcular_costo_aluminio_pulido():
    ventana = Ventana(ancho=12, alto=15, estilo="O", acabado_aluminio="Pulido", tipo_vidrio="Transparente")
    costo_esperado = 15210
    assert ventana.calcular_costo_aluminio() == costo_esperado

def test_calcular_costo_aluminio_lacado_brillante():
    ventana = Ventana(ancho=12, alto=15, estilo="O", acabado_aluminio="Lacado Brillante", tipo_vidrio="Transparente")
    costo_esperado = 16260
    assert ventana.calcular_costo_aluminio() == costo_esperado

def test_calcular_costo_aluminio_lacado_mate():
    ventana = Ventana(ancho=12, alto=15, estilo="O", acabado_aluminio="Lacado Mate", tipo_vidrio="Transparente")
    costo_esperado = 16080
    assert ventana.calcular_costo_aluminio() == costo_esperado

def test_calcular_costo_aluminio_anodizado():
    ventana = Ventana(ancho=12, alto=15, estilo="O", acabado_aluminio="Anodizado", tipo_vidrio="Transparente")
    costo_esperado = 17190  
    assert ventana.calcular_costo_aluminio() == costo_esperado

def test_calcular_costo_chapas_con_chapa():
    ventana = Ventana(ancho=100, alto=150, estilo="XO", acabado_aluminio="Pulido", tipo_vidrio="Transparente")
    assert ventana.calcular_costo_chapas() == 16200

def test_calcular_costo_chapas_sin_chapa():
    ventana = Ventana(ancho=100, alto=150, estilo="O", acabado_aluminio="Pulido", tipo_vidrio="Transparente")
    assert ventana.calcular_costo_chapas() == 0

def test_calcular_costo_ventana_total():
    ventana = Ventana(ancho=15, alto=20, estilo="OXO", acabado_aluminio="Lacado Mate", tipo_vidrio="Bronce", esmerilado=True)
    costo_total = ventana.calcular_costo_ventana()
    # Calcula el costo total esperado sumando los costos individuales y compara
    assert costo_total == 111594.6
