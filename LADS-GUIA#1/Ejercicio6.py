# ------------------------------------------------------------------------------
# EJERCICIO 6: Construcción de Mensaje Personalizado con f-Strings
# ------------------------------------------------------------------------------
# Instrucciones:
# - Declara las siguientes variables: nombre (cadena), edad (entero) y puntaje (número).
# - Utiliza f-strings para construir el mensaje:
#   "Hola, [nombre]. Tienes [edad] años y tu puntaje es [puntaje]."
# - Imprime el mensaje resultante.
# ------------------------------------------------------------------------------

nombre = input("Ingresa tu nombre: ")
edad = int(input("Ingresa tu edad: "))
puntaje = float(input("Ingresa tu puntaje: "))

mensaje = f"Hola, {nombre}. Tienes {edad} años y tu puntaje es {puntaje}."
print(mensaje)
