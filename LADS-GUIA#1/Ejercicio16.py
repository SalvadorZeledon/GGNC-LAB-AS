# ------------------------------------------------------------------------------
# EJERCICIO 16: Recorrido y Formateo de un Diccionario
# ------------------------------------------------------------------------------
# Instrucciones:
# - Define un diccionario con al menos cuatro pares clave-valor (por ejemplo, datos de un estudiante).
# - Recorre el diccionario con un bucle for e imprime cada par en el formato:
#   "Clave: X, Valor: Y".
# ------------------------------------------------------------------------------

estudiante = {
    "nombre": "Salvador",
    "edad": 26,
    "carrera": "Ingeniería en Sistemas",
    "universidad": "USO"
}

for clave, valor in estudiante.items():
    print(f"Clave: {clave}, Valor: {valor}")
