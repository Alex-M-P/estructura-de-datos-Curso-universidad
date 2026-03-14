class Vehiculo:
    def __init__(self, marca, modelo, anio, tipo):
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.tipo = tipo

    def mostrar_informacion(self):
        return f"{self.marca} {self.tipo} {self.modelo} ({self.anio})"