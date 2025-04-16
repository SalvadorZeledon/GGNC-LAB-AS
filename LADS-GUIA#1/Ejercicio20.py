# ------------------------------------------------------------------------------
# EJERCICIO 20: Parseo y Validación de un String JSON
# ------------------------------------------------------------------------------
# Instrucciones:
# - Define una función parsear_json(json_str) que intente convertir el string usando json.loads().
# - Si ocurre un error (por ejemplo, JSON mal formado), captura la excepción y
#   retorna o imprime "Error: JSON inválido".
# - En el programa principal, prueba la función con un string JSON correcto y otro incorrecto,
#   mostrando los resultados.
# ------------------------------------------------------------------------------

import json

def parsear_json(json_str):
    try:
        data = json.loads(json_str)
        return data
    except json.JSONDecodeError:
        return "Error: JSON inválido"

# Caso 1: Uso correcto 
json_valido = '{"nombre": "Salvador", "edad": 22}'
resultado_valido = parsear_json(json_valido)
print("Resultado válido:", resultado_valido)

# Caso 2: Este es el el incorrecto (osea da error)
json_invalido = '{"nombre": "Salvador", "edad": 22'  
resultado_invalido = parsear_json(json_invalido)
print("Resultado inválido:", resultado_invalido)
