from abc import ABC, abstractmethod

#CLASE DE ABSTRACTA (CLASE MADRE)

class Servicio(ABC):
    
    def __init__(self, nombre):
        self.nombre = nombre

    #Metodo abstracto para calcular costo
    @abstractmethod
    def calcular_costo(self):
        pass

    #Metodo abstracto para descripción
    @abstractmethod
    def descripcion(self):
        pass


#SUBCLASE 1: SERVICIO DE SALA

class ServicioSala(Servicio):

    def __init__(self, nombre, horas, costo_por_hora):
        super().__init__(nombre)
        self.horas = horas
        self.costo_por_hora = costo_por_hora

    def calcular_costo(self):
        return self.horas * self.costo_por_hora
    
    def descripcion(self):
        return f"Sala reservada por {self.horas} horas"
    
#SUBCLASE 2: SERVICIO DE EQUIPO

class ServicioEquipo(Servicio):

    def __init__(self, nombre, dias, costo_por_dia):
        super().__init__(nombre)
        self.dias = dias
        self.costo_por_dia = costo_por_dia

    def calcular_costo(self):
        return self.dias * self.costo_por_dia
    
    def descripcion(self):
        return f"Equipo alquilado por {self.dias} dias"
    
#SUBCLASE 3: SERVICIO DE ASESORIA

class ServicioAsesoria(Servicio):

    def __init__(self, nombre, horas, tarifa_hora):
        super().__init__(nombre)
        self.horas = horas
        self.tarifa_hora = tarifa_hora

    def calcular_costo(self):
        return self.horas * self.tarifa_hora
    
    def descripcion(self):
        return f"Asesoria durante {self.horas} horas"
    

    
