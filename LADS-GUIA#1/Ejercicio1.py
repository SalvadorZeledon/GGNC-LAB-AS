# ------------------------------------------------------------------------------
# EJERCICIO 1: Operaciones Aritméticas Básicas con Manejo de Errores
# ------------------------------------------------------------------------------
# Instrucciones:
# - Solicita al usuario que ingrese dos números (pueden ser enteros o flotantes).
# - Calcula e imprime la suma, resta, multiplicación y división de ambos números.
# - Usa un bloque try/except para capturar el error de división por cero y, 
#   en ese caso, muestra el mensaje "Error: No se puede dividir por cero".
# ------------------------------------------------------------------------------

try:
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))

    suma = num1 + num2
    resta = num1 - num2
    multiplicacion = num1 * num2

    try:
        division = num1 / num2
    except ZeroDivisionError:
        division = "Error: No se puede dividir por cero"

    print(f"Suma: {suma}")
    print(f"Resta: {resta}")
    print(f"Multiplicación: {multiplicacion}")
    print(f"División: {division}")

except ValueError:
    print("Error: Debes ingresar valores numéricos válidos.")
