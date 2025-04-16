# ------------------------------------------------------------------------------
# EJERCICIO 8: Comparación y Determinación del Número Mayor
# ------------------------------------------------------------------------------
# Instrucciones:
# - Solicita dos números al usuario.
# - Utiliza condicionales (if/elif/else) para comparar ambos.
# - Imprime "El número X es mayor que Y", o "Ambos números son iguales" si se cumple esa condición.
# ------------------------------------------------------------------------------

try:
    num1 = float(input("Ingresa el primer número: "))
    num2 = float(input("Ingresa el segundo número: "))

    if num1 > num2:
        print(f"El número {num1} es mayor que {num2}")
    elif num2 > num1:
        print(f"El número {num2} es mayor que {num1}")
    else:
        print("Ambos números son iguales")

except ValueError:
    print("Error: Debes ingresar valores numéricos válidos.")
