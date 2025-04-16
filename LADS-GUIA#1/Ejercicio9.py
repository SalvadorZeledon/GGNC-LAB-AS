# ------------------------------------------------------------------------------
# EJERCICIO 9: Clasificación de Edad en Categorías
# ------------------------------------------------------------------------------
# Instrucciones:
# - Pide al usuario su edad (como número entero).
# - Establece los siguientes rangos:
#     o 0 a 12: "niño"
#     o 13 a 17: "adolescente"
#     o 18 a 64: "adulto"
#     o 65 o más: "anciano"
# - Muestra el mensaje "Con [edad] años, eres [categoría]".
# ------------------------------------------------------------------------------

try:
    edad = int(input("Ingresa tu edad: "))

    if edad < 0:
        print("Edad no válida.")
    elif edad <= 12:
        categoria = "niño"
    elif edad <= 17:
        categoria = "adolescente"
    elif edad <= 64:
        categoria = "adulto"
    else:
        categoria = "anciano"

    if edad >= 0:
        print(f"Con {edad} años, eres {categoria}.")

except ValueError:
    print("Error: Ingresa una edad válida (número entero).")
