# ------------------------------------------------------------------------------
# EJERCICIO 19: Conversión Segura de Entrada a Entero
# ------------------------------------------------------------------------------
# Instrucciones:
# - Pide al usuario que ingrese un dato que se supone es un número.
# - Usa un bloque try/except para intentar convertir la entrada a entero.
# - Si la conversión es exitosa, imprime "El número ingresado es: X";
#   de lo contrario, muestra "Error: Entrada no válida".
# ------------------------------------------------------------------------------

entrada = input("Ingresa un número: ")

try:
    numero = int(entrada)
    print(f"El número ingresado es: {numero}")
except ValueError:
    print("Error: Entrada no válida.")
