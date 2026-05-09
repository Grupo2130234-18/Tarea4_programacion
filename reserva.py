from datetime import datetime 
from cliente import Cliente
import logging

from servicios import Servicio
# CONFIGURACIÓN DEL ARCHIVO LOGS
logging.basicConfig(
    filename="logs.txt",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


class ReservaError(Exception):
    pass

## Clase para manejar reservas
class Reservas:
    def __init__(self, cliente, servicio, duracion, estado="Pendiente", precio=0):
        ## Agregar fecha de reserva para tener un registro temporal de cuándo se hizo la reserva
        self._fecha_reserva = datetime.now() 
        
        ## Validaciones iniciales
        if not isinstance(cliente, Cliente):
            raise ReservaError("El cliente debe ser una instancia de Cliente")

        if not isinstance(servicio, Servicio):
            raise ReservaError("El servicio debe ser una instancia de Servicio")
        
        if duracion <= 0:
            raise ReservaError("La duración debe ser mayor a 0")
        
        
        ## Asignar atributos
        self._cliente = cliente
        self._servicio = servicio
        self._duracion = duracion
        self._estado = estado
        
        self._precio = precio
        # Agregar esta reserva a la lista de reservas del cliente
        self._cliente.agregar_reserva(self)


    # getters
    def get_cliente(self):
        return self._cliente

    def get_servicio(self):
        return self._servicio

    def get_duracion(self):
        return self._duracion

    def get_estado(self):
        return self._estado

    def get_precio(self):
        return self._precio
    
    
    # Setters
    def set_duracion(self, duracion):
        if duracion <= 0:
            raise ReservaError("La duración debe ser positiva")
        self._duracion = duracion
    
    def set_estado(self, estado):
        estados_validos = ["Pendiente", "Confirmada", "Cancelada"]
        if estado not in estados_validos:
            raise ReservaError(f"Estado inválido. Use: {estados_validos}")
        self._estado = estado
    
    

    # MÉTODOS PARA VALIDAR DATOS DE RESERVA
    def confirmar_reserva(self):
        try:
            if self._estado == "Confirmada":
                raise ReservaError("La reserva ya está confirmada.")

            if self._estado == "Cancelada":
                raise ReservaError("No se puede confirmar una reserva cancelada.")

            self._estado = "Confirmada"
            logging.info(
                f"Reserva confirmada para cliente: {self._cliente.get_nombre()}")

        except ReservaError as e:
            logging.error(f"Error al confirmar reserva: {e}")
            raise

        except Exception as e:  # Captura CUALQUIER otro error inesperado
            logging.error(f"Error inesperado al confirmar: {e}")
            raise
        
## Metodo para cancelar reserva
    def cancelar_reserva(self):
        try:
            if self._estado == "Cancelada":
                raise ReservaError("La reserva ya está cancelada.")

         
            self._estado = "Cancelada"
            logging.info(
                    f"Reserva cancelada para cliente: {self._cliente.get_nombre()}")
            return True
        
        except ReservaError as e:
            logging.error(f"Error al cancelar reserva: {e}")
            return False
        
        except Exception as e:
            logging.error(f"Error inesperado al cancelar: {e}")
            return False

## Método para calcular el total de la reserva
    def calcular_total(self):
        try:
            if self._servicio is None:
                raise ReservaError("El servicio no puede ser vacío.")
            if self._duracion <= 0:
                raise ReservaError("Duracion  Invalida.")
            costo_por_reserva = self._servicio.calcular_costo()
            total = costo_por_reserva * self._duracion
         
            logging.info(f"Total calculado: ${total}")
            return total
        
        except ReservaError as e:
            logging.error(f"Error al calcular total: {e}")
            raise
        except Exception as e:
            logging.error(f"Error inesperado al calcular total: {e}")
            raise
