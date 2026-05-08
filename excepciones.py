import logging

#CONFIGURACIÓN DEL ARCHIVO DE LOGS

logging.basicConfig(
    filename="errores.log",
    level=logging.ERROR,
    formate="%(asctime)s - %(levelname)s - %(message)s")

#EXCEPCIONES PERSONALIZADAS

class ClientesError(Exception):
    pass

class ReservaError(Exception):
    pass

class ServicioError(Exception):
    pass

#FUNCIONES PARA MANEJO DE ERRORES

def manejar_error(error):

    try:

        logging.error(f"se produjo un error: {error}")

        print(f"ERROR: {error}")

    except Exception as e:

        print(f"Error inesperado en el sistema de logs: {e}")

    finally:

        print("Proceso de manejo de errores finalizado.")
