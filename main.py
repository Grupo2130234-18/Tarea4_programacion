# SISTEMA PRINCIPAL SOFTWARE FJ
# Archivo encargado de ejecutar las pruebas generales
# del sistema de gestión de clientes, servicios y reservas.
# Aquí se validan operaciones exitosas y manejo de errores.

from cliente import Cliente
from servicios import ServicioSala, ServicioEquipo, ServicioAsesoria
from reserva import Reservas


print("\n========== SOFTWARE FJ ==========\n")

# Se crean objetos de tipo Cliente con validaciones
# automáticas de datos personales.
# El bloque try/except evita que el sistema se detenga
# si ocurre un error durante el registro.

# CREACIÓN DE CLIENTES

try:

    cliente1 = Cliente(
        "Pepito Perez",
        "123456789",
        "3001234567",
        "Bogotá"
    )

    cliente2 = Cliente(
        "Maria Lopez",
        "987654321",
        "3019876543",
        "Medellin"
    )

    print("Clientes creados correctamente.\n")

except Exception as e:
    print(f"Error creando clientes: {e}")

# Creación de diferentes servicios especializados
# aplicando herencia y polimorfismo.
# Cada servicio implementa su propio cálculo de costo.

# CREACIÓN DE SERVICIOS

try:

    sala1 = ServicioSala(
        "Sala VIP",
        3,
        50000
    )

    equipo1 = ServicioEquipo(
        "Portatil Gamer",
        2,
        80000
    )

    asesoria1 = ServicioAsesoria(
        "Asesoria Python",
        4,
        120000
    )

    print("Servicios creados correctamente.\n")

except Exception as e:
    print(f"Error creando servicios: {e}")

# Se muestran los servicios registrados utilizando
# métodos sobrescritos en cada clase derivada.

# MOSTRAR SERVICIOS


try:

    print("===== SERVICIOS =====")

    print(f"\nServicio: {sala1.nombre}")
    print(f"Descripción: {sala1.descripcion()}")
    print(f"Costo: ${sala1.calcular_costo()}")

    print(f"\nServicio: {equipo1.nombre}")
    print(f"Descripción: {equipo1.descripcion()}")
    print(f"Costo: ${equipo1.calcular_costo()}")

    print(f"\nServicio: {asesoria1.nombre}")
    print(f"Descripción: {asesoria1.descripcion()}")
    print(f"Costo: ${asesoria1.calcular_costo()}")

except Exception as e:
    print(f"Error mostrando servicios: {e}")

# Asociación entre clientes y servicios mediante
# objetos de tipo Reserva.
# Se valida la correcta integración de clases.

# CREACIÓN DE RESERVAS

try:

    reserva1 = Reservas(
        cliente1,
        sala1,
        1
    )

    reserva2 = Reservas(
        cliente2,
        asesoria1,
        1
    )

    print("\nReservas creadas correctamente.\n")

except Exception as e:
    print(f"Error creando reservas: {e}")

# Confirmación de reservas verificando estados
# y evitando duplicidad en el procesamiento.

# CONFIRMAR RESERVAS


try:

    reserva1.confirmar_reserva()
    reserva2.confirmar_reserva()

    print("Reservas confirmadas correctamente.\n")

except Exception as e:
    print(f"Error confirmando reservas: {e}")

# Cálculo total de cada reserva utilizando
# métodos encapsulados dentro de la clase Reserva.

# MOSTRAR TOTALES

try:

    print("===== TOTALES =====")

    print(f"Total reserva 1: ${reserva1.calcular_total()}")
    print(f"Total reserva 2: ${reserva2.calcular_total()}")

except Exception as e:
    print(f"Error calculando totales: {e}")


# MOSTRAR CLIENTES
try:

    print("\n===== CLIENTES =====")

    cliente1.mostrar_cliente()
    cliente2.mostrar_cliente()

except Exception as e:
    print(f"Error mostrando clientes: {e}")

# BLOQUE DE VALIDACIÓN Y MANEJO DE EXCEPCIONES
# En esta sección se simulan errores controlados para
# comprobar la estabilidad y robustez del sistema.

# PRUEBAS DE ERRORES

print("\n===== PRUEBAS DE ERRORES =====\n")


# CLIENTE INVÁLIDO
# Validación de datos incorrectos en el cliente:
# nombre corto, documento inválido y teléfono incorrecto.
try:

    
    cliente_error = Cliente(
        "Jo",
        "12A",
        "ABC",
        ""
    )

except Exception as e:
    print(f"Error detectado correctamente: {e}")


# SERVICIO INVÁLIDO
# Verificación de restricciones en duración y costos.
# El sistema debe impedir valores negativos.
try:

    servicio_error = ServicioSala(
        "Sala Error",
        -5,
        -1000
    )

    print(servicio_error.calcular_costo())

except Exception as e:
    print(f"Error detectado correctamente: {e}")


# RESERVA INVÁLIDA
# Validación de tipos de datos incorrectos y
# duración inválida en reservas.
try:

    reserva_error = Reservas(
        "cliente falso",
        sala1,
        -1
    )

except Exception as e:
    print(f"Error detectado correctamente: {e}")


# CONFIRMAR DOS VECES
# Prueba de control lógico para evitar confirmar
# una reserva previamente procesada.
try:

    reserva1.confirmar_reserva()

except Exception as e:
    print(f"Error detectado correctamente: {e}")


print("\n========== FIN DEL SISTEMA ==========\n")

# Finalización del sistema y cierre de ejecución.
# Todas las pruebas fueron procesadas correctamente.
