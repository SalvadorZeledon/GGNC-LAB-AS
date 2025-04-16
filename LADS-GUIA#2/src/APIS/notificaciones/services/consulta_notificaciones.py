from database.database import get_connection

def get_notification_data(id_estudiantes):
    connection = get_connection()
    query = """
        SELECT nombre, apellido, email, carnet
        FROM estudiantes
        WHERE id_estudiantes = %s
    """
    results = []
    try:
        with connection.cursor() as cursor:
            cursor.execute(query, (id_estudiantes,))
            rows = cursor.fetchall()
            for row in rows:
                results.append({
                    "nombre_estudiante": row[0],
                    "apellido_estudiante": row[1],
                    "correo": row[2],
                    "carnet": row[3]
                })
    except Exception as e:
        raise Exception(f"Error al ejecutar get_notification_data: {str(e)}")
    finally:
        connection.close()
    return results
