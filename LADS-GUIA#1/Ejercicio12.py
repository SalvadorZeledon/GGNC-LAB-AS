# ------------------------------------------------------------------------------
# EJERCICIO 12: Suma de Elementos en un Array (Módulo array)
# ------------------------------------------------------------------------------
# Instrucciones:
# - Importa el módulo array y crea un array de enteros con los valores [10, 20, 30, 40].
# - Usa un bucle o la función sum() para calcular la suma de los elementos.
# - Imprime el resultado con un mensaje descriptivo.
# ------------------------------------------------------------------------------

import array

numeros = array.array('i', [10, 20, 30, 40])
suma = sum(numeros)

print(f"La suma de los elementos del array es: {suma}")
