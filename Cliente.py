import logging

# CONFIGURACIÓN DEL ARCHIVO LOGS
logging.basicConfig(
    filename="logs.txt",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


# EXCEPCIÓN PERSONALIZADA
class ClienteError(Exception):
    pass


class Cliente:

    def __init__(self, nombre, cedula, telefono, ciudad, estado=True):

        self._reservas = []

        # Uso de setters para validar desde el inicio
        self.set_nombre(nombre)
        self.set_cedula(cedula)
        self.set_telefono(telefono)
        self.set_ciudad(ciudad)
        self.set_estado(estado)

  
    # GETTERS
  

    def get_nombre(self):
        return self._nombre

    def get_cedula(self):
        return self._cedula

    def get_telefono(self):
        return self._telefono

    def get_ciudad(self):
        return self._ciudad

    def get_estado(self):
        return self._estado

    def get_reservas(self):
        return self._reservas


    # SETTERS CON VALIDACIONES
   

    def set_nombre(self, nombre):

        try:
            if not isinstance(nombre, str):
                raise ClienteError("El nombre debe ser texto.")

            if len(nombre.strip()) < 3:
                raise ClienteError("El nombre debe tener mínimo 3 caracteres.")

            self._nombre = nombre.strip()

        except Exception as e:
            logging.error(f"Error en nombre: {e}")
            raise

    def set_cedula(self, cedula):

        try:
            cedula = str(cedula)

            if not cedula.isdigit():
                raise ClienteError("La cédula solo debe contener números.")

            if len(cedula) < 5:
                raise ClienteError("La cédula es demasiado corta.")

            self._cedula = cedula

        except Exception as e:
            logging.error(f"Error en cédula: {e}")
            raise

    def set_telefono(self, telefono):

        try:
            telefono = str(telefono)

            if not telefono.isdigit():
                raise ClienteError("El teléfono solo debe contener números.")

            if len(telefono) != 10:
                raise ClienteError("El teléfono debe tener 10 dígitos.")

            self._telefono = telefono

        except Exception as e:
            logging.error(f"Error en teléfono: {e}")
            raise

    def set_ciudad(self, ciudad):

        try:
            if not isinstance(ciudad, str):
                raise ClienteError("La ciudad debe ser texto.")

            if len(ciudad.strip()) < 3:
                raise ClienteError("Ciudad inválida.")

            self._ciudad = ciudad.strip()

        except Exception as e:
            logging.error(f"Error en ciudad: {e}")
            raise

    def set_estado(self, estado):

        try:
            if not isinstance(estado, bool):
                raise ClienteError("El estado debe ser True o False.")

            self._estado = estado

        except Exception as e:
            logging.error(f"Error en estado: {e}")
            raise

  
    # MÉTODO PARA AGREGAR RESERVAS

    def agregar_reserva(self, reserva):

        try:

            if reserva is None:
                raise ClienteError("La reserva no puede ser vacía.")

            self._reservas.append(reserva)

        except Exception as e:
            logging.error(f"Error al agregar reserva: {e}")
            raise

    # MÉTODO PARA MOSTRAR DATOS

    def mostrar_cliente(self):

        try:

            print("\n===== DATOS DEL CLIENTE =====")
            print(f"Nombre: {self._nombre}")
            print(f"Cédula: {self._cedula}")
            print(f"Teléfono: {self._telefono}")
            print(f"Ciudad: {self._ciudad}")
            print(f"Estado: {self._estado}")
            print(f"Cantidad de reservas: {len(self._reservas)}")

        except Exception as e:
            logging.error(f"Error mostrando cliente: {e}")
            print("Ocurrió un error al mostrar el cliente.")

        finally:
            print("Proceso finalizado.\n")
