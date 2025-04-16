# ------------------------------------------------------------------------------
# EJERCICIO 5: Reemplazo de Palabras en una Cadena de Texto
# ------------------------------------------------------------------------------
# Instrucciones:
# - Solicita al usuario una oración.
# - Pide que ingrese la palabra que desea buscar y la palabra por la que quiere reemplazarla.
# - Usa el método replace() para efectuar la sustitución y muestra el texto modificado.
# ------------------------------------------------------------------------------

oracion = input("Ingresa una oración: ")
buscar = input("Palabra que deseas reemplazar: ")
reemplazo = input("Palabra por la que deseas reemplazarla: ")

nueva_oracion = oracion.replace(buscar, reemplazo)

print("Texto modificado:")
print(nueva_oracion)
