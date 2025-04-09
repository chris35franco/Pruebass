import unittest
from calculo_pago import calcular_pago

class TestCasosAceptacion(unittest.TestCase):

    def test_01_contrato_invalido(self):
        resultado = calcular_pago("Otro", 5)
        self.assertEqual(resultado, "Error: Contrato no válido.")

    def test_02_tiempo_completo_horas_diurnas(self):
        resultado = calcular_pago("Docente tiempo completo", horas_diurnas=10)
        self.assertIn("Salario Bruto: $500000", resultado)
        self.assertIn("Salario Neto: $460000", resultado)

    def test_03_medio_tiempo_horas_diurnas(self):
        resultado = calcular_pago("Docente medio tiempo", horas_diurnas=10)
        self.assertIn("Salario Bruto: $300000", resultado)
        self.assertIn("Salario Neto: $276000", resultado)

    def test_04_horas_nocturnas_recargo(self):
        resultado = calcular_pago("Docente tiempo completo", horas_nocturnas=10)
        self.assertIn("Salario Bruto: $675000", resultado)
        self.assertIn("Salario Neto: $621000", resultado)

    def test_05_horas_dominicales_recargo(self):
        resultado = calcular_pago("Docente tiempo completo", horas_dominicales=10)
        self.assertIn("Salario Bruto: $875000", resultado)
        self.assertIn("Salario Neto: $805000", resultado)

    def test_06_horas_festivas_recargo(self):
        resultado = calcular_pago("Docente tiempo completo", horas_festivas=10)
        self.assertIn("Salario Bruto: $875000", resultado)
        self.assertIn("Salario Neto: $805000", resultado)

    def test_07_docente_sin_horas(self):
        resultado = calcular_pago("Docente tiempo completo")
        self.assertIn("Salario Bruto: $0", resultado)
        self.assertIn("Salario Neto: $0", resultado)

    def test_08_horas_negativas(self):
        resultado = calcular_pago("Docente tiempo completo", horas_diurnas=-5)
        self.assertIn("Error: Horas diurnas no pueden ser negativas.", resultado)

    def test_09_todas_las_categorias(self):
        resultado = calcular_pago("Docente tiempo completo", horas_diurnas=5, horas_nocturnas=5, horas_dominicales=5, horas_festivas=5)
        self.assertIn("Salario Bruto: $1462500", resultado)
        self.assertIn("Salario Neto: $1345500", resultado)

    def test_10_verificar_descuento_8_por_ciento(self):
        resultado = calcular_pago("Docente tiempo completo", horas_diurnas=10)
        self.assertIn("Descuento Parafiscales: $40000", resultado)

    def test_11_docente_100h_diurnas(self):
        resultado = calcular_pago("Docente tiempo completo", horas_diurnas=100)
        self.assertIn("Salario Bruto: $5000000", resultado)
        self.assertIn("Salario Neto: $4600000", resultado)

    def test_12_docente_50h_nocturnas(self):
        resultado = calcular_pago("Docente tiempo completo", horas_nocturnas=50)
        self.assertIn("Salario Bruto: $3375000", resultado)
        self.assertIn("Salario Neto: $3105000", resultado)

    def test_13_docente_30h_dominicales(self):
        resultado = calcular_pago("Docente tiempo completo", horas_dominicales=30)
        self.assertIn("Salario Bruto: $2625000", resultado)
        self.assertIn("Salario Neto: $2415000", resultado)

    def test_14_docente_20h_festivas(self):
        resultado = calcular_pago("Docente tiempo completo", horas_festivas=20)
        self.assertIn("Salario Bruto: $1750000", resultado)
        self.assertIn("Salario Neto: $1610000", resultado)

    def test_15_solo_10h_nocturnas(self):
        resultado = calcular_pago("Docente tiempo completo", horas_diurnas=0, horas_nocturnas=10)
        self.assertIn("Salario Bruto: $675000", resultado)

    def test_16_solo_10h_dominicales(self):
        resultado = calcular_pago("Docente tiempo completo", horas_dominicales=10)
        self.assertIn("Salario Bruto: $875000", resultado)

    def test_17_solo_10h_festivas(self):
        resultado = calcular_pago("Docente tiempo completo", horas_festivas=10)
        self.assertIn("Salario Bruto: $875000", resultado)

    def test_18_todas_categorias_medio_tiempo(self):
        resultado = calcular_pago("Docente medio tiempo", horas_diurnas=5, horas_nocturnas=5, horas_dominicales=5, horas_festivas=5)
        self.assertIn("Salario Bruto: $877500", resultado)
        self.assertIn("Salario Neto: $807300", resultado)

    def test_19_varias_combinaciones_tiempo_completo(self):
        resultado1 = calcular_pago("Docente tiempo completo", horas_diurnas=5, horas_nocturnas=5)
        resultado2 = calcular_pago("Docente tiempo completo", horas_dominicales=5, horas_festivas=5)
        self.assertNotEqual(resultado1, resultado2)

    def test_20_varias_combinaciones_medio_tiempo(self):
        resultado1 = calcular_pago("Docente medio tiempo", horas_diurnas=5, horas_nocturnas=5)
        resultado2 = calcular_pago("Docente medio tiempo", horas_dominicales=5, horas_festivas=5)
        self.assertNotEqual(resultado1, resultado2)

if __name__ == "__main__":
    unittest.main()

