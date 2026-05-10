from cliente import Cliente
from servicios import ServicioSala, ServicioEquipo, ServicioAsesoria
from reserva import Reservas


print("\n========== SOFTWARE FJ ==========\n")

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



# CONFIRMAR RESERVAS


try:

    reserva1.confirmar_reserva()
    reserva2.confirmar_reserva()

    print("Reservas confirmadas correctamente.\n")

except Exception as e:
    print(f"Error confirmando reservas: {e}")


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

# PRUEBAS DE ERRORES

print("\n===== PRUEBAS DE ERRORES =====\n")


# CLIENTE INVÁLIDO
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
try:

    reserva_error = Reservas(
        "cliente falso",
        sala1,
        -1
    )

except Exception as e:
    print(f"Error detectado correctamente: {e}")


# CONFIRMAR DOS VECES
try:

    reserva1.confirmar_reserva()

except Exception as e:
    print(f"Error detectado correctamente: {e}")


print("\n========== FIN DEL SISTEMA ==========\n")