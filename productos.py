VARIABLE_ORCOS = "Orcos"
VARIABLE_HUMANOS = "Humanos"

class Producto:
    def __init__(self):
        self.imagen = ""
        self.descripcion = ""
        self.grupo = ""

class Arma(Producto):
    def __init__(self):
        Producto.__init__(self)

class ArmaHumanos(Arma):
    def __init__(self):
        self.grupo = VARIABLE_HUMANOS
        self.imagen = "imagenes/humanos/arma.png"
        self.descripcion = "Arma de los Humanos"
        
class ArmaOrcos(Arma):
    def __init__(self):
        self.grupo = VARIABLE_ORCOS
        self.imagen = "imagenes/orcos/arma.png"
        self.descripcion = "Arma de los Orcos"

class Escudo(Producto):
    def __init__(self):
        Producto.__init__(self)

class EscudoHumanos(Arma):
    def __init__(self):
        self.grupo = VARIABLE_HUMANOS
        self.imagen = "imagenes/humanos/escudo.png"
        self.descripcion = "Escudo de los Humanos"
        
class EscudoOrcos(Arma):
    def __init__(self):
        self.grupo = VARIABLE_ORCOS
        self.imagen = "imagenes/orcos/escudo.png"
        self.descripcion = "Escudo de los Orcos"

class Montura(Producto):
    def __init__(self):
        Producto.__init__(self)

class MonturaHumanos(Montura):
    def __init__(self):
        self.grupo = VARIABLE_HUMANOS
        self.imagen = "imagenes/humanos/montura.png"
        self.descripcion = "Montura de los Humanos"
        
class MonturaOrcos(Montura):
    def __init__(self):
        self.grupo = VARIABLE_ORCOS
        self.imagen = "imagenes/orcos/montura.png"
        self.descripcion = "Montura de los Orcos"

class Personaje(Producto):
    def __init__(self):
        Producto.__init__(self)

class PersonajeHumanos(Personaje):
    def __init__(self):
        self.grupo = VARIABLE_HUMANOS
        self.imagen = "imagenes/humanos/personaje.png"
        self.descripcion = "Personaje de los Humanos"
        
class PersonajeOrcos(Personaje):
    def __init__(self):
        self.grupo = VARIABLE_ORCOS
        self.imagen = "imagenes/orcos/personaje.png"
        self.descripcion = "Personaje de los Orcos"