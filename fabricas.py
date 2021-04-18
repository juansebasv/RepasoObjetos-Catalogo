from productos import *

class Fabrica:
    def crear_producto(self, producto):
        pass

class FabricaHumanos(Fabrica):
    def crear_producto(self, producto):
        producto.getProductoHumanos()
        return producto

class FabricaOrcos(Fabrica):
    def crear_producto(self, producto):
        producto.getProductoOrcos()
        return producto