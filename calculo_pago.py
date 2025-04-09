def calcular_pago(tipo_contrato="Docente tiempo completo", horas_diurnas=0, horas_nocturnas=0, horas_dominicales=0, horas_festivas=0):
    tarifas = {
        "Docente tiempo completo": 50000,
        "Docente medio tiempo": 30000
    }
    
    if tipo_contrato not in tarifas:
        return "Error: Contrato no válido."

    tarifa = tarifas[tipo_contrato]

    if tarifa < 0:
        return "Error: La tarifa por hora no puede ser negativa."

    errores = []
    if horas_diurnas < 0:
        errores.append("Error: Horas diurnas no pueden ser negativas.")
    if horas_nocturnas < 0:
        errores.append("Error: Horas nocturnas no pueden ser negativas.")
    if horas_dominicales < 0:
        errores.append("Error: Horas dominicales no pueden ser negativas.")
    if horas_festivas < 0:
        errores.append("Error: Horas festivas no pueden ser negativas.")

    if errores:
        errores.append("Solo se calculará la jornada con valores correctos.")

    pago_diurno = max(0, horas_diurnas) * tarifa
    pago_nocturno = max(0, horas_nocturnas) * tarifa * 1.35
    pago_dominical = max(0, horas_dominicales) * tarifa * 1.75
    pago_festivo = max(0, horas_festivas) * tarifa * 1.75

    salario_total = pago_diurno + pago_nocturno + pago_dominical + pago_festivo
    descuento_parafiscales = salario_total * 0.08
    salario_neto = salario_total - descuento_parafiscales

    if salario_neto < 0:
        return "Error: Salario negativo, revise los datos ingresados."

    resultado = f"""
Salario Bruto: ${int(salario_total)} pesos
Descuento Parafiscales: ${int(descuento_parafiscales)} pesos
Salario Neto: ${int(salario_neto)} pesos
"""

    if errores:
        return "\n".join(errores) + "\n" + resultado

    return resultado
