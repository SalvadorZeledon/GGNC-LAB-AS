# ------------------------------------------------------------------------------
# EJERCICIO 14: Eliminación de Elementos Duplicados Mediante Conjuntos
# ------------------------------------------------------------------------------
# Instrucciones:
# - Crea una lista de cadenas que contenga elementos repetidos,
#   por ejemplo: ["manzana", "banana", "manzana", "cereza"].
# - Convierte la lista en un conjunto y muestra el conjunto resultante.
# - Explica brevemente en un comentario cómo el uso de conjuntos elimina los duplicados.
# ------------------------------------------------------------------------------

# Los conjuntos (set) eliminan automáticamente los elementos duplicados,
# ya que solo pueden contener valores únicos.

frutas = ["manzana", "banana", "manzana", "cereza"]
frutas_sin_duplicados = set(frutas)

print(f"Frutas sin duplicados: {frutas_sin_duplicados}")
