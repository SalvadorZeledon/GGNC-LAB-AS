# ------------------------------------------------------------------------------
# EJERCICIO 3: Conversión de Temperatura de Celsius a Fahrenheit
# ------------------------------------------------------------------------------
# Instrucciones:
# - Define la función celsius_a_fahrenheit(celsius) que reciba un valor numérico.
# - Dentro de la función, aplica la fórmula: F = (C × 9/5) + 32 y retorna el resultado.
# - En el programa principal, solicita una temperatura en Celsius y muestra el 
#   resultado con el mensaje "X °C equivalen a Y °F".
# ------------------------------------------------------------------------------

def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

try:
    celsius = float(input("Ingresa la temperatura en °C: "))
    fahrenheit = celsius_a_fahrenheit(celsius)
    print(f"{celsius} °C equivalen a {fahrenheit} °F")

except ValueError:
    print("Error: Debes ingresar un valor numérico válido.")
