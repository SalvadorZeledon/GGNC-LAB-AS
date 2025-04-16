# ------------------------------------------------------------------------------
# EJERCICIO 2: Cálculo de Promedio de Tres Valores
# ------------------------------------------------------------------------------
# Instrucciones:
# - Pide tres números al usuario.
# - Suma los tres números y divide el resultado entre 3.
# - Imprime el mensaje "El promedio de los números ingresados es: X", 
#   donde X es el promedio calculado.
# ------------------------------------------------------------------------------

try:
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))
    num3 = float(input("Ingresa el tercer número: "))

    promedio = (num1 + num2 + num3) / 3
    print(f"El promedio de los números ingresados es: {promedio}")

except ValueError:
    print("Error: Debes ingresar valores numéricos válidos.")
