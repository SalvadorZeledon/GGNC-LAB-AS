# ------------------------------------------------------------------------------
# EJERCICIO 4: Análisis de Texto - Contador de Caracteres, Palabras y Espacios
# ------------------------------------------------------------------------------
# Instrucciones:
# - Solicita al usuario que ingrese una frase o párrafo.
# - Usa len() para contar el número total de caracteres.
# - Emplea split() para dividir el texto en palabras y cuenta el número de palabras.
# - Recorre la cadena contando el número de espacios (usa el método count(" ")).
# - Imprime los tres resultados con mensajes descriptivos.
# ------------------------------------------------------------------------------

texto = input("Ingresa una frase o párrafo: ")

total_caracteres = len(texto)
total_palabras = len(texto.split())
total_espacios = texto.count(" ")

print(f"Total de caracteres: {total_caracteres}")
print(f"Total de palabras: {total_palabras}")
print(f"Total de espacios: {total_espacios}")
