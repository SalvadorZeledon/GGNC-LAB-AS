# ------------------------------------------------------------------------------
# EJERCICIO 7: Verificación del Formato de un Texto
# ------------------------------------------------------------------------------
# Instrucciones:
# - Solicita una cadena al usuario.
# - Utiliza los métodos isupper() e islower() para comprobar el formato.
# - Si la cadena es completamente mayúscula, muestra "El texto está en mayúsculas".
# - Si es minúscula, muestra "El texto está en minúsculas".
# - De lo contrario, muestra "El texto tiene un formato mixto".
# ------------------------------------------------------------------------------

texto = input("Ingresa un texto: ")

if texto.isupper():
    print("El texto está en mayúsculas.")
elif texto.islower():
    print("El texto está en minúsculas.")
else:
    print("El texto tiene un formato mixto.")
