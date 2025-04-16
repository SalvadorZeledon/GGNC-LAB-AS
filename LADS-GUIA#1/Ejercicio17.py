# ------------------------------------------------------------------------------
# EJERCICIO 17: Cálculo del Área de un Círculo mediante Función
# ------------------------------------------------------------------------------
# Instrucciones:
# - Define una función area_circulo(radio) que reciba el radio como parámetro.
# - Dentro de la función, calcula el área utilizando la fórmula:
#   área = 3.14 * (radio ** 2).
# - Retorna el área y, en el programa principal, solicita un radio y muestra el
#   mensaje "El área del círculo es: X".
# ------------------------------------------------------------------------------

def area_circulo(radio):
    return 3.14 * (radio ** 2)

try:
    radio = float(input("Ingresa el radio del círculo: "))
    area = area_circulo(radio)
    print(f"El área del círculo es: {area}")
except ValueError:
    print("Error: Debes ingresar un valor numérico válido.")
