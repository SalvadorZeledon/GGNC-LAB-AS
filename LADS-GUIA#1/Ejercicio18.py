# ------------------------------------------------------------------------------
# EJERCICIO 18: Función que Sume y Retorne un Mensaje
# ------------------------------------------------------------------------------
# Instrucciones:
# - Define una función sumar(n1, n2) que sume dos números y retorne el string:
#   "La suma es: X", donde X es el resultado de la suma.
# - Llama a la función con valores de prueba y muestra el resultado.
# ------------------------------------------------------------------------------

def sumar(n1, n2):
    resultado = n1 + n2
    return f"La suma es: {resultado}"

print(sumar(10, 15))
