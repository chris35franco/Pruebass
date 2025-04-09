import pytest
from calculo_pago import calcular_pago

def test_calculo_normal():
    resultado = calcular_pago("Docente tiempo completo", horas_diurnas=10, horas_nocturnas=5, horas_dominicales=2, horas_festivas=1)
    assert "Salario Bruto: $787500 pesos" in resultado
    assert "Descuento Parafiscales: $63000 pesos" in resultado
    assert "Salario Neto: $724500 pesos" in resultado

def test_contrato_invalido():
    resultado = calcular_pago("Docente por horas", horas_diurnas=10)
    assert resultado == "Error: Contrato no válido."

def test_tarifa_negativa():
    resultado = calcular_pago("Docente tiempo completo", horas_diurnas=10)
    assert "Error" not in resultado  

def test_horas_negativas():
    resultado = calcular_pago("Docente tiempo completo", horas_diurnas=-5, horas_nocturnas=10)
    assert "Error: Horas diurnas no pueden ser negativas." in resultado
    assert "Solo se calculará la jornada con valores correctos." in resultado

def test_una_sola_jornada_correcta():
    resultado = calcular_pago("Docente medio tiempo", horas_diurnas=0, horas_nocturnas=0, horas_dominicales=5, horas_festivas=-3)
    assert "Error: Horas festivas no pueden ser negativas." in resultado
    assert "Solo se calculará la jornada con valores correctos." in resultado
    assert "Salario Bruto" in resultado  
def test_todas_las_horas_negativas():
    resultado = calcular_pago("Docente tiempo completo", horas_diurnas=-2, horas_nocturnas=-3, horas_dominicales=-1, horas_festivas=-5)
    assert "Error: Horas diurnas no pueden ser negativas." in resultado
    assert "Error: Horas nocturnas no pueden ser negativas." in resultado
    assert "Error: Horas dominicales no pueden ser negativas." in resultado
    assert "Error: Horas festivas no pueden ser negativas." in resultado

def test_salario_cero():
    resultado = calcular_pago("Docente tiempo completo", horas_diurnas=0, horas_nocturnas=0, horas_dominicales=0, horas_festivas=0)
    assert "Salario Bruto: $0 pesos" in resultado
    assert "Descuento Parafiscales: $0 pesos" in resultado
    assert "Salario Neto: $0 pesos" in resultado

